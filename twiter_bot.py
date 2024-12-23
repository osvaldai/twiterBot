import time

import requests
import schedule
from requests_oauthlib import OAuth1
import os
from datetime import datetime

# Учетные данные приложения из Twitter Developer Console
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Эндпоинт Twitter API v2 для отправки твитов
ENDPOINT_URL = 'https://api.twitter.com/2/tweets'


def get_today_post():
    # Get the current month name and day of the week
    current_month = datetime.now().strftime('%B')
    current_week_of_month = (datetime.now().day - 1) // 7 + 1  # Convert day to week of month (1-4)
    current_day_of_week = datetime.now().weekday() + 1  # .strftime('Day %A')  # Convert to format like "Day Monday"

    week_folder_name = f"Week {current_week_of_month}"
    file_name = f"Day {current_day_of_week}.txt"

    # Path to the file
    file_path = os.path.join("twitter_post", current_month,
                             week_folder_name, file_name)
    print(file_path)
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            post_content = file.read()
            return post_content
    else:
        return None


# Настройка аутентификации
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def posting():
    tweet_datas = {
        'text': get_today_post()
    }
    if tweet_datas is not None:
        # Отправка твита
        response = requests.post(ENDPOINT_URL, json=tweet_datas, auth=auth)

        # Проверка ответа
        if response.status_code == 201:
            print("Твит успешно отправлен!")
            print(response.json())
        else:
            print(f"Ошибка! Код: {response.status_code}")
            print(response.text)


# Настройка расписания
schedule.every().day.at("09:15").do(posting)

# Бесконечный цикл для выполнения запланированных задач
while True:
    schedule.run_pending()
    time.sleep(1)
