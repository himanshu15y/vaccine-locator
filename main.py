import requests
from time import sleep
token=<telegran-token>
user=<bot-user-name>
params=('chat_id',<chat-id>)
# f = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')

import requests

headers = {
    'authority': 'cdn-api.co-vin.in',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'origin': 'https://www.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cowin.gov.in/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'if-none-match': 'W/"c78f-IryKT8kLiWwLAjr9M/5zeIsK+oY"',
}

params = (
    ('district_id', '149'),
    ('date', '15-07-2021'),
)

# response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict', headers=headers, params=params)
from datetime import datetime
d = requests.post(url=f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1044584962&text=botrunning{datetime.now()}')
response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)
# for i in range(0,10):
while True:
    try:
        dt = datetime.now()
        if dt.minute==58 and dt.second in range(20,25):
            d = requests.post(url=f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1044584962&text=botrunning{datetime.now()}')
        for pincode in ('485001'):
            import json
            params = (('pincode', f'{pincode}'),('date', datetime.strftime(dt,"%d-%m-%Y")))
            response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)
            js=response.json()
#             print(js)
            len(js['centers'])
            for center in js['centers']:
                address=center['address']
                for session in center['sessions']:
                    available_capacity_dose1=session['available_capacity_dose1']
                    available_capacity=session['available_capacity']
                    min_age_limit=session['min_age_limit']
                    if(min_age_limit<45 and (available_capacity>0 or available_capacity_dose1>0)):
                        text=f'{min_age_limit} {address} {available_capacity}'
                        d = requests.post(url=f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={text}')
                        print(text)
        for district in ('149',):
#             print(district)
            import json
            params = (('district_id', f'{district}'),('date', datetime.strftime(dt,"%d-%m-%Y")))
            response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict', headers=headers, params=params)
            js=response.json()
#             print(js)
            len(js['centers'])
            for center in js['centers']:
                address=center['address']
                fee_type=center['fee_type']
                for session in center['sessions']:
                    available_capacity_dose1=session['available_capacity_dose1']
                    available_capacity=session['available_capacity']
                    min_age_limit=session['min_age_limit']
                    if(min_age_limit<45 and (available_capacity>0 or available_capacity_dose1>0)):
                        text=f'{min_age_limit} {address} {available_capacity} available_capacity_dose1={available_capacity_dose1} fee={fee_type}'
                        print(text)
                        d = requests.post(url=f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={text}')
    except:
        try:
            sleep(2)
            print(e.args)
            print("-------Sleeping-------")
            d = requests.post(url=f'https://api.telegram.org/bot{token}/sendMessage?chat_id={cahtid}&text=error')
        except:
            sleep(10)
            pass
