from datetime import datetime
def get_days_from_today(date):
   
    ### Инструкция по обработке вводимых данных
    try:
        datetime_date= datetime.strptime(date, "%Y-%m-%d").date()
        date_today= datetime.now().date()
        number_day= date_today- datetime_date
        return number_day.days
    ### Проверка на неправильный ввод данных
    except ValueError:
        print("Please input correct date in format: Year-month-day")
        return
