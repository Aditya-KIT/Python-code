def is_leap(year):
    year=year%400
    if(year%100!=0):
        year=year%4
    if(year==0):
        return (bool(1))
    else:
        return (bool(0))

year = int(input())
print(is_leap(year))