import datetime


def year(request):
    date_year = datetime.datetime.now()
    return {
        'year': date_year.year,
    }
