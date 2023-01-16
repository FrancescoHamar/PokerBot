import discord
import random

from discord.ext import commands

print(discord.__version__)

usedCards = []

first_player = ''
second_player = ''

gameOn = False

currentCard = ''

suits = {
    1: 'Hearths',
    2: 'Diamonds',
    3: 'Clubs',
    4: 'Spades'
}

numbers = {
    1: 'Ace',
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}

player1 = []
player2 = []
player1Actual = []
player2Actual = []
player1ActualValues = []
player2ActualValues = []


client = commands.Bot(command_prefix='!')

first_channel = client.get_channel(756456123871133716)
second_channel = client.get_channel(756456150744039474)
main_channel = client.get_channel(756444146297864232)

first_change = False
second_change = False

check = 0


def hand_start():
    global player1
    global player2
    global currentCard
    global gameOn

    for o in range(5):
        currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        while currentCard in usedCards:
            currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        player1.append(currentCard)
        usedCards.append(currentCard)

        currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        while currentCard in usedCards:
            currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        player2.append(currentCard)
        usedCards.append(currentCard)


def change_card(card, player):
    global player1
    global player2
    global currentCard

    if player == 1:
        currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        while currentCard in usedCards:
            currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        player1[card] = currentCard
        usedCards.append(currentCard)

    if player == 2:
        currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        while currentCard in usedCards:
            currentCard = f'{numbers[random.randint(1, 13)]} of {suits[random.randint(1, 4)]}'
        player2[card] = currentCard
        usedCards.append(currentCard)


def done_check(player):
    global check

    check = check + 1

    if check == 1:
        print("Changes have been done.\n Analyzing winner...")
        winner_check()
        if player == 1:
            player1Actual.sort()
            print(player1Actual)

            player1ActualValues.append(value(player1Actual[0]))
            player1ActualValues.append(value(player1Actual[1]))
            player1ActualValues.append(value(player1Actual[2]))
            player1ActualValues.append(value(player1Actual[3]))
            player1ActualValues.append(value(player1Actual[4]))

            player1ActualValues.sort()
            print(player1ActualValues)

            return actual_ranker(player1Actual, player1ActualValues, 1)

        if player == 2:
            player2Actual.sort()
            print(player2Actual)

            player2ActualValues.append(value(player2Actual[0]))
            player2ActualValues.append(value(player2Actual[1]))
            player2ActualValues.append(value(player2Actual[2]))
            player2ActualValues.append(value(player2Actual[3]))
            player2ActualValues.append(value(player2Actual[4]))

            player2ActualValues.sort()
            print(player2ActualValues)

            print(actual_ranker(player2Actual, player2ActualValues, 2))


def card_converter(name, card, apposite, player):
    global player1Actual
    global player2Actual
    global player1
    global player2

    if player == 1:
        if name in str(card):
            player1Actual.append(apposite)
            if "Diamonds" in card:
                player1Actual[player1.index(card)] = player1Actual[player1.index(card)] + 13
            elif "Clubs" in card:
                player1Actual[player1.index(card)] = player1Actual[player1.index(card)] + 26
            elif "Spades" in card:
                player1Actual[player1.index(card)] = player1Actual[player1.index(card)] + 39

    elif player == 2:
        if name in str(card):
            player2Actual.append(apposite)
            if "Diamonds" in card:
                player2Actual[player2.index(card)] = player2Actual[player2.index(card)] + 13
            elif "Clubs" in card:
                player2Actual[player2.index(card)] = player2Actual[player2.index(card)] + 26
            elif "Spades" in card:
                player2Actual[player2.index(card)] = player2Actual[player2.index(card)] + 39


def winner_check():
    for card in player1:
        card_converter("Ace", card, 1, 1)
        card_converter("2", card, 2, 1)
        card_converter("3", card, 3, 1)
        card_converter("4", card, 4, 1)
        card_converter("5", card, 5, 1)
        card_converter("6", card, 6, 1)
        card_converter("7", card, 7, 1)
        card_converter("8", card, 8, 1)
        card_converter("9", card, 9, 1)
        card_converter("10", card, 10, 1)
        card_converter("Jack", card, 11, 1)
        card_converter("Queen", card, 12, 1)
        card_converter("King", card, 13, 1)

    for card in player2:
        card_converter("Ace", card, 1, 2)
        card_converter("2", card, 2, 2)
        card_converter("3", card, 3, 2)
        card_converter("4", card, 4, 2)
        card_converter("5", card, 5, 2)
        card_converter("6", card, 6, 2)
        card_converter("7", card, 7, 2)
        card_converter("8", card, 8, 2)
        card_converter("9", card, 9, 2)
        card_converter("10", card, 10, 2)
        card_converter("Jack", card, 11, 2)
        card_converter("Queen", card, 12, 2)
        card_converter("King", card, 13, 2)

    #  FUNCTIONS FOR CARD RANKING BELOW


