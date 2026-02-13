
class Fruit:
    def __init__(self,name, fun_fact):
        self.name = name
        self.fun_fact = fun_fact

    def to_dict(self):
        return {'name':self.name,
                'fun_fact':self.fun_fact}
