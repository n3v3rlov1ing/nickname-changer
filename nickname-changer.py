from telethon.sync import TelegramClient
from telethon import functions, types

# Enter data from my.telegram.org
api_id = 14267457
api_hash = 'ff498b9a4d8e4ef040a975fc67b14af3'
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