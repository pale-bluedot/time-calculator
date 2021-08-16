##################################################################################################
# File name: time_calculator.py
# Author: Johan Andrade
# Date created: 07 / 26 / 2021
# Date last modified  08 / 15 / 2021
# Description: The function should add the duration time to the start time and return the result.
# Refer to README.md for full description
##################################################################################################


def add_time(start, duration, day=""):

    hour, min = map(int, start[:-2].split(':'))  # removes AM/PM characters
    dhour, dmin = map(int, duration.split(':'))

    week = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }

    # hold this value before we modify it to 12-hour clock
    elapsedhour = dhour
    elapsedmin = dmin

    # modulo operate the hour by 12 to work with integers 1-12 on a 12-hour clock
    hour %= 12
    dhour %= 12

    if start[-2:] == 'PM':
        hour += 12

    duration = (dhour * 60) + dmin

    time = (hour * 60) + min + duration

    hour, min = divmod(time, 60)

    realhour = hour  # hold this value to determine how many hours we are into the day

    # if hour is greater than 24 we need the remainder to return 1-12 integers
    hour %= 24
    period = 'AM' if hour < 12 else 'PM'

    hour %= 12
    if hour == 0:
        hour = 12

    # iterate through week dictionary and find a match when starting day is entered
    for item in week:
        if day.capitalize() == week[item]:
            if ((elapsedhour < 24) and (realhour < 24) and (min < 10)):
                new_time = "{}:0{} {}, {}".format(hour, min, period,
                                                  day.capitalize())
            elif ((elapsedhour < 24) and (realhour < 24) and (min > 10)):
                new_time = "{}:{} {}, {}".format(hour, min, period,
                                                 day.capitalize())
            elif ((elapsedhour < 24) and (realhour > 24) and (min < 10)):
                new_time = "{}:0{} {}, {}".format(hour, min, period,
                                                  day.capitalize())
            elif ((elapsedhour < 24) and (realhour > 24) and (min > 10)):
                new_time = "{}:{} {}, {}".format(hour, min, period,
                                                 day.capitalize())
            elif ((elapsedhour == 24) and (elapsedmin == 0) and (min < 10)):
                item += 1
                if (item > 7):
                    item = 1
                    new_day = week[item]
                else:
                    new_day = week[item]
                new_time = "{}:0{} {}, {} (next day)".format(
                    hour, min, period, new_day.capitalize())
            elif ((elapsedhour == 24) and (elapsedmin == 0) and (min > 10)):
                item += 1
                if (item > 7):
                    item = 1
                    new_day = week[item]
                else:
                    new_day = week[item]
                new_time = "{}:{} {}, {} (next day)".format(
                    hour, min, period, new_day.capitalize())
            elif ((elapsedhour >= 24) and (elapsedmin > 0) and (min < 10)):
                elapsedtime = int((elapsedhour / 24) + 1)
                item = item + elapsedtime
                if (item <= 7):
                    item = item
                elif (item > 7):
                    item %= 7
                else:
                    None
                new_day = week[item]
                new_time = "{}:0{} {}, {} ({} days later)".format(
                    hour, min, period, new_day.capitalize(), elapsedtime)
            elif ((elapsedhour >= 24) and (elapsedmin > 0) and (min > 10)):
                elapsedtime = int((elapsedhour / 24) + 1)
                item = item + elapsedtime
                if (item <= 7):
                    item = item
                elif (item > 7):
                    item %= 7
                else:
                    None
                new_day = week[item]
                new_time = "{}:{} {}, {} ({} days later)".format(
                    hour, min, period, new_day.capitalize(), elapsedtime)
            else:
                None
        # conditions when no starting day is entered
        elif day == "":
            if ((elapsedhour < 24) and (realhour < 24) and (min < 10)):
                new_time = "{}:0{} {}".format(hour, min, period)
            elif ((elapsedhour < 24) and (realhour < 24) and (min > 10)):
                new_time = "{}:{} {}".format(hour, min, period)
            elif ((elapsedhour < 24) and (realhour > 24) and (min < 10)):
                new_time = "{}:0{} {} (next day)".format(hour, min, period)
            elif ((elapsedhour < 24) and (realhour > 24) and (min > 10)):
                new_time = "{}:{} {} (next day)".format(hour, min, period)
            elif ((elapsedhour == 24) and (elapsedmin == 0) and (min < 10)):
                new_time = "{}:0{} {} (next day)".format(hour, min, period)
            elif ((elapsedhour == 24) and (elapsedmin == 0) and (min > 10)):
                new_time = "{}:{} {} (next day)".format(hour, min, period)
            elif ((elapsedhour >= 24) and (elapsedmin > 0) and (min < 10)):
                elapsedtime = int((elapsedhour / 24) + 1)
                new_time = "{}:0{} {} ({} days later)".format(
                    hour, min, period, elapsedtime)
            elif ((elapsedhour >= 24) and (elapsedmin > 0) and (min > 10)):
                elapsedtime = int((elapsedhour / 24) + 1)
                new_time = "{}:{} {} ({} days later)".format(
                    hour, min, period, elapsedtime)
            else:
                None
        else:
            None

    return new_time