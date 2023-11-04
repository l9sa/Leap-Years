def is_leap_year(year):
    if year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False
    else:
        return True

def print_next_leap_years(current_year, nof_leap_years):
    nof_leap_years_found = 0

    while nof_leap_years_found < nof_leap_years:
        if is_leap_year(current_year):
            nof_leap_years_found += 1
            print(current_year)

        current_year += 1

def print_next_leap_years_with_recursion(current_year, nof_leap_years, nof_leap_years_found=0):
    if is_leap_year(current_year):
        nof_leap_years_found += 1
        print(current_year)

    if nof_leap_years_found < nof_leap_years:
        print_next_leap_years_with_recursion(current_year + 1, nof_leap_years, nof_leap_years_found)

current_year = int(input("Enter the current year: "))
nof_leap_years = int(input("Enter the number of leap years to print: "))

print_next_leap_years(current_year, nof_leap_years)

print_next_leap_years_with_recursion(current_year, nof_leap_years)