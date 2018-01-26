from box import Box, BoxList
from .utils import _to_snake_case, API


class BaseAttrDict:
    '''
    This allows us to retrieve data
    from the API in dot-notation.
    This shouldn't really be used by the user.

    .. _python-box: https://github.com/cdgriffith/Box

    Model:

        sample_data = {
            "stats": {
                "kills": 3849
                "matches": {
                    "solo": 293
                    "duos": 193
                    "squads": 212
                }
            }
        }

        x = sample_data['stats']['kills']  # returns 3849
        # same as
        x = sample_data.stats.kills  # returns 3849

    This functionality allows this library to present API
    data in a clean dynamic way.

    Attributes
    ----------
    raw_data: dict
        The raw data in the form of a dictionary being used
    '''

    def __init__(self, client, data):
        self.client = client
        self.from_data(data)

    def from_data(self, data):
        self.raw_data = data
        if isinstance(data, list):
            self._boxed_data = BoxList(
                data, camel_killer_box=not self.client.camel_case
            )
        else:
            self._boxed_data = Box(
                data, camel_killer_box=not self.client.camel_case
            )
        return self
