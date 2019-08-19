import pandas as pd


def output_csv(input_file, output_name):
    """

    :param input_file: the input csv.gz file
    :param output_name: the name of the output file
    :return: a normal csv file
    """
    df = pd.read_csv(input_file, compression='gzip', encoding='latin1')
    return df.to_csv(output_name)


# output_csv('Players_on_Court_Table.csv', "players_on_court_table_csv.csv")
# output_csv('SS_to_NBA_Player_Map.csv', "ss_to_nba_player_map.csv")
# output_csv('Team_Mapping_Table.csv', "team_mapping_table_csv.csv")
box_scores = pd.read_csv("Box_Scores.csv", compression='gzip', encoding='latin1')
hustle_stats = pd.read_csv("Hustle_Stats.csv", compression='gzip', encoding='latin1')

# Watch out! Game_ID might be upper case or lower case

# Get 16-17 hustle stats based on Game_ID


def get_specific_season_stats(input_file, column, regular_season):
    """
    :param input_file: target file
    :param column: which column to target (usually Game_id)
    :param regular_season: first three digits of Game_ID (regular season starts with 2, playoffs starts with 4,
    so we add 200 for playoffs, then multiply by 100000 as there are 5 digits after that
    :return: rows in specific season
    """
    return input_file[((input_file[column] < (regular_season + 1) * 100000) &
                       (input_file[column] > regular_season * 100000))
                      | ((input_file[column] < (regular_season + 200 + 1) * 100000) &
                         (input_file[column] > (regular_season + 200) * 100000))]


hustle_1617 = get_specific_season_stats(hustle_stats, 'Game_ID', 216)
box_scores_1617 = get_specific_season_stats(box_scores, 'Game_id', 216)

game_id_1617 = hustle_1617.Game_ID.unique()
hustle_1617_player = hustle_1617.Person_ID.unique()
hustle_1617_type = hustle_1617.Event_Msg_Type.unique()

hustle_per_game = []
for h in hustle_1617_type:
    hustle_per_game.append({h: 0})

# print(hustle_per_game)
result = {}
for i in game_id_1617:
    for j in hustle_1617_player:
        result[i] = {j: hustle_per_game}

        event_msg_type = hustle_1617.loc[
            (hustle_1617['Game_ID'] == i) & (hustle_1617['Person_ID'] == j), ['Event_Msg_Type']]
print(result)

# for m in range(len(hustle_per_game)):
#     for n in range(len(event_msg_type)):
#         if hustle_per_game[m].keys() == event_msg_type[n]:
#             hustle_per_game[m][hustle_per_game[m].keys()] += 1
        # print(result)







# print(hustle.iloc[:, 0:8].head())
# sample = pd.read_json("C:/Users/lilif/Desktop/NBA Hackathon/2019 Basketball Analytics/Basketball/Player Tracking"
#              "/SASGSW/2017051410_nba-gsw_TRACKING.jsonl", lines=True, orient='columns')

# print(list(sample.columns.values.tolist()))

