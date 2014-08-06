from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

cover = """def cover(func, data):
    cdata = set(tuple(d) for d in data)
    res = func(cdata)
    if not isinstance(res, (tuple, list)):
        raise TypeError("Must be a list or a tuple.")
    return res, str(res)
"""


def checker(data, user_data):
    user_result, str_result = user_data
    for t in user_result:
        if not isinstance(t, (tuple, list)) or len(t) != 2 or not isinstance(t[0], int) or not isinstance(t[1], int):
            return False, (False, "You should return a list/tuple of lists/tuples with two integers in each.")
    if not data:
        if user_result:
            return False, (True, "How did you draw this?")
        else:
            return True, (True, "Great")
    if len(user_result) < 2:
        return False, (False, "Only one point in your result.")
    data = list(data)
    for i in range(len(user_result) - 1):
        f, s = user_result[i], user_result[i + 1]
        if tuple(f + s) in data:
            data.remove(tuple(f + s))
        elif tuple(s + f) in data:
            data.remove(tuple(s + f))
        else:
            return False, (True, "The wrong segment {}.".format(f + s))
    if data:
        return False, (True, "You forgot about {}.".format(data[0]))
    return True, (True, "Great")


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,  # or None
            'python-3': cover
        },
        checker=checker,
        function_name="draw",

    ).on_ready)
