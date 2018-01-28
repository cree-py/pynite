### Client
| Name | Description | Type |
|------|-------------|------|
| client.get_id(platform, epic_username) | Get player ID. | String |
| client.get_player(platform, epic_username) | Get player statstics. | [Player](https://github.com/cree-py/pynite/blob/master/docs/player.md) |
| client.get_solos(platform, epic_username) | Get statistics for a player's solo games. | [Solos](https://github.com/cree-py/pynite/blob/master/docs/solos.md) |
| client.get_duos(platform, epic_username) | Get statistics for a player's duo games. | [Duos](https://github.com/cree-py/pynite/blob/master/docs/duos.md) |
| client.get_squads(platform, epic_username) | Get statistics for a player's squad games. | [Squads](https://github.com/cree-py/pynite/blob/master/docs/squads.md) |
| client.get_lifetime_stats(platform, epic_username) | Get total lifetime statistics for a player. | [List\[{}, {}\]](https://github.com/cree-py/pynite/blob/master/docs/lifetime.md) |
