# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:23:43 2016

@author: richard.vuong
"""

import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():

    header()

    postcode = input('What postcode do you want the weather for? ')

    html = get_html_from_web(postcode)
    report = get_weather_from_html(html)

    if float(report.temp) >= 20:
        print('Get out the ice creams! The temperature in {} is a scorching {} {} ({})'.format(
            report.loc,
            report.temp,
            report.scale,
            report.cond
            ))
    elif float(report.temp) <= 5:
        print('Put on your coat! The temperature in {} is a freezing {} {} ({})'.format(
            report.loc,
            report.temp,
            report.scale,
            report.cond
            ))
    else:
        print('The temperature in {} is {} {} ({})'.format(
            report.loc,
            report.temp,
            report.scale,
            report.cond
            ))
            
def header():
    print('---------------------------------')
    print('           WEATHER APP           ')
    print('---------------------------------')


def get_html_from_web(code):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(code)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report
    
    
def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()