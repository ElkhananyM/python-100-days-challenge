import timeit

from game_data import data
import art
import random
# picks A and B from the data dictionary
def pick_data():
    a = random.choice(data)
    while True:
        b = random.choice(data)
        if b != a:
            break
    return a, b

def pick_new_b():
    return random.choice(data)

# compare A and B's follower_count to see who's higher
def compare_data(a_data, b_data, player):
    correct_choice = "a" if a_data["follower_count"] > b_data["follower_count"] else "b"
    if player == correct_choice:
        return True
    else:
        return False

score = 0
a, b = pick_data()

while True:
    print(art.logo)
    print(f"Compare A: {a["name"]}, {a["description"]}, {a["country"]}. {a["follower_count"]}")
    print(art.vs)
    print(f"Against B: {b["name"]}, {b["description"]}, {b["country"]}. {b["follower_count"]}")
    player_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    if compare_data(a, b, player_pick):
        score += 1
        a = b
        while True:
            b = pick_new_b()
            if b != a:
                break
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Your final score is {score}.")
        break
    print(f"You're right! Current score is {score}")