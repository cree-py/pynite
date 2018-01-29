class BaseError(Exception):
    '''The base class for all errors.'''

    def __init__(self):
        pass


class NotResponding(BaseError):
    '''Raised when the Fortnite API is down.'''

    def __init__(self):
        self.code = 504
        self.error = 'API request timed out, please be patient.'
        super().__init__(self.error)


class Unauthorized(BaseError):
    '''Raised when an invalid or blocked API key is passed'''

    def __init__(self):
        self.code = 401
        self.error = 'Invalid API key.'
        super().__init__(self.error)


class NotFound(BaseError):
    '''Raised when an invalid platform/name combo has been passed'''

    def __init__(self):
        self.code = 404
        self.error = 'No profile with this platform/name combination has been found.'
        super().__init__(self.error)


class NoGames(BaseError):
    '''Raised when a player has not played a certain game mode'''

    def __init__(self, mode):
        self.code = 404
        self.error = f'This player has not played the {mode} gamemode yet.'
        super().__init__(self.error)


class NoKeyError(BaseError):
    '''Raised when normal info about something is missing. Should never happen.'''

    def __init__(self, mode):
        self.code = 404
        self.error = 'A wrapper-breaking error has just occured. Please contact us.'
        super().__init__(self.error)
