class BMI:

    groups: dict

    def __init__(self, dset, groups):
        self.groups = groups
        self.dset = dset

    def calc_prob_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            if(value[0] == 0):
                condition = (dset.has_diab()) & (dset.bmi >= value[0]) & (dset.bmi <= value[1])
            else:
                condition = (dset.has_diab()) & (dset.bmi > value[0]) & (dset.bmi <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs
    
    def calc_prob_not_diab(self):
        probs = []
        dset = self.dset
        for key, value in self.groups.items():
            if(value[0] == 0):
                condition = (dset.has_not_diab()) & (dset.bmi >= value[0]) & (dset.bmi <= value[1])
            else:
                condition = (dset.has_not_diab()) & (dset.bmi > value[0]) & (dset.bmi <= value[1])
            prob = dset.loc(condition).shape[0]/dset.qtt_total
            probs.append(prob)
        return probs