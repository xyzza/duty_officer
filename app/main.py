# coding:utf-8


class Queue(object):
    u"""
    Queue object.
    Store queue state, current unit of queue.

    """
    # units must be iterable
    _units = None
    _current = 0

    def __init__(self, units=None):
        if self._units is None:
            self._units = units
        assert self._units is not None and len(self._units), \
            u"Queue can't be empty!"

    def current(self):
        return self._units[self._current]

    def append(self, unit):
        self._units.append(unit)
        return len(self._units)

    def insert(self, position, unit):
        self._units.insert(position, unit)
        return len(self._units)

    def next(self):
        self._current += 1
        if self._current == len(self._units):
            self._current = 0
        assert self._current < len(self._units)
        return self._current

    def __repr__(self):
        return "units is <{0}>, current is {1} ".format(
            repr(self._units),
            self._current)


def queue_test():
    """
    test case
    """
    queue = Queue(['a', 'b', 'c'])

    assert queue.current() == 'a'
    queue.next()
    assert queue.current() == 'b'
    queue.next()
    assert queue.current() == 'c'
    queue.next()
    assert queue.current() == 'a'

    queue.append('d')
    queue.next()
    queue.next()
    queue.next()

    assert queue.current() == 'd'
    queue.insert(1, 'q')

    queue.next()
    queue.next()
    queue.next()
    assert queue.current() == 'q'

    try:
        Queue([])
    except AssertionError, e:
        assert e.message == u"Queue can't be empty!"


if __name__ == "__main__":
    queue_test()