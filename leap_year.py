def isLeapYear(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0:
        print("It is a leap year!")
        return True

    elif year % 400 == 0:
        print("Would you look at that, it happens to be a leap year!")
        return True

    print("NOT A LEAP YEAR AHHHHHH")
    return False
