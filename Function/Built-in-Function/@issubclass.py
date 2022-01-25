# issubclass(object, subclass)

from datetime import date


class now:
    year = int(date.today().strftime('%y'))


class me(now):
    name = 'David'
    bornYear = 1
    age = now.year - bornYear


print(me.age)
# out: 21

print(issubclass(now, me))
# out: False

print(issubclass(me, now))
# out: True
