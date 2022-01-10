# issubclass(object, subclass)

from datetime import date


class now:
    year = int(date.today().strftime('%y'))


class me(now):
    name = 'David'
    bornYear = 1
    age = now.year - bornYear


print(me.age)
# output: 21

print(issubclass(now, me))
# output: False

print(issubclass(me, now))
# output: True
