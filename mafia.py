import random



# Function to distribute roles to players
def distribute_roles(players):
    num_players = len(players)
    num_mafia = num_players // 3

    roles = ['Mafia'] * num_mafia + ['Citizen'] * (num_players - num_mafia)
    random.shuffle(roles)

    for i, player in enumerate(players):
        player['role'] = roles[i]

# Function to simulate a night round
def night_round(players):
    print("Night round:")
    for player in players:
        if player['role'] == 'Mafia':
            target = random.choice(players)
            while target['role'] == 'Mafia':
                target = random.choice(players)
            print(f"(Mafia) chose to eliminate {target['name']}")
            players.remove(target)

# Function to simulate a day round
def day_round(players):
    print("Day round:")
    for player in players:
        print(f"{player['name']} ")

    accused = input("Accuse a player: ")
    vote_count = {}
    for player in players:
        vote_count[player['name']] = 0

    for player in players:
        if player['name'] != accused:
            vote = random.choice(players)
            vote_count[vote['name']] += 1

    max_votes = max(vote_count.values())
    accused_players = [player for player, votes in vote_count.items() if votes == max_votes]

    if len(accused_players) == 1:
        eliminated = next(player for player in players if player['name'] == accused_players[0])
        players.remove(eliminated)
        print(f"{eliminated['name']} ({eliminated['role']}) was eliminated.")
    else:
        print("No one was eliminated.")

# Function to check if the game is over
def game_over(players):
    num_mafia = sum(1 for player in players if player['role'] == 'Mafia')
    num_citizens = len(players) - num_mafia

    if num_mafia == 0:
        print("The citizens win!")
        return True
    elif num_mafia >= num_citizens:
        print("The mafia win!")
        return True
    else:
        return False

# Main game loop
def play_game():
    print("Welcome to Mafia Card Game!")



    num_players = int(input("Enter the number of players: "))

    players = []
    for i in range(num_players):
        name = input(f"Enter the name of Player {i+1}: ")
        player = {'name': name, 'role': ''}
        players.append(player)

    distribute_roles(players)

    while not game_over(players):
        night_round(players)
        day_round(players)

play_game()




