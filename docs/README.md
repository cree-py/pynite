# Welcome to the pynite Docs!

### Introduction
Welcome to PyNite™! PyNite is an asynchronous Python wrapper for the [Fortnite Tracker Network](https://fortnitetracker.com). The wrapper is currently in progress, meaning we are **currently** developing more wrapper classes, but for now, all the data from FTN should be accessible to you, albeit in a more difficult manner.

### Installation
PyNite is available through `pip`, but not PyPI as of currently. We will publish this module to PyPI once it becomes more practical.
#### To install:
```pip install git+https://github.com/cree-py/pynite```

This should install PyNite along with its dependencies. If for some reason the dependencies are not installed, PyNite will not work correctly. You can manually install the dependencies through
```pip install aiohttp```
and
```pip install python-box```

You can update PyNite by running ```pip install -U git+https://github.com/cree-py/pynite```. The current stable version is `1.1.2`.

PyNite requires Python 3.6 or later versions.

### Legal
MIT License

Copyright (c) 2018 RBC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Reference

## The following section contains reference material.

### Classes
- Client extends Object
- Player extends Box

### Generic Objects
| Name | Description |
|------|-------------|
| ValueDict | Dictionary for data values. |
| MatchDict | Dictionary for match information. |

#### ValueDict
| Name | Description | Type |
|------|-------------|------|
| label | The name of the Dictionary. | String |
| field | The field of the Dictionary. | String |
| category | The category of the Dictionary. | String |
| value_int* | The value of the Dictionary. | Int |
| value_dec* | The value of the Dictionary. | Float |
| value | The value of the Dictionary. | String |
| percentile* | The percentile of the value of the Dictionary. | Float |
| display_value | The Display value for the Dictionary. | String |

\*Only available in some ValueDicts. Use your brain to see what seems plausible.

#### MatchDict
| Name | Description | Type |
|------|-------------|------|
| id | ID of the match | Integer |
| accountId | Account ID of the player. | String |
| playlist | The mode that was played. "p2" = solo, "p10" = duo, "p9" = squad. | String |
| kills | The number of kills the player made in the match. | Integer |
| minutesPlayed | How long the match took. | Integer |

### Client
| Name | Description | Type |
|------|-------------|------|
| client.get_id(platform, epic_username) | Get player ID. | String |
| client.get_player(platform, epic_username) | Get player statstics. | Player |
| client.get_solos(platform, epic_username) | Get statistics for a player's solo games. | Solo |
| client.get_duos(platform, epic_username) | Get statistics for a player's duo games. | Duo |
| client.get_squads(platform, epic_username) | Get statistics for a player's squad games. | Squad |
| client.get_lifetime_stats(platform, epic_username) | Get total lifetime statistics for a player. | Dict |

### Player
| Name | Description | Type |
|------|-------------|------|
| player.get_id() | Get the player's Epic Games ID. | String |
| player.get_solos() | Get the player's solo stats. | Dict |
| player.get_duos() | Get the player's duo stats. | Dict |
| player.get_squads() | Get the player's squad stats. | Dict |
| player.get_lifetime_stats() | Get the player's lifetime stats. | Dict |
| player.platformId | The platform ID of the player. | Integer |
| player.platformName | The platform name of the player. Can be 'pc', 'psn', or 'xbl'. | String |
| player.platformNameLong | The long platform name of the player. | String |
| player.epicUserHandle | The player's name. | String |
| player.recentMatches | Recent matches played. | MatchDict List |

### Solo
All Types return a `ValueDict`
| Name | Description |
|------|-------------|
| solo.trn_rating | The Tracker Network Rating for the Player. |
| solo.score | The Score for the Player. | ValueDict |
| solo.top1 | The Victory Royales for the Player. |
| solo.top3 | The number of Top 3 wins for the Player. |
| solo.top5 | The number of Top 5 wins for the Player. |
| solo.top6 | The number of Top 6 wins for the Player. |
| solo.top10 | The number of Top 10 wins for the Player. |
| solo.top12 | The number of Top 12 wins for the Player. |
| solo.top25 | The number of Top 25 wins for the Player. |
| solo.kd | The Kill to Death ratio in solos. |
| solo.matches | The number of matches played. |
| solo.kills | The number of kills the Player has.
| solo.minutes_played | The number of minutes the Player has played.
| solo.kpm | The average number of kills per minute. |
| solo.kpg | The average number of kills per game. |
| solo.avg_time_played | The average amount of time for each match. |
| solo.score_per_match | The average score per match played |
| solo.score_per_min | The average score per minute played |

### Duo
| Name | Description | Type |
|------|-------------|------|
| duo.trn_rating | The Tracker Network Rating for the Player. | ValueDict |
| duo.score | The Score for the Player. | ValueDict |
| duo.top1 | The Victory Royales for the Player. | ValueDict |
| duo.top3 | The number of Top 3 wins for the Player. | ValueDict |
| duo.top5 | The number of Top 5 wins for the Player. | ValueDict |
| duo.top6 | The number of Top 6 wins for the Player. | ValueDict |
| duo.top10 | The number of Top 10 wins for the Player. | ValueDict |
| duo.top12 | The number of Top 12 wins for the Player. | ValueDict |
| duo.top25 | The number of Top 25 wins for the Player. | ValueDict |
| duo.kd | ??? | ValueDict |
| duo.matches | The number of matches played. | ValueDict |
| duo.kills | The number of kills the Player has. | ValueDict |
| duo.minutes_played | The number of minutes the Player has played. | ValueDict |
| duo.kpm | The average number of kills per minute. | ValueDict |
| duo.kpg | The average number of kills per game. | ValueDict |
| duo.avg_time_played | The average amount of time for each match. | ValueDict |
| duo.score_per_match | The average score per match played | ValueDict |
| duo.score_per_min | The average score per minute played | ValueDict |

### Squad
| Name | Description | Type |
|------|-------------|------|
| squad.trn_rating | The Tracker Network Rating for the Player. | ValueDict |
| squad.score | The Score for the Player. | ValueDict |
| squad.top1 | The Victory Royales for the Player. | ValueDict |
| squad.top3 | The number of Top 3 wins for the Player. | ValueDict |
| squad.top5 | The number of Top 5 wins for the Player. | ValueDict |
| squad.top6 | The number of Top 6 wins for the Player. | ValueDict |
| squad.top10 | The number of Top 10 wins for the Player. | ValueDict |
| squad.top12 | The number of Top 12 wins for the Player. | ValueDict |
| squad.top25 | The number of Top 25 wins for the Player. | ValueDict |
| squad.kd | ??? | ValueDict |
| squad.matches | The number of matches played. | ValueDict |
| squad.kills | The number of kills the Player has. | ValueDict |
| squad.minutes_played | The number of minutes the Player has played. | ValueDict |
| squad.kpm | The average number of kills per minute. | ValueDict |
| squad.kpg | The average number of kills per game. | ValueDict |
| squad.avg_time_played | The average amount of time for each match. | ValueDict |
| squad.score_per_match | The average score per match played | ValueDict |
| squad.score_per_min | The average score per minute played | ValueDict |

More coming soon™

### Help

If you need help with anything, feel free to join our discord server to contact us.