def value(card):
    if card > 39:
        card = card - 39
    elif card > 26:
        card = card - 26
    elif card > 13:
        card = card - 13
    else:
        card = card
    return card


def suit(card):
    if card > 39:
        card = 4
    elif card > 26:
        card = 3
    elif card > 13:
        card = 2
    else:
        card = 1
    return card


def flush(numbered_cards):
    if suit(numbered_cards[0]) == suit(numbered_cards[1]) == suit(numbered_cards[2]) == suit(numbered_cards[3]) == \
            suit(numbered_cards[4]):
        return True
    else:
        return False


def straight(valued_cards):
    if valued_cards[0] == valued_cards[1] - 1 == valued_cards[2] - 2 == valued_cards[3] - 3 == valued_cards[4] - 4 or \
            valued_cards[0] == valued_cards[1] - 9 == valued_cards[2] - 10 == \
            valued_cards[3] - 11 == valued_cards[4] - 12:
        return True
    else:
        return False


def straight_flush(numbered_cards, valued_cards):
    if flush(numbered_cards) and straight(valued_cards):
        return True
    else:
        return False


def poker(valued_cards):
    if valued_cards[0] == valued_cards[1] == valued_cards[2] == valued_cards[3] or \
            valued_cards[1] == valued_cards[2] == valued_cards[3] == valued_cards[4]:
        return True
    else:
        return False


def tris(valued_cards):
    if valued_cards[0] == valued_cards[1] == valued_cards[2] or \
            valued_cards[1] == valued_cards[2] == valued_cards[3] or \
            valued_cards[2] == valued_cards[3] == valued_cards[4]:
        return True
    else:
        return False


def two_pair(valued_cards):
    if valued_cards[0] == valued_cards[1]:
        if valued_cards[2] == valued_cards[3]:
            return True
        elif valued_cards[3] == valued_cards[4]:
            return True
    elif valued_cards[1] == valued_cards[2] and \
            valued_cards[3] == valued_cards[4]:
        return True
    else:
        return False


def pair(valued_cards):
    if valued_cards[0] == valued_cards[1] or valued_cards[1] == valued_cards[2] or \
                valued_cards[2] == valued_cards[3] or valued_cards[3] == valued_cards[4]:
        return True
    else:
        return False


def full_house(valued_cards):
    if (valued_cards[0] == valued_cards[1] == valued_cards[2] and
            valued_cards[3] == valued_cards[4]) or \
            (valued_cards[2] == valued_cards[3] == valued_cards[4] and
                valued_cards[0] == valued_cards[1]):
        return True
    else:
        return False


def actual_ranker(numbered_cards, valued_cards, player):
    if player == 1:
        if straight_flush(numbered_cards, valued_cards):
            if 1 in valued_cards and 10 in valued_cards:
                return f"Straight Flush base 10 with suit {suit(numbered_cards[0])}"
            else:
                return f"Straight Flush base {valued_cards[0]} with suit {suit(numbered_cards[0])}"
        elif poker(valued_cards):
            return final_poker(valued_cards)
        elif flush(numbered_cards):
            return f"Flush {suit(numbered_cards[0])}"
        elif full_house(valued_cards):
            return final_full(valued_cards)
        elif straight(valued_cards):
            if 1 in valued_cards and 10 in valued_cards:
                return f"Straight base 10"
            else:
                return f"Straight base {valued_cards[0]}"
        elif tris(valued_cards):
            if valued_cards[0] == numbered_cards[1]:
                return f"Three of a kind {valued_cards[1]}"
            elif valued_cards[3] == valued_cards[4]:
                return f"Three of a kind {valued_cards[4]}"
            else:
                return f"Three of a kind {valued_cards[2]}"
        elif two_pair(valued_cards):
            return final_two_pair(valued_cards)
        elif pair(valued_cards):
            return final_pair(valued_cards)
        else:
            if 1 in valued_cards:
                return final_high_card(1, valued_cards, numbered_cards)
            else:
                for a in range(12):
                    if final_high_card(13 - a, valued_cards, numbered_cards) is not None:
                        return final_high_card(13 - a, valued_cards, numbered_cards)


