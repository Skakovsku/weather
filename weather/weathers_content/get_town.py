import os
from dadata import Dadata
from dotenv import load_dotenv

load_dotenv()

def get_town(ip_user):
    token = os.getenv('token_town')
    dadata = Dadata(token)
    result = dadata.iplocate(ip_user)
    if result is None:
        return 'Москва'
    user_toun = result.get('value').split(' ')[1]
    return user_toun
