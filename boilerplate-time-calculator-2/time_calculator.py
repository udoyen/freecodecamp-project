week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
current_day = " "
_24_time_mapper = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 1,
    14: 2,
    15: 3,
    16: 4,
    17: 5,
    18: 6,
    19: 7,
    20: 8,
    21: 9,
    22: 10,
    23: 11,
    0: 12
}


def midday_status_helper(midday_status: str) -> str:
    """
    Function to help determine the
    midday status "PM" or "AM"
    :param midday_status:
    :type midday_status: str
    :rtype: str
    """
    if midday_status.upper() == 'PM':
        return 'AM'
    return 'PM'


def time_with_no_day(start: str, duration: str) -> str:
    """
    Return string result for time
    with no day argument added
    :param start:
    :type start: str
    :param duration:
    :type duration: str
    :rtype: str
    """
    # "3:30 PM" and "33:33"
    #    3:00
    # + 33:33
    # -------
    # split the time arguments
    section_1 = start.split(":")
    section_2 = section_1[1].split(" ")
    main_hour = int(section_1[0])
    main_mins = int(section_2[0])
    time_of_day = section_2[1]  # PM or AM
    duration_components = duration.split(":")
    duration_hours = int(duration_components[0])
    duration_mins = int(duration_components[1])

    total_mins = main_mins + duration_mins

    if total_mins > 59:
        real_mins = total_mins % 60
        extra_hours = round(total_mins / 60)

        real_duration = duration_hours + extra_hours

        # New main hour
        if real_duration + main_hour >= 24:
            new_time_hr = _24_time_mapper[main_hour + (real_duration % 24)]
        else:
            if (real_duration + main_hour) % 12 == 0:
                new_time_hr = real_duration + main_hour
            else:
                new_time_hr = (real_duration + main_hour) % 12

        # Flip the PM or AM
        if real_duration + main_hour >= 12:
            # Check if it's just next day or n days
            if 0.20 < real_duration / 24 < 1:
                midday_status = midday_status_helper(time_of_day)
                flip = 'next day'
                return f"{new_time_hr}:{real_mins:02} {midday_status} ({flip})"
            if real_duration / 24 < 0.20:
                return f"{new_time_hr}:{real_mins:02} {midday_status_helper(time_of_day)}"
            if real_duration / 24 >= 1:
                if real_duration == 24:
                    midday_status = time_of_day
                    return f"{new_time_hr}:{real_mins:02} {midday_status} (next day)"
                elif main_hour + (real_duration % 24) >= 12:
                    midday_status = midday_status_helper(time_of_day)
                    days = round(real_duration / 24) + 1
                    return f"{new_time_hr}:{real_mins:02} {midday_status} ({days} days later)"
                else:
                    midday_status = time_of_day
                    days = round(real_duration / 24) + 1
                    return f"{new_time_hr}:{total_mins:02} {midday_status} ({days} days later)"
        else:
            return f"{new_time_hr}:{real_mins:02} {time_of_day}"
    else:
        real_duration = duration_hours

        # New main hour
        if real_duration + main_hour >= 24:
            new_time_hr = _24_time_mapper[main_hour + (real_duration % 24)]
        else:
            if (real_duration + main_hour) % 12 == 0:
                new_time_hr = real_duration + main_hour
            else:
                new_time_hr = (real_duration + main_hour) % 12

        # Flip the PM or AM
        if (real_duration + main_hour) / 12 >= 1:
            # Check if it's just next day or n days
            if 0.20 < real_duration / 24 < 1:
                midday_status = midday_status_helper(time_of_day)
                flip = 'next day'
                return f"{new_time_hr}:{total_mins:02} {midday_status} ({flip})"
            if real_duration / 24 < 0.20:
                return f"{new_time_hr}:{total_mins:02} {midday_status_helper(time_of_day)}"
            if real_duration / 24 >= 1:
                if real_duration == 24:
                    midday_status = time_of_day
                    return f"{new_time_hr}:{total_mins:02} {midday_status} (next day)"
                elif main_hour + (real_duration % 24) >= 12:
                    midday_status = midday_status_helper(time_of_day)
                    days = round(real_duration / 24) + 1
                    return f"{new_time_hr}:{total_mins:02} {midday_status} ({days} days later)"
                else:
                    midday_status = time_of_day
                    days = round(real_duration / 24) + 1
                    return f"{new_time_hr}:{total_mins:02} {midday_status} ({days} days later)"
        else:
            return f"{new_time_hr}:{total_mins:02} {time_of_day}"


