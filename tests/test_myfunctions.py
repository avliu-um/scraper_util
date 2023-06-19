# TODO

from mypythonlib import myfunctions

def test_format_str(s):
    assert myfunctions.format_str('\n\n\r\rhello world||\r\r') == 'hello world')
