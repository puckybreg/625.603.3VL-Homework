import random

# Function for simulating a series
def play_series(prob):
    team_a_series_count = 0
    team_b_series_count = 0
    while team_a_series_count <= 4 and team_b_series_count <= 4:

        # Check if either team has won already
        if team_a_series_count == 4:
            return "team_a"
        elif team_b_series_count == 4:
            return "team_b"

        # If not simulate another game
        game_outcome = random.randint(0, 100)
        if game_outcome <= prob:
            team_a_series_count += 1
        else:
            team_b_series_count += 1




def main():
    team_a_series_counter = 0
    team_b_series_counter = 0
    chance_of_winning = 55

    for i in range(1000):
       series_victor = play_series(chance_of_winning)

       if series_victor == "team_a":
           team_a_series_counter += 1
       else:
           team_b_series_counter += 1

    print(f"Team A won {team_a_series_counter} series & Team B won {team_b_series_counter} series")
    print(f"The probablity that Team A will win a world series against Team B, given our 1000 trails is {team_a_series_counter/1000}")



if __name__ == "__main__":
    main()