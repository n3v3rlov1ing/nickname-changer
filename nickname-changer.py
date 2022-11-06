from telethon.sync import TelegramClient
from telethon import functions, types

# Enter data from my.telegram.org
api_id = 0
api_hash = ''
client = TelegramClient('anon', api_id, api_hash)

first_name = input('Enter first name: ')
last_name = input('Enter last name: ')

while True:
    change_status = input()
    if change_status == '/afk':
        with TelegramClient('anon', api_id, api_hash) as client:
            result = client(functions.account.UpdateProfileRequest(
                first_name=first_name,
                last_name=last_name
            ))
        print('[+] Статус успешно изменен!')
        continue
    else:
        continue
