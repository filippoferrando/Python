from datetime import date
f_date = date(2020, 3, 19)
l_date = date(2020, 12, 22)
delta = l_date - f_date
print(delta.days)