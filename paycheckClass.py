"""
Author: B10 Devs
Description:
    This class is set up to take in the variables associated with a
    standard paycheck and make those into an instance of the class
    'Paycheck'.  The class also has a repr for debug and output.
"""


class PayCheck(object):

    def __init__(self, date, gross, our_cut, workers_comp, misc, total, notes):
        self.date = date
        self.gross = gross
        self.our_cut = our_cut
        self.workers_comp = workers_comp
        self.misc = misc
        self.total = total
        # self.hometime = hometime
        self.notes = notes
        # self.id = id

    # repr for debug and conformation.
    @property
    def __repr__(self):
        return "Date {} : Gross ${} Our Cut ${} WA ${} Misc ${} Total ${} Notes : {}".format(
            self.date,
            self.gross,
            self.our_cut,
            self.workers_comp,
            self.misc,
            self.total,
            self.notes)














