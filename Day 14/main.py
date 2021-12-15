import random
import game_data
import art

#print(game_data.data)

is_correct = True

def random_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

while is_correct:
    print(art.logo)
    total_score = 0
    compare_a = random.choice(game_data.data)
    compare_b = random.choice(game_data.data)
    if compare_a == compare_b:
        compare_b == random.choice(game_data.data)
    
    print(f"Compare A: {random_data(compare_a)}")
    print(art.vs)
    print(f"Compare B: {random_data(compare_b)}")

    answer = input("Who has more followers? Type 'A' or 'B' :").lower()

    if compare_a['follower_count'] > compare_b['follower_count']:
        more_follower = 'a'
    else:
        more_follower = 'b'

    if answer == more_follower:
        total_score += 1
        print(f"Correct, {compare_a['name']} have {compare_a['follower_count']} followers and {compare_b['name']} have {compare_b['follower_count']} followers")
        print(f"Current score is : {total_score}\n")
    else:
        print(f"Wrong, {compare_a['name']} have {compare_a['follower_count']} followers and {compare_b['name']} have {compare_b['follower_count']} followers")
        print(f"Current score is : {total_score}\n")
        is_correct = False
