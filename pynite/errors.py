'''
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
'''


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
