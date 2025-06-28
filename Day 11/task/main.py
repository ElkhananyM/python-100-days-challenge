import random
import art

def check_win(player, computer):
    if sum(player) == 21:
        print(f"You have BlackJack! {sum(player)} You win! 🤯")
        return False

    if sum(computer) == 21:
        print(f"Computer has BlackJack! {sum(computer)} You lose! 🤯")
        return False

    if sum(player) > 21:
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer[0]}, final score: {sum(computer)}")
        print("You went over. You lose! 😭")
        return False

    if sum(player) == sum(computer):
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer[0]}, final score: {sum(computer)}")
        print("You and the Computer are tied. It's a draw! 🤔")
        return False

    if sum(computer) > 21:
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
        print("Computer went over. You win! 😎")

    elif sum(player) > sum(computer):
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
        print("Your hand is higher than Computer. You win! 😎")
    else:
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
        print("Your hand is lower than Computer. You lose! 😭")

    return False
def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = random.choices(cards, k=2)
    cpu_cards = random.choices(cards, k=2)
    print(art.logo)

    while True:
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {cpu_cards[0]}")
        print(f"***CPU CARDS {cpu_cards}")
        proceed = input("Type 'y' to get another card, type 'n' to pass: ")
        if proceed == "y":
            player_cards.append(random.choice(cards))
            if sum(player_cards) > 21:
                if check_win(player_cards, cpu_cards) is False:
                    break
            else:
                continue
        else:
            while sum(cpu_cards) < 17:
                cpu_cards.append(random.choice(cards))
            if check_win(player_cards, cpu_cards) is False:
                break

play = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")
if play == 'y':
    blackjack()
while input("Would you like to play another round? 'y' or 'n': ") == "y":
    blackjack()

#---------------------------------------------------------------------------------------


def deal_card():
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


import timeit

code1 = """
result = []
for i in range(1000):
    result.append(i * 2)
"""

code2 = """
result = [i * 2 for i in range(1000)]
"""

time1 = timeit.timeit(stmt=code1, number=10000)
time2 = timeit.timeit(stmt=code2, number=10000)


print(f"Code 1 execution time: {time1}")
print(f"Code 2 execution time: {time2}")