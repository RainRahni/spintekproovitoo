import csv
from datetime import date, timedelta


def payday(year):
    """Return dates in a given year when is payday."""
    national_holidays_dict = {}
    january_dict = {}
    february_dict = {}
    march_dict = {}
    april_dict = {}
    may_dict = {}
    june_dict = {}
    july_dict = {}
    august_dict = {}
    september_dict = {}
    october_dict = {}
    november_dict = {}
    december_dict = {}
    year = 2023
    start_date = date(year, 1, 1)  # January 1st of the year
    end_date = date(year, 12, 31)  # December 31st of the year
    for delta in range((end_date - start_date).days + 1):
        d = start_date + timedelta(days=delta)
        if d.month == 0o1:
            january_dict[d.strftime('%d.%m.%Y')] = d.strftime('%A')
        elif d.month == 0o2:
            february_dict[d.strftime('%d.%m.%Y')] = d.strftime('%A')

    rows = []
    for month in range(1, 13):
        payday_date = payday(year=2023)
        rows.append([january_dict.keys(), payday_date])

    with open('2023.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
