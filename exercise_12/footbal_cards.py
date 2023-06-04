team_information = input().split(" ")
terminated = False
teams_info = []
for team_num in range(1, 12):
    teams_info.append(f"A-{team_num}")
    teams_info.append(f"B-{team_num}")

for player in team_information:
    if player in teams_info:
        teams_info.remove(player)
        if any([sum([x.count("A") for x in teams_info]) < 7, sum([x.count("A") for x in teams_info]) < 7]):
            terminated = True
            break

print(f"Team A - {sum([x.count('A') for x in teams_info])}; Team B - {sum([x.count('B') for x in teams_info])}")
if terminated:
    print("Game was terminated")