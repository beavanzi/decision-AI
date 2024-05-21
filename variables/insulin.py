class Insulin:
    groups: dict

    def __init__(self, dset, groups):
        self.groups = groups
        self.dset = dset

    def calc_prob_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            condition_to_zero = value[0] == 0
            if condition_to_zero:
                condition = (dset.has_diab()) & (dset.insulin >= value[0]) & (dset.insulin <= value[1])
            else:
                condition = (dset.has_diab()) & (dset.insulin > value[0]) & (dset.insulin <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs