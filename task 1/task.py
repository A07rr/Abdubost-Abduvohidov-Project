year = 365
week = 7
def calculation(days):
    count_years = days // year
    remainder_1 = days - count_years * year
    count_weeks = remainder_1 // week
    remainder_2 = days - count_weeks * week
    count_days = days - count_years * year - count_weeks * week
    result = f"Years: {count_years} -> Weeks: {count_weeks} -> Days: {count_days}"
    print(result)

calculation(days= int(input("Enter the number of days: ")))


