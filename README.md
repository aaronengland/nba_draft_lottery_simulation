# nba_draft_lottery_simulation

The `nba_draft_lottery_simulation` function takes a list of teams, another list of their corresponding probability of landing the first pick, and the number of simulations and returns a data frame of the predicted draft order.

To install, use: `pip install git+https://github.com/aaronengland/nba_draft_lottery_simulation.git`

Example:

```
from nba_draft_lottery_simulation import nba_draft_lottery_simulation

# get teams
teams_list = ['New York Knicks','Cleveland Cavaliers','Phoenix Suns',
              'Chicago Bulls','Atlanta Hawks','Washington Wizards',
              'New Orleans Pelicans','Memphis Grizzlies','Dallas Mavericks',
              'Minnesota Timberwolves','Los Angeles Lakers',
              'Charlotte Hornets','Miami Heat','Sacramento Kings']

# get the probabilities
probability_list = [0.14,0.14,0.14,0.125,0.105,0.09,0.06,0.06,0.06,0.03,0.02,
                    0.01,0.01,0.01]

# generate predictions
predicted_draft_order = nba_draft_lottery_simulation(list_teams=teams_list, 
                                                     list_probability=probability_list,
                                                     n_simulations=10)
```
