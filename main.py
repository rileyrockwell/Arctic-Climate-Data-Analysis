class Nonsense(object):
    
    def __init__(self, dm1, dm2, dm3):
        self.one = dm1
        self.two = dm2
        self.three = dm3


instance = Nonsense('some', 'bullshit', 'somewhere')

print(instance.one)
print(instance.two)
print(instance.three)