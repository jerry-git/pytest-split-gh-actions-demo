import time


def do_something1():
    _do_work_light()


def do_something2():
    _do_work_light()


def do_something3():
    _do_work_light()


def do_something4():
    _do_work_light()


def do_something5():
    _do_work_light()


def do_something6():
    _do_work_light()


def do_something7():
    _do_work_heavy()


def do_something8():
    _do_work_heavy()


def do_something9():
    _do_work_heavy()


def do_something10():
    _do_work_heavy()


def _do_work_light():
    time.sleep(10)


def _do_work_heavy():
    time.sleep(60)
