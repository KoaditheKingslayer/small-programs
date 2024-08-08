def add_time(start, duration, day=''):

    result = time_math(start, duration, day)
    
    # Format the new time as a string
    new_time = f'{result[0]}:{result[1]} {result[2]}'
    
    # Append the day of the week if provided
    if result[4] != '':
        new_time += f', {result[4]}'
    
    # Append the number of days later if applicable
    if result[3] > 0:
        if result[3] == 1:
            new_time += " (next day)"
        else:
            new_time += f' ({result[3]} days later)'
    
    # Print and return the new time
    print(new_time)
    return new_time

def parse_time(start):
    # Split the time and period if provided, otherwise split only time
    if len(start.split()) > 1:
        time, period = start.split()
        hour, minute = map(int, time.split(':'))
        return hour, minute, period
    else:
        time = start
        hour, minute = map(int, time.split(':'))
        return hour, minute

def time_math(time_1, time_2, day):
    # Parse the start and duration times
    time_start = parse_time(time_1)
    time_duration = parse_time(time_2)
    
    # Initialize the result list
    time_result = [0, 0, '', 0, '']  # [hour, minute, period, days_later, new_day]
    
    # List of AM and PM hours for 24-hour conversion
    am_list = [24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    pm_list = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    
    # Days of the week for handling day change
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Find the index of the provided day, if any
    if day:
        day_index = days_of_week.index(day.capitalize())
    else:
        day_index = -1

    # Convert 12 AM to 0 and 12 PM to 12, otherwise convert PM hours to 24-hour format
    if time_start[0] == 12 and time_start[2] == 'AM':
        time_start = (0, time_start[1], time_start[2])
    elif time_start[0] == 12 and time_start[2] == 'PM':
        time_start = (12, time_start[1], time_start[2])
    elif time_start[2] == 'PM':
        time_start = (time_start[0] + 12, time_start[1], time_start[2])
    
    # Calculate total minutes and days later
    total_minutes = (time_start[0] * 60 + time_start[1]) + (time_duration[0] * 60 + time_duration[1])
    days_later = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    # Calculate the new hour and minute
    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60

    # Determine the new period (AM/PM)
    if new_hour >= 12:
        new_period = 'PM'
        if new_hour > 12:
            new_hour -= 12
    else:
        new_period = 'AM'
        if new_hour == 0:
            new_hour = 12

    # Set the result time
    time_result[0] = new_hour
    time_result[1] = '{:02}'.format(new_minute)
    time_result[2] = new_period
    time_result[3] = days_later

    # Calculate the new day of the week, if applicable
    if day_index != -1:
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        time_result[4] = new_day
    
    # Return the calculated time and additional info
    return time_result

# Example calls to test the function
add_time('3:30 PM', '2:12', 'Monday')
