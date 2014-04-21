months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day in range(1,31):
            return day

def valid_month(month):
    if month:
        month = month.lower()
        month = month[0].upper() + month[1:]
        if (month in months):
            return month
        
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year in range(1900,2014):
            return year