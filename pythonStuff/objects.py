
didi = {'name': 'Didi',
        'age': 17,
        'college': 'UT Austin',
        'fave_color': 'Blue',
        }

class Person(object):
    def __init__(self, name, age, fave_color, college=None):
        self.name=name
        self.age=age
        self.college=college
        self.fave_color=fave_color
        self.hungry=True
        self.tired=True

    def eat(self, food):
        print('YUM I am eating {food}'.format(food=food))
        self.hungry=False

    def __str__(self):
        didi_string = 'Name: {n}, Age{a}, College: {c}, Favorite color: {f}'.format(n=name, a=age, c=college, f=fave_color)
        return didi_string

    def nap(self, time):
        print('You slept for {t} minutes'.format(t=time))
        self.tired=false

didi = Person(name='Didi', age=17, college='UT Austin', fave_color='Blue')
max = Person(name='Max', age = 90, fave_color='Pink')

print(didi)
print(max.name)
print('Didi is hungry {h} '.format(h=didi.hungry))
didi.eat('banana')
didi.sleep(30)
