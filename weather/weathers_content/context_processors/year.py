import datetime


def year(request):
    date_year = datetime.datetime.now()
    return {
        'year': date_year.year,
    }

def years_old(request):
    date_current = date_year = datetime.datetime.now()
    years_old = date_current.year - 1976
    return {'years_old': years_old,}
