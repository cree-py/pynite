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
| playlist | The mode that was played. `p2` = solo, `p10` = duo, `p9` = squad. | String |
| kills | The number of kills in the match. | Integer |
| minutesPlayed | How long the match took. | Integer |
