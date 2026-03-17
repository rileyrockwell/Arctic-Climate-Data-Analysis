class Nonsense(object):
    
    def __init__(self, dm1, dm2, dm3, dm4):
        self.one = dm1
        self.two = dm2
        self.three = dm3
        self.four = dm4


instance = Nonsense('some', 'bullshit', 'happening', 'somewhere')

print(instance.one)
print(instance.two)
print(instance.three)
print(instance.four)