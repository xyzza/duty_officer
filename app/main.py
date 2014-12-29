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
        #TODO: maybe we should return a position number instead of value
        return self._units[self._current]

    def append(self, unit):
        self._units.append(unit)
        return len(self._units)

    def insert(self, position, unit):
        self._units.insert(position, unit)
        return len(self._units)

    def forward(self):
        self._current += 1
        if self._current == len(self._units):
            self._current = 0
        assert self._current < len(self._units)
        return self.current()

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
    assert queue.forward() == 'b'
    assert queue.forward() == 'c'

    assert queue.append('d') == 4
    assert queue.forward() == 'd'
    assert queue.forward() == 'a'

    # insertion doesn't change current index!
    assert queue.insert(1, 'q') == 5
    # check we still in position 0
    #TODO: maybe we should return a position number instead of value
    assert queue.current() == 'a'
    assert queue.forward() == 'q'

    try:
        Queue([])
    except AssertionError, e:
        assert e.message == u"Queue can't be empty!"





if __name__ == "__main__":
    queue_test()