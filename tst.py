import csv
import datetime
import holidays
import argparse

def get_payday(year, month):
    """Leiab palgamaksmise kuupäeva ja meeldetuletuse kuupäeva antud aasta ja kuu kohta."""
    # Find 10nth day of given year and month.
    pay_date = datetime.date(year, month, 10)

    # if 10th workday is either weekend or national holiday, then payday is last workday.
    weekday_as_int = pay_date.weekday()
    if weekday_as_int == 5 or (pay_date in holidays.Estonia(year) and 6 > weekday_as_int > 0):
        pay_date -= datetime.timedelta(days=1)
    elif weekday_as_int == 6:
        pay_date -= datetime.timedelta(days=2)
    elif weekday_as_int == 0 and pay_date in holidays.Estonia(year):
        pay_date -= datetime.timedelta(days=3)

    # Find the reminder date - 3 workdays before pay date.
    reminder_date = pay_date - datetime.timedelta(days=3)
    if weekday_as_int == 5 or (reminder_date in holidays.Estonia(year) and 6 > weekday_as_int > 0) :
        reminder_date -= datetime.timedelta(days=1)
    elif weekday_as_int == 6:
        pay_date -= datetime.timedelta(days=2)
    elif weekday_as_int == 0 and reminder_date in holidays.Estonia(year):
        pay_date -= datetime.timedelta(days=3)
    return pay_date, reminder_date


def write_csv_file(year):
    """Kirjutab CSV-faili, mis sisaldab palgamaksmise kuupäeva ja meeldetuletuse kuupäeva iga kuu kohta antud aasta jaoks."""
    with open(f"{year}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Kirjutage päis
        writer.writerow(["Kuu", "Palgamaksmise kuupäev", "Meeldetuletuse kuupäev"])
        # Kirjutage andmed iga kuu kohta
        for month in range(1, 13):
            pay_date, reminder_date = get_payday(year, month)
            writer.writerow([datetime.date(year, month, 1).strftime("%B"), pay_date.strftime("%d.%m.%Y"), reminder_date.strftime("%d.%m.%Y")])


def main():
    # Looge argumentide parser, et lugeda sisse aastaarv
    parser = argparse.ArgumentParser(description="Genereerib Spin TEKi palgamaksmise kuupäevade tabeli antud aasta jaoks.")
    parser.add_argument("year", type=int, help="Aastaarv")

    args = parser.parse_args()

    # Kirjutage CSV-fail
    write_csv_file(args.year)


if __name__ == "__main__":
    main()
