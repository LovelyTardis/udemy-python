"""
    Module for everything that is about time and dates for the application.
"""
import datetime


def get_today():
    """ Builds the weekday, day, month and year for today

    :return: tuple of weekday, day, month, year
    """
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    months = [
        "january", "february", "march", "april",
        "may", "june", "july", "august",
        "september", "october", "november", "december"
    ]
    today = datetime.date.today()
    weekday = days[today.weekday()]
    day = today.day
    month = months[today.month - 1]
    year = today.year
    return weekday, day, month, year


def get_hour() -> []:
    """ Gets the actual time

    :return: time by hour and minute
    """
    time = datetime.datetime.now()
    return time.hour, time.minute


def daytime_salute() -> str:
    """ Builds and returns a string depending on the actual hour of the day

    :return: string
    """
    hour, _ = get_hour()
    if 6 < hour < 13:
        return "Good morning"
    if 13 < hour < 21:
        return "Good evening"
    return "Good night"
