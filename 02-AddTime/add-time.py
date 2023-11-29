def add_time(startTime, duration, startingDay=''):
    """ Returns sum of startTime and duration. If starting day is set, it can also tell a day of week """

    # Data from func input (startTime)
    daysOfWeek = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = int(startTime.split(' ')[0].split(':')[0])
    minutes = int(startTime.split(' ')[0].split(':')[1])
    halfOfDay = startTime.split(' ')[1]
    
    # Data from func input (duration)

    dur_hours = int(duration.split(':')[0])
    dur_minutes = int(duration.split(':')[1])

    # Data from func input (startingDay) formatted to numeric value
    day = ''
    daysPassed = 0

    # Changing hours from AM/PM to 24h format
    if halfOfDay == 'PM':
        hours = hours + 12

        # Solving problem ...

    # ... with sum of minutes changing a hour

    if minutes + dur_minutes > 60:
        minutes = (minutes + dur_minutes) - 60
        hours = hours + 1
    else:
        minutes = minutes + dur_minutes
    
    # ... with sum of hours changing day
    if hours + dur_hours >= 24:
        daysPassed = (hours + dur_hours)//24
        hours = (hours + dur_hours)%24
    else:
        hours = hours + dur_hours
    
    # ... with startingDay set ...
    if startingDay != '':
        if daysPassed == 0:
            day = daysOfWeek[daysOfWeek.index(startingDay.capitalize())]
        # ... that with daysPassed is NOT passing to next week
        elif (daysPassed + daysOfWeek.index(startingDay.capitalize())) <= 6:
            day = daysOfWeek[daysPassed + daysOfWeek.index(startingDay.capitalize())]
        # ... that with daysPassed IT IS passing to next week(s)
        else:
            daysToEndOfWeek = 7 - daysOfWeek.index(startingDay.capitalize())
            day = daysOfWeek[(daysPassed - daysToEndOfWeek)%7]

# Final formatting before output section
        
    # Returning to AM/PM format
    if hours == 0:
        hours = 12
        halfOfDay = 'AM'
    elif hours < 12:
        halfOfDay = 'AM'
    elif hours == 12:
        halfOfDay = 'PM'
    else:
        hours = hours-12
        halfOfDay = 'PM'
    
    # Formatting minutes to return for ex. '05' instead of '5'
    if len(str(minutes)) == 1:
        minutes = f'0{minutes}'

# Output section

    if startingDay == '':
        main_return = f'{hours}:{minutes} {halfOfDay}'
        if daysPassed == 0:
            return main_return
        elif daysPassed == 1:
            return f'{main_return} (next day)'
        else:
            return f'{main_return} ({daysPassed} days later)'
    else:
        main_return = f'{hours}:{minutes} {halfOfDay},'
        if daysPassed == 0:
            return f'{main_return} {day}'
        elif daysPassed == 1:
            return f'{main_return} {day} (next day)'
        else:
            return f'{main_return} {day} ({daysPassed} days later)'
       
