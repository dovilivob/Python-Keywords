# issubclass(object, subclass)

from datetime import date


class now:
    year = int(date.today().strftime('%y'))


class me(now):
    name = 'David'
    bornYear = 1
    age = now.year - bornYear


print(me.age)
# Output: 21

print(issubclass(now, me))
# Output: False

print(issubclass(me, now))
# Output: True
