from dadata import Dadata

def get_town(ip_user):
    token = "c50fb477485fea3f972c5a6a860f91793d13b045"
    dadata = Dadata(token)
    result = dadata.iplocate(ip_user)
    if result is None:
        return 'Воркута'
    user_toun = result.get('value').split(' ')[1]
    return user_toun