def time_with_day(start: str, duration: str, day: str = None) -> str:
    """
    Return string result for time
    with day argument added
    :param start:
    :type start: str
    :param duration:
    :type duration: str
    :param day:
    :type day: str
    :rtype: str
    """
    # "3:30 PM" and "33:33"
    #    3:00
    # + 33:33
    # -------
    # split the time arguments
    section_1 = start.split(":")
    section_2 = section_1[1].split(" ")
    main_hour = int(section_1[0])
    main_mins = int(section_2[0])
    time_of_day = section_2[1]  # PM or AM
    duration_components = duration.split(":")
    duration_hours = int(duration_components[0])
    duration_mins = int(duration_components[1])

    total_mins = main_mins + duration_mins

    global current_day

    if total_mins > 59:
        real_mins = total_mins % 60
        extra_hours = round(total_mins / 60)

        real_duration = duration_hours + extra_hours

        # New main hour
        if real_duration + main_hour >= 24:
            new_time_hr = _24_time_mapper[main_hour + (real_duration % 24)]
        else:
            if (real_duration + main_hour) % 12 == 0:
                new_time_hr = real_duration + main_hour
            else:
                new_time_hr = (real_duration + main_hour) % 12

        # Flip the PM or AM
        if (real_duration + main_hour) / 12 >= 1:
            # Check if it's just next day or n days
            if 0.20 < real_duration / 24 < 1:
                midday_status = midday_status_helper(time_of_day)
                flip = 'next day'
                return "{0}:{1:02} {2}, {3} ({4})".format(new_time_hr, real_mins, midday_status,
                                                          week_days[week_days.index(day.capitalize()) + 1], flip)
            if real_duration / 24 < 0.20:
                return f"{new_time_hr}:{real_mins:02} {time_of_day}, {day.capitalize()}"
            if real_duration / 24 >= 1:
                if real_duration == 24:
                    midday_status = time_of_day
                    return f"{new_time_hr}:{real_mins:02} {midday_status}, {week_days[week_days.index(day) + 1]}" \
                           f" (next day)"
                elif main_hour + (real_duration % 24) >= 12:
                    midday_status = midday_status_helper(time_of_day)
                    days = round(real_duration / 24) + 1
                    # Determine the day of the week
                    current_day = " "
                    for i in week_days:
                        if current_day == i:
                            break
                        n = week_days.index(i)
                        for j in range(0, week_days.index(day) + days):
                            if n == week_days.index(day.capitalize()) + days:
                                current_day = i
                                break
                            n += 7
                    return f"{new_time_hr}:{real_mins:02} {midday_status}, {current_day} ({days} days later)"
                else:
                    if real_duration == 24:
                        midday_status = time_of_day
                        return f"{new_time_hr}:{real_mins:02} {midday_status}, {day} (next day)"
                    elif main_hour + (real_duration % 24) >= 12:
                        midday_status = midday_status_helper(time_of_day)
                        days = round(real_duration / 24) + 1
                        # Determine the day of the week
                        current_day = " "
                        for i in week_days:
                            if current_day == i:
                                break
                            n = week_days.index(i)
                            for j in range(0, week_days.index(day.capitalize()) + days):
                                if n == week_days.index(day.capitalize()) + days:
                                    print(f"day: {i}")
                                    current_day = i
                                    break
                                n += 7
                        return f"{new_time_hr}:{real_mins:02} {midday_status}, {current_day} ({days} days later)"
                    else:
                        midday_status = time_of_day
                        days = round(real_duration / 24) + 1
                        # Determine the day of the week
                        current_day = " "
                        for i in week_days:
                            if current_day == i:
                                break
                            n = week_days.index(i)
                            for j in range(0, week_days.index(day.capitalize()) + days):
                                if n == week_days.index(day.capitalize()) + days:
                                    print(f"day: {i}")
                                    current_day = i
                                    break
                                n += 7
                        return f"{new_time_hr}:{real_mins:02} {midday_status}, {current_day} ({days} days later)"
        else:
            return f"{new_time_hr}:{real_mins:02} {time_of_day}, {day.capitalize()}"
    else:

        real_duration = duration_hours

        # New main hour
        if real_duration + main_hour >= 24:
            new_time_hr = _24_time_mapper[main_hour + (real_duration % 24)]
        else:
            if (real_duration + main_hour) % 12 == 0:
                new_time_hr = real_duration + main_hour
            else:
                new_time_hr = (real_duration + main_hour) % 12

        # Flip the PM or AM
        if (real_duration + main_hour) / 12 >= 1:
            # Check if it's just next day or n days
            if 0.20 < real_duration / 24 < 1:
                midday_status = midday_status_helper(time_of_day)
                flip = 'next day'
                return "{0}:{1:02} {2}, {3} ({4})".format(new_time_hr, total_mins, midday_status,
                                                          week_days[week_days.index(day.capitalize()) + 1], flip)
            if real_duration / 24 < 0.20:
                return f"{new_time_hr}:{total_mins:02} {time_of_day}, {day.capitalize()}"
            if real_duration / 24 >= 1:
                if real_duration == 24:
                    midday_status = time_of_day
                    days = round(real_duration / 24)
                    # Determine the day of the week
                    current_day = " "
                    for i in week_days:
                        if current_day == i:
                            break
                        n = week_days.index(i)
                        for j in range(0, week_days.index(day.capitalize())):
                            if n == week_days.index(day.capitalize()) + days:
                                current_day = i
                                break
                            n += 7
                    return f"{new_time_hr}:{total_mins:02} {midday_status}, {current_day} (next day)"
                elif main_hour + (real_duration % 24) >= 12:
                    midday_status = midday_status_helper(time_of_day)
                    days = round(real_duration / 24) + 1
                    # Determine the day of the week
                    current_day = " "
                    for i in week_days:
                        if current_day == i:
                            break
                        n = week_days.index(i)
                        for j in range(0, week_days.index(day.capitalize()) + days):
                            if n == week_days.index(day.capitalize()) + days:
                                current_day = i
                                break
                            n += 7
                    # first error
                    return f"{new_time_hr}:{total_mins:02} {midday_status}, {current_day} ({days} days later)"
                else:
                    if real_duration == 24:
                        midday_status = time_of_day
                        return f"{new_time_hr}:{total_mins:02} {midday_status}, {day.capitalize()} (next day)"
                    elif main_hour + (real_duration % 24) >= 12:
                        midday_status = midday_status_helper(time_of_day)
                        days = round(real_duration / 24) + 1
                        # Determine the day of the week
                        current_day = " "
                        for i in week_days:
                            if current_day == i:
                                break
                            n = week_days.index(i)
                            for j in range(0, week_days.index(day.capitalize())):
                                if n == week_days.index(day.capitalize()) + days:
                                    current_day = i
                                    break
                                n += 7
                        return f"{new_time_hr}:{total_mins:02} {midday_status}, {current_day} ({days} days later)"
                    else:
                        midday_status = time_of_day
                        days = round(real_duration / 24) + 1
                        # Determine the day of the week
                        current_day = " "
                        for i in week_days:
                            if current_day == i:
                                break
                            n = week_days.index(i)
                            for j in range(0, week_days.index(day)):
                                if n == week_days.index(day.capitalize()) + days:
                                    print(f"day: {i}")
                                    current_day = i
                                    break
                                n += 7
                        return f"{new_time_hr}:{total_mins:02} {midday_status}, {current_day} ({days} days later)"
        else:
            return f"{new_time_hr}:{total_mins:02} {time_of_day}, {day.capitalize()}"


def add_time(start: str, duration: str, day: str = None) -> callable:
    """
    Main entry point
    for the application
    :param start:
    :type start: str
    :param duration:
    :type duration: str
    :param day:
    :type day: str
    :rtype: callable
    """
    if day is None:
        return time_with_no_day(start, duration)
    return time_with_day(start, duration, day)
