class ModelBaseAgent():
    def __init__(self,inti_a, inti_b):
        self.model = {"loc_a" : inti_a , "Loc_b" : inti_b}
    def DoAction(self,location,status):
        self.model[location] = status
        print(self.model)
        if self.model["Loc_a"] == self.model["Loc_a"] == 'clean'
            return 'NoOp'
        elif status == 'dirty':
            return 'suck'
        elif location == 'Loca_a':
            return 'right'
        else:
            return 'left'
        
a = ModelBaseAgent('dirty','dirty')
print(a.DoAction('Loc_a', 'dirty'))