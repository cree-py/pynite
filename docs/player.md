### Player
| Name | Description | Type |
|------|-------------|------|
| player.get_id() | Get the player's Epic Games ID. | String |
| player.get_solos() | Get the player's solo stats. | [Solos](https://github.com/cree-py/pynite/blob/master/docs/solos.md) |
| player.get_duos() | Get the player's duo stats. | [Duos](https://github.com/cree-py/pynite/blob/master/docs/duos.md) |
| player.get_squads() | Get the player's squad stats. | [Squads](https://github.com/cree-py/pynite/blob/master/docs/squads.md) |
| player.get_lifetime_stats() | Get the player's lifetime stats. | [List\[{}, {}\]](https://github.com/cree-py/pynite/blob/master/docs/lifetime.md) |
| player.platform_id | The platform ID of the player. | Integer |
| player.platform_name | The platform name of the player. Can be 'pc', 'psn', or 'xbl'. | String |
| player.platform_name_long | The long platform name of the player. | String |
| player.epic_user_handle | The player's name. | String |
| player.recent_matches | Recent matches played. | List\[[MatchDict](https://github.com/cree-py/pynite/blob/master/docs/main.md#matchdict), [MatchDict](https://github.com/cree-py/pynite/blob/master/docs/main.md#matchdict)\] |
