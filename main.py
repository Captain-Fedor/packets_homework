import datetime
from applications.salary import salary_info
from applications.db.people import people_info
from durty_main import *
def currnet_date():
    date_now = datetime.date.today()
    date_now_str = date_now.strftime('%d-%b-%Y')
    return print(date_now_str)


if __name__ == '__main__':
    currnet_date()
    salary_info()
    people_info()
    junk()

