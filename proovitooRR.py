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

    # Find the reminder date = 3 workdays before pay date.
    reminder_date = pay_date - datetime.timedelta(days=1)
    # Counter for work days.
    counter = 2
    while counter != 0:
        # Subtract 1 day from remainder date.
        reminder_date -= datetime.timedelta(days=1)
        # if it is weekday and not holiday, decrement counter by 1
        if reminder_date.weekday() < 5 and reminder_date not in holidays.Estonia(year):
            counter -= 1
        # Next day date
        next_day_date = reminder_date - datetime.timedelta(days=1)
        # Check if counter is 0, pay date is Monday and so that next day will not be either saturday, sunday or holiday.
        if counter == 0 and pay_date.weekday() == 0 and next_day_date.weekday() < 5 \
                and next_day_date not in holidays.Estonia(year):
            reminder_date -= datetime.timedelta(days=1)
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
            writer.writerow([datetime.date(year, month, 1).strftime("%B"), pay_date.strftime("%d.%m.%Y"),
                             reminder_date.strftime("%d.%m.%Y")])


def main():
    # Create argument parser.
    parser = argparse.ArgumentParser(description="Generate payday dates for Spintek.")
    parser.add_argument("year", type=int)

    args = parser.parse_args()

    # Write to csv file.
    write_csv_file(args.year)


if __name__ == "__main__":
    main()
