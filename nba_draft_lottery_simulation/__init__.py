import pandas as pd
import random

# function for nba lottery odds
def nba_draft_lottery_simulation(list_teams, list_probability, n_simulations=10):
    # multiply each by 1000
    count_list = [int(x*1000) for x in list_probability]
    
    # create empty pandas df to append each prediction
    empty_df = pd.DataFrame({'Team': list_teams})
    for x in range(n_simulations):
        # put the teams in a list n times
        list_of_teams = []
        for i in range(len(count_list)):
            teams = [list_teams[i]] * count_list[i]
            list_of_teams.extend(teams)
        # randomly select teams from list_of_teams
        draft_order_list = []
        for i in range(len(list_teams)):
            # randomly shuffle the list of teams
            random.shuffle(list_of_teams)
            # get random number
            random_number = random.randint(0, len(list_of_teams)-1)
            # select a random team
            random_team = list_of_teams[random_number]
            # append this team to draft_order_list
            draft_order_list.append(random_team)
            # remove all elements of random_team from list_of_teams
            list_of_teams = list(filter(lambda a: a != random_team, list_of_teams))
        # get the order of each team
        draft_selection_list = []
        for team in list_teams:
            order_of_selection = draft_order_list.index(team) + 1
            draft_selection_list.append(order_of_selection)
        # append to empty_df
        empty_df['Order_{}'.format(x+1)] = draft_selection_list
    
    # calculate the mean across columns
    empty_df['mean_draft_position'] = empty_df.mean(axis=1)
    # sort ascending
    empty_df_sorted = empty_df.sort_values(by=['mean_draft_position'], ascending=True)
    
    # print the draft order
    draft_order_df = pd.DataFrame({'Draft Order': [x+1 for x in range(len(list_teams))],
                                   'Team': empty_df_sorted['Team']})
    return draft_order_df
