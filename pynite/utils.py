import re


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def _to_snake_case(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def _to_camel_case(snake):
    parts = snake.split('_')
    return parts[0] + "".join(x.title() for x in parts[1:])


class API:
    BASE = 'http://api.fortnitetracker.com/v1'
    PLAYER = BASE + '/profile'
