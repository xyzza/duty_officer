#coding:utf-8
u"""
Скрипт для определения дежурного по pull-request
"""
import sys
import json
from command_center import CommandCenter

OFFICERS_JSON = '.officers.json'
STATE_JSON = '.state.json'


def _save_state(state, destination):
    """
    Записывает текущее состояние в виде json в файл
    state - dict хранящий состояние
    """
    _state = json.dumps(state)
    with open(destination, "w") as f:
        f.write(_state)


def _load_state(state_store):
    # TODO: docstring
    with open(state_store, "r") as f:
        state = f.read()
    try:
        state = json.loads(state)
    except ValueError:
        # initial step with empthy file
        # FIXME refactor this
        state = {}
    return state


def _reset_state():
    _save_state({}, STATE_JSON)


def send_mail(to, d1, d2):
    # TODO: send mail
    print "Hello %s! Today on duty is %s and %s" % (to, d1, d2)


def main():
    #initial step
    officers = _load_state(OFFICERS_JSON)
    _prev_state = _load_state(STATE_JSON)

    # TODO: Refactor
    dev_args = officers['dev_list'], _prev_state.get('dev')
    senior_args = officers['senior_list'], _prev_state.get('senior')
    dev_cc = CommandCenter(*dev_args)
    senior_cc = CommandCenter(*senior_args)
    duty_dev = dev_cc.get_next_duty_index(dev_args[1])
    duty_senior = senior_cc.get_next_duty_index(senior_args[1])
    # save new duty state for both dev and senior lists
    _prev_state.update({'dev': duty_dev, 'senior': duty_senior})
    _save_state(_prev_state, STATE_JSON)

    # all developers in lists
    all_officers = reduce(lambda x, y: x+y, officers.values())

    for dev in all_officers:
        d1 = dev_cc.get_individual_assigment(dev, duty_dev)
        d2 = senior_cc.get_individual_assigment(dev, duty_senior)
        send_mail(dev, d1, d2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and '--reset' in sys.argv:
        _reset_state()
        print 'State droped!'
    main()