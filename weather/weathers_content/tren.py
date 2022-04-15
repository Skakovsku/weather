forecast = {'2022-04-16 12:00:00': {'description': 'небольшой снег',
                                    'sign': 'http://openweathermap.org/img/wn/13d@2x.png',
                                    'temp': -7},
            '2022-04-17 12:00:00': {'description': 'пасмурно',
                                    'sign': 'http://openweathermap.org/img/wn/04d@2x.png',
                                    'temp': -7},
            '2022-04-18 12:00:00': {'description': 'небольшой снег',
                                    'sign': 'http://openweathermap.org/img/wn/13d@2x.png',
                                    'temp': 0},
            '2022-04-19 12:00:00': {'description': 'небольшой снег',
                                    'sign': 'http://openweathermap.org/img/wn/13d@2x.png',
                                    'temp': 0},
            '2022-04-20 12:00:00': {'description': 'пасмурно',
                                    'sign': 'http://openweathermap.org/img/wn/04d@2x.png',
                                    'temp': -10}}

def func(a, *kwargs):
    print(a, kwargs)

x = 1
y = 9
z = 'chk'
func(x, y, z)
