### Lifetime Stats

List\[{'key': 'statistic', 'value': 'value'}, {'key': 'statistic', 'value': 'value'}\]

All indexes return [LifetimeDict](https://github.com/cree-py/pynite/blob/master/docs/main.md#lifetimedict)

Index | Key | Value |
|-----|------|------|
| 0 | 'Top 3' | str |
| 1 | 'Top 5s' | str(int) |
| 2 | 'Top 3s' | str(int) |
| 3 | 'Top 6s' | str(int) |
| 4 | 'Top 12s' | str(int) |
| 5 | 'Top 25s' | str(int) |
| 6 | 'Score' | str(int) |
| 7 | 'Matches Played' | str(int) |
| 8 | 'Wins' | str(int) |
| 9 | 'Win%' | str(int) |
| 10 | 'Kills' | str(int) |
| 11 | 'K/d' | str(float) |
| 12 | 'Kills Per Min' | str(float) |
| 13 | 'Time Played' | str(0d 0h 0m 0s) |
| 14 | 'Avg Survival Time' | str(0d 0h 0m 0s) |

#### Examples

```
client = pynite.Client('token')
player = client.get_player('pc', 'muselk')
lifetime = await player.get_lifetime_stats()

print(lifetime[10].key, lifetime[10].value)
# Prints Kills 1923 to the console. 1923 is the number of kills the person made. This varies for each person.
```
