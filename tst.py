import csv
import datetime
import holidays
import argparse


def get_payday(year, month):
    """Get pay date and reminder date for given month in given year."""
    # Find 10nth day of given year and month.
    pay_date = datetime.date(year, month, 10)

    # if 10th workday is either weekend or national holiday, then payday is last workday.
    while 7 > pay_date.weekday() > 4 or pay_date in holidays.Estonia(year):
        pay_date -= datetime.timedelta(days=1)
    """pay_date_weekday_as_int = pay_date.weekday()
    if pay_date_weekday_as_int == 5 or (pay_date in holidays.Estonia(year) and 6 > pay_date_weekday_as_int > 0):
        pay_date -= datetime.timedelta(days=1)
    elif pay_date_weekday_as_int == 6:
        pay_date -= datetime.timedelta(days=2)
    elif pay_date_weekday_as_int == 0 and pay_date in holidays.Estonia(year):
        pay_date -= datetime.timedelta(days=3)"""
    # Find the reminder date - 3 workdays before pay date.
    reminder_date = pay_date - datetime.timedelta(days=1)
    counter = 0
    #7 > reminder_date.weekday() > 4 or pay_date in holidays.Estonia(year)

    while counter != 4:
        if reminder_date.weekday() < 5 and reminder_date not in holidays.Estonia(year):
            counter += 1
        reminder_date -= datetime.timedelta(days=1)

    """if 3 >= pay_date.weekday() >= 0:
        reminder_date = pay_date - datetime.timedelta(days=6)
    elif (pay_date.weekday() - 4) == 0 and pay_date in holidays.Estonia(year):
        reminder_date = pay_date - datetime.timedelta(days=7)
    elif (pay_date.weekday() - 4) == 1 and pay_date in holidays.Estonia(year):
        reminder_date = pay_date - datetime.timedelta(days=5)
    else:
        reminder_date = pay_date - datetime.timedelta(days=4)"""
    return pay_date, reminder_date


def write_csv_file(year):
    """Write contents to csv file."""
    with open(f"{year}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write header.
        writer.writerow(["Month", "Pay Date", "Reminder Date"])
        # Get pay date and reminder date for each month and write it to file.
        for month in range(1, 13):
            pay_date, reminder_date = get_payday(year, month)
            writer.writerow([datetime.date(year, month, 1).strftime("%B"), pay_date.strftime("%d.%m.%Y"), reminder_date.strftime("%d.%m.%Y")])


def main():
    # Looge argumentide parser, et lugeda sisse aastaarv
    parser = argparse.ArgumentParser(description="Generate payday dates for Spintek.")
    parser.add_argument("year", type=int, help="Aastaarv")

    args = parser.parse_args()

    # Write to csv file.
    write_csv_file(args.year)


if __name__ == "__main__":
    print(get_payday(2023, 8))
    main()
