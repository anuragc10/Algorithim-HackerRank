year=int(input())

yes_leap=0
no_leap=0
p=0
if (year==1918):
    print("26.09.1918")

elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
    print("12.09.",end='')
    print(year)
else:
    print("13.09.",end='')
    print(year)
