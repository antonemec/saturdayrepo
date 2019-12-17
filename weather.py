import configparser
import requests


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather(city, country, api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast?q={},{}&units=metric&appid={}".format(city, country, api_key)
    r = requests.get(url)
    return r.json()


def main():

    api_key = get_api_key()
    country = input('Enter country: ')
    city = input('Enter city:')
    weather = get_weather(city, country, api_key)

    for i in range(5):
        print('Погода в ',city,
            weather['list'][i]['dt_txt'], '\n---------------\n',
            'Температура: ', weather['list'][i]['main']['temp'], '\n',
            # weather['list'][i]['main']['feels_like'], '\n',
            'Минимальная температура: ', weather['list'][i]['main']['temp_min'], '\n',
            'Максимальная температура: ', weather['list'][i]['main']['temp_max'],  '\n',
            'Атмосферное давление на уровне моря по умолчанию, гПа: ', weather['list'][i]['main']['pressure'],  '\n',
            'Атмосферное давление на уровне моря, гПа: ', weather['list'][i]['main']['sea_level'], '\n',
            'Атмосферное давление на уровне земли, гПа: ', weather['list'][i]['main']['grnd_level'], '\n',
            'Влажность,%: ', weather['list'][i]['main']['humidity'],  '\n',
            #weather['list'][i]['main']['temp_kf'],
            '\n---------------\n',
            'Идентификатор погодного условия: ', weather['list'][i]['weather'][0]['id'],   '\n',
            'Группа погоды: ', weather['list'][i]['weather'][0]['main'],   '\n',
            'Погодные условия в группе: ', weather['list'][i]['weather'][0]['description'],  '\n',
            '\n---------------\n',
            weather['list'][i]['clouds'], '\n---------------\n',
            weather['list'][i]['wind'], '\n---------------\n',
            weather['list'][i]['sys'], '\n')


if __name__ == '__main__':
    main()