def final_pair(valued_cards):
    for n in range(5):
        if valued_cards[n] == valued_cards[n+1]:
            return f"Pair of {valued_cards[n]}"


def final_two_pair(valued_cards):
    if valued_cards[4] == valued_cards[3]:
        if valued_cards[1] == valued_cards[2]:
            return f"Two Pair of {valued_cards[4]} and {valued_cards[2]}"
        else:
            if 1 in valued_cards:
                return f"Two Pair of Aces and {valued_cards[3]}"
            else:
                return f"Two Pair of {valued_cards[3]} and {valued_cards[0]}"
    else:
        if 1 in valued_cards:
            return f"Two Pair of Aces and {valued_cards[4]}"
        else:
            return f"Two Pair of {valued_cards[3]}s and {valued_cards[0]}"


def final_full(valued_cards):
    if valued_cards[1] == valued_cards[2]:
        return f"Full House with tris of {valued_cards[0]} and pair of {valued_cards[4]}"
    else:
        return f"Full House with tris of {valued_cards[4]} and pair of {valued_cards[1]}"


def final_poker(valued_cards):
    if valued_cards[0] == valued_cards[1]:
        return f"Poker {valued_cards[0]}"
    else:
        return f"Poker {valued_cards[1]}"


def final_high_card(card, valued_cards, numbered_cards):
    if card in valued_cards:
        for a in range(4):
            if card + (a * 13) in numbered_cards:
                return f"Highcard of {undo_converter(card + (a * 13))} ({card + (a * 13)})"


def undo_converter(card):
    print(card)
    for a in range(4):
        print(f"Current value: {card - (13 * (3 - a))}")
        print(f"Subbed value: {13 * (3 - a)}")
        if card > (13 * (3 - a)):
            print(f"a is {a}")
            if card - (13 * (3 - a)) == 1:
                if a == 0:
                    return f"Ace of Spades"
                elif a == 1:
                    return f"Ace of Clubs"
                elif a == 2:
                    return f"Ace of Diamonds"
                else:
                    return f"Ace of Hearths"
            elif card - (13 * (3 - a)) == 13:
                if a == 0:
                    return f"King of Spades"
                elif a == 1:
                    return f"King of Clubs"
                elif a == 2:
                    return f"King of Diamonds"
                else:
                    return f"King of Hearths"
            elif card - (13 * (3 - a)) == 12:
                if a == 0:
                    return f"Queen of Spades"
                elif a == 1:
                    return f"Queen of Clubs"
                elif a == 2:
                    return f"Queen of Diamonds"
                else:
                    return f"Queen of Hearths"
            elif card - (13 * (3 - a)) == 11:
                if a == 0:
                    return f"Jack of Spades"
                elif a == 1:
                    return f"Jack of Clubs"
                elif a == 2:
                    return f"Jack of Diamonds"
                else:
                    return f"Jack of Hearths"
            else:
                if a == 0:
                    return f"{card - (13 * (3 - a))} of Spades"
                elif a == 1:
                    return f"{card - (13 * (3 - a))} of Clubs"
                elif a == 2:
                    return f"{card - (13 * (3 - a))} of Diamonds"
                else:
                    return f"{card - (13 * (3 - a))} of Hearths"


