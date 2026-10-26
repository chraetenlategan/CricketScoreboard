from GameInfo import GetGameInfo
from players import PlayerStats
from events import Events

get_game_info = GetGameInfo()
format_name, overs = get_game_info.get_format()
team1, team2 = get_game_info.get_team_names()
toss_winner, toss_decision, toss_loser = get_game_info.toss_information(team1, team2)
team_batting = toss_winner if toss_decision == 'bat' else toss_loser
team_bowling = toss_loser if toss_decision == 'bat' else toss_winner
team1_players = get_game_info.create_player_list(team1)
team2_players = get_game_info.create_player_list(team2)

for player in team1_players:
    player_stats = PlayerStats(player)

for player in team2_players:
    player_stats = PlayerStats(player)

events = Events()
current_bowler = events.get_bowler(team1_players if team_bowling == team1 else team2_players)
current_batsman = events.get_batsman(team1_players if team_batting == team1 else team2_players)
current_batsman2 = events.get_batsman(team1_players if team_batting == team1 else team2_players)