# coding:utf-8


class CommandCenter(object):
    u"""
    This class take care about rotating list of officers,
    and assigning duty officer
    """
    _OFFICER_NOT_FOUND = 'Officer not found :('
    _mail_map = None

    def __init__(self, officer_list, last_on_duty):
        u"""
        :param officer_list: list of officers emails
        :param last_on_duty: index of last duty officer
        """
        self.officer_list = officer_list
        self.last_on_duty = last_on_duty
        # generate {'username': 'user_email'} map
        self._mail_map = dict(map(lambda m: (m.split('@')[0], m),
                                  self.officer_list))

    def get_next_on_duty(self, officer_index):
        u"""
        Return next duty officer
        :param officer_index: int or None index of officer
        :return: mail of next duty officer
        """
        if officer_index is not None:
            # WOW here is the bug!
            officer = officer_index + 1
            if officer != self._OFFICER_NOT_FOUND:
                return officer
        # return index of first active member
        return 0

    def get_officer_by_index(self, officer_index):
        """
        :param officer_index: int or None index of officer
        :return: mail of current oficer
        """
        if officer_index is not None:
            try:
                return self.officer_list[officer_index]
            except IndexError:
                pass
        return self._OFFICER_NOT_FOUND

    def change_myself(self, message_for, duty_officer):
        if message_for == duty_officer:
            # probably we need to take next for him
            duty_officer = self.get_next_on_duty(message_for)
        return duty_officer