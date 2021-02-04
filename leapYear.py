
def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    return False

year = input("Input the year: ")
y = int(year)
if is_leap_year(y):
    print("Yes")
else:
    print("No")
