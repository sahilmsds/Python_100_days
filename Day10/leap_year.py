def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
                return True
            else:
                print(f"{year} is not a leap year.")
                return False
        else:
            print(f"{year} is a leap year.")
            return True
    else:
        print(f"{year} is not a leap year.")
        return False
    
year = int(input("Enter a year: "))

is_leap_year(year)