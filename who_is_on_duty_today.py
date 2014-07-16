#coding:utf-8
u"""
Скрипт для определения дежурного по pull-request
"""
import sys
import json
# Глобальная переменная, в которой лежит состояние программы
STATE = {
    'prev_index': None,
    'duty_list': [
        'Mark',
        'Antony',
        'Denoza',
        'Barbossa',
    ],
    'senior_list': None,
}
OFFICER_NOT_FOUND = 'Officer not found :('


def _save_state(state):
    """
    Записывает текущее состояние в виде json в файл
    state - dict хранящий состояние
    """
    _state = json.dumps(state)
    with open(".state.json", "w") as f:
        f.write(_state)


def _load_state(curr_state, state_store=None):
    u"""
    Читает состояние из файла
    current_state - dict текущее состояние
    state_store - путь к файлу, если не указан, по умолчанию
    ищет файл .state.json в директории скрипта
    """
    if not state_store:
        state_store = ".state.json"
    with open(state_store, "r") as f:
        state = f.read()
    try:
        state = json.loads(state)
    except ValueError:
        # initial step
        state = {}
    curr_state['prev_index'] = state.get('prev_index')


def _reset_state():
    _save_state({})


def get_next_officer(duty_officer_index):
    u"""
    Возвращает следующего дежурного после указанного duty_officer
    """
    if duty_officer_index is not None:
        officer = get_officer_by_index(duty_officer_index + 1)
        if officer != OFFICER_NOT_FOUND:
            return officer
    # return first active member
    return STATE['duty_list'][0]


def get_officer_by_index(index):
    if index is not None:
        try:
            return STATE['duty_list'][index]
        except IndexError:
            pass
    return OFFICER_NOT_FOUND


def main():
    #initial step
    _load_state(STATE)
    #working steps
    next_officer = get_next_officer(STATE['prev_index'])
    prev_officer = get_officer_by_index(STATE['prev_index'])

    print prev_officer, 'prev officer'
    print next_officer, 'next officer'

    #post run step
    STATE['prev_index'] = STATE['duty_list'].index(next_officer)
    _save_state(STATE)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--reset':
        _reset_state()
        print 'State droped!'
    main()