@client.command()
async def play(ctx, player_id):
    global first_player
    global second_player
    global gameOn
    global first_channel
    global second_channel
    global main_channel

    first_channel = client.get_channel(756456123871133716)
    second_channel = client.get_channel(756456150744039474)
    main_channel = client.get_channel(756444146297864232)

    if not gameOn:
        gameOn = True

        await main_channel.purge(limit=100)
        await first_channel.purge(limit=100)
        await second_channel.purge(limit=100)

        #  role1 = discord.utils.get(ctx.guild.roles, name="Poker-Player-1")
        #  role2 = discord.utils.get(ctx.guild.roles, name="Poker-Player-2")

        print(player_id)

        first_player = f'<@!{ctx.author.id}>'
        second_player = player_id

        print(first_player)
        print(second_player)

        #  await first_player.add_roles(role1)
        #  await second_player.add_roles(role2)

        hand_start()

        await main_channel.send(f"{first_player} go to Player 1 channel.")
        await main_channel.send(f"{second_player} go to Player 2 channel.")

        await first_channel.send(f"```PLAYER 1 CURRENT CARDS:\n1:  {player1[0]}\n2:  {player1[1]}\n3:  {player1[2]}\n"
                                 f"4:  {player1[3]}\n5:  {player1[4]}\n```")
        await second_channel.send(f"```PLAYER 2 CURRENT CARDS:\n1:  {player2[0]}\n2:  {player2[1]}\n3:  {player2[2]}\n"
                                  f"4:  {player2[3]}\n5:  {player2[4]}\n```")

        await first_channel.send(f"```Which cards would you like to change? Remember, you can change up to four "
                                 f"cards.```\n(Answer by using the command '!change' and then specify which cards would"
                                 f" you like to change. Example: '!change 1 3 4' if you wish to change your first, "
                                 f"third, and fourth card or '!change 0' if you don't wish to change any card)")
        await second_channel.send(f"```Which cards would you like to change? Remember, you can change up to four "
                                  f"cards.```\n(Answer by using the command '!change' and then specify which cards "
                                  f"would you like to change. \nExample: '!change 1 3 4' if you wish to change your "
                                  f"first, third, and fourth card or '!change 0' if you don't wish to change "
                                  f"any card)")

    else:
        await ctx.send("A game is already in progress! Wait until it ends to play")


@client.command()
async def change(ctx, *, cards):
    global first_player
    global second_player
    global player1
    global player2
    global first_change
    global second_change
    global main_channel

    main_channel = client.get_channel(756444146297864232)

    print(first_player)
    print(second_player)

    first_player = first_player.translate({ord(i): None for i in '!@<>'})

    if str(ctx.author.id) == str(first_player) and not first_change:
        print("Player one recognized")
        first_change = 0

        if "One" in cards.capitalize() or "1" in cards:
            change_card(0, 1)
            first_change = first_change + 1

        if "Two" in cards.capitalize() or "2" in cards:
            change_card(1, 1)
            first_change = first_change + 1

        if "Three" in cards.capitalize() or "3" in cards:
            change_card(2, 1)
            first_change = first_change + 1

        if "Four" in cards.capitalize() or "4" in cards:
            change_card(3, 1)
            first_change = first_change + 1

        if "Five" in cards.capitalize() or "5" in cards:
            change_card(4, 1)
            first_change = first_change + 1

        if "Zero" in cards.capitalize() or "0" in cards:
            await ctx.send("Servito!")

        await first_channel.send(
            f"```PLAYER 1 CURRENT CARDS:\n1:  {player1[0]}\n2:  {player1[1]}\n3:  {player1[2]}\n"
            f"4:  {player1[3]}\n5:  {player1[4]}\n```")

        await main_channel.send(f"```Player 1 changed {first_change} cards!```")
        await main_channel.send(f"```Player One has a {done_check(1)}```")

    elif str(ctx.author.id) == str(first_player) and first_change:
        await first_channel.send("You can only change your cards once in a game")

    if str(ctx.author) == str(second_player) and not second_change:
        second_change = 0
        print("Player two recognized")
        if "One" in cards or "1" in cards.capitalize():
            change_card(0, 2)
            second_change = second_change + 1

        if "Two" in cards or "2" in cards.capitalize():
            change_card(1, 2)
            second_change = second_change + 1

        if "Three" in cards or "3" in cards.capitalize():
            change_card(2, 2)
            second_change = second_change + 1

        if "Four" in cards or "4" in cards.capitalize():
            change_card(3, 2)
            second_change = second_change + 1

        if "Five" in cards or "5" in cards.capitalize():
            change_card(4, 2)
            second_change = second_change + 1

        if "Zero" in cards or "0" in cards:
            await ctx.send("Servito!")

        await second_channel.send(
            f"```PLAYER 2 CURRENT CARDS:\n1:  {player2[0]}\n2:  {player2[1]}\n3:  {player2[2]}\n"
            f"4:  {player2[3]}\n5:  {player2[4]}\n```")

        await main_channel.send(f"```Player 2 changed {second_change} cards!```")
        done_check(2)

    elif str(ctx.author.id) == str(second_player) and second_change:
        await second_channel.send("You can only change your cards once in a game")


