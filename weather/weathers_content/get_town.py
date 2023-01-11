import os

from dadata import Dadata
from dotenv import load_dotenv

load_dotenv()

def get_town(ip_user):
    if os.path.exists('./file_data_ip.txt'):
        file = open('./file_data_ip.txt', 'r')
        while True:
            ip = file.readline().rstrip().split(' ')
            if ip == ['']:
                break
            if ip[0] == ip_user:
                user_town = ip[1]
                file.close()
                return ip[1]
        file.close()
    token = os.getenv('token_town')
    dadata = Dadata(token)
    result = dadata.iplocate(ip_user)
    if result is None:
        return 'Москва'
    user_town = result['data']['city']
    if user_town is None:
        return 'Москва'
    file = open('./file_data_ip.txt', 'a')
    file.write(ip_user + ' ' + user_town + '\n')
    file.close()
    return user_town
