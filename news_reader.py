import time
import requests
from win32com.client import Dispatch

my_url = "https://newsapi.org/v2/top-headlines?country=us"
my_params = {
    'pageSize': 20,
    'totalResults': 10,
    'category': 'technology',
    'apiKey': '942a1011ccfd4be5a5a6f46f47cf67bc'
    # 'url': 'https://www.theverge.com/'
}
my_news = requests.get(my_url, params=my_params).json()


def speak(news):
    read = Dispatch('SAPI.SpVoice')
    read.Speak(news)


speak('Hey there! Let\'s go through some of the great headlines today')
num = 0
for i in my_news['articles']:
    if num < 10:
        speak('From the source {0}'.format(i['title'].split('-')[1]))
        speak('The news is... {0}'.format(i['title'].split('-')[0]))
        time.sleep(1)
        num += 1
    else:
        speak("That's it for Today! See you later with some more interesting things")
        break