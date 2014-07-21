# coding:utf-8


class CommandCenter(object):
    u"""
    This class take care about rotating list of officers,
    and assigning duty officer
    """

    def __init__(self, officer_list, last_on_duty):
        u"""
        :param officer_list: list of officers emails
        :param last_on_duty: index of last duty officer
        """
        self.officer_list = officer_list
        self.last_on_duty = last_on_duty

    def get_next_duty_index(self, officer_index):
        u"""
        Return next duty officer index
        :param officer_index: int or None index of officer
        :return: mail of next duty officer
        """
        if (officer_index is not None) and (
                len(self.officer_list) > officer_index + 1):
            return officer_index + 1
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
        #FIXME: What I should to return?
        return None

    def get_individual_assigment(self, message_for, duty_officer):
        """
        TODO doc
        :param message_for:
        :param duty_officer:
        :return:
        """
        if message_for == self.get_officer_by_index(duty_officer):
            # probably we need to take next for him
            duty_officer = self.get_next_duty_index(duty_officer)

        return self.get_officer_by_index(duty_officer)