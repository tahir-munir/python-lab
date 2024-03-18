class ModelBaseAgent():
    def __init__(self,a, b):
        self.model = ("loc_a" : a , "Loc_b" : b)
    def DoAction(self,location,status):
        self.model[location] = status
        print(self.model)
        if self.model["Loc_a"] = self.model["Loc_a"] == 'clean'
            return 'NoOp'
        elif status == 'dirty':
            return 'suck'
        elif location == 'Loca_a'