@client.command()
async def clear(ctx, amount=50):
    await ctx.channel.purge(limit=amount)


@client.command()
async def quitGame(ctx, amount=50):
    global gameOn
    global first_channel
    global second_channel
    global main_channel
    global first_change
    global second_change
    global check
    global player1
    global player2
    global player1Actual
    global player2Actual
    global player1ActualValues
    global player2ActualValues
    global first_player
    global second_player
    global usedCards

    first_channel = client.get_channel(756456123871133716)
    second_channel = client.get_channel(756456150744039474)
    main_channel = client.get_channel(756444146297864232)

    first_player = first_player.translate({ord(i): None for i in '!@<>'})

    if str(first_player) == str(ctx.author.id):
        await first_channel.purge(limit=amount)
        await second_channel.purge(limit=amount)
        await main_channel.purge(limit=amount)
        gameOn = False
        first_change = False
        second_change = False
        check = 0

        player1 = []
        player2 = []
        player1Actual = []
        player2Actual = []
        player1ActualValues = []
        player2ActualValues = []
        first_player = ''
        second_player = ''
        usedCards = []

    else:
        await ctx.send("You cannot stop the game as you are not in a game currently, or you are not the First Player")


@client.command()
async def newHand(ctx, amount=50):
    global gameOn
    global first_channel
    global second_channel
    global main_channel
    global first_change
    global second_change
    global check
    global player1
    global player2
    global player1Actual
    global player2Actual
    global player1ActualValues
    global player2ActualValues
    global first_player
    global second_player
    global usedCards

    print(first_player)
    print(ctx.author.id)

    first_player = first_player.translate({ord(i): None for i in '!@<>'})

    if str(first_player) == str(ctx.author.id):
        first_channel = client.get_channel(756456123871133716)
        second_channel = client.get_channel(756456150744039474)
        main_channel = client.get_channel(756444146297864232)

        await first_channel.purge(limit=amount)
        await second_channel.purge(limit=amount)
        await main_channel.purge(limit=amount)
        gameOn = False
        first_change = False
        second_change = False
        check = 0

        player1 = []
        player2 = []
        player1Actual = []
        player2Actual = []
        player1ActualValues = []
        player2ActualValues = []
        usedCards = []

        hand_start()

        first_player = f'<@!{ctx.author.id}>'

        await main_channel.send(f"{first_player} go to Player 1 channel.")
        await main_channel.send(f"{second_player} go to Player 2 channel.")

        await first_channel.send(f"```PLAYER 1 CURRENT CARDS:\n1:  {player1[0]}\n2:  {player1[1]}\n3:  {player1[2]}\n"
                                 f"4:  {player1[3]}\n5:  {player1[4]}\n```")
        await second_channel.send(f"```PLAYER 2 CURRENT CARDS:\n1:  {player2[0]}\n2:  {player2[1]}\n3:  {player2[2]}\n"
                                  f"4:  {player2[3]}\n5:  {player2[4]}\n```")

        await first_channel.send(f"```Which cards would you like to change? Remember, you can change up to four "
                                 f"cards.```\n(Answer by using the command '!change' and then specify which cards would"
                                 f" you like to change. Example: '!change 1 3 4' if you wish to change your first, "
                                 f"third, and fourth card or '!change 0' if you don't wish to change any card)")
        await second_channel.send(f"```Which cards would you like to change? Remember, you can change up to four "
                                  f"cards.```\n(Answer by using the command '!change' and then specify which cards "
                                  f"would you like to change. \nExample: '!change 1 3 4' if you wish to change your "
                                  f"first, third, and fourth card or '!change 0' if you don't wish to change "
                                  f"any card)")

    else:
        await ctx.send("You either have no current games in progress to restart or you are not the first player, "
                       "ask your opponent to restart the game if that is the case.")


print("Bot starting up")


client.run("NzU2NDM2OTA4OTE3MTI5Mjc3.X2R0xQ.ecmvFirEjwb-U4ehmXru6Wf3INE")
