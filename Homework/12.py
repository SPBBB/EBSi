# input sports info.
team_name = input("Enter the team name: ")
opponent_name = input("Enter the opponent team name: ")
team_score = int(input(f"Enter the {team_name}'s score: "))
opponent_score = int(input(f"Enter the {opponent_name}'s score: "))
key_player = input("Enter the key player's name: ")

# print sports news.
print(f"[Sports News] The {team_name} won against the {opponent_name} with a final score of {team_score} to {opponent_score}.")
print(f"The highlight of the game was {key_player}, who played a decisive role in securing the victory. Fans are eagerly awaiting the next match.")