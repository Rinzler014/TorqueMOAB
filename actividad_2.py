import pandas as pd
import datetime

data = pd.read_csv('data.csv')

def state_with_the_most_accidents():
    
    states = data["State"].values
    states = pd.DataFrame(states, columns=["State"])
    return states["State"].value_counts()

def hours_with_most_accidents():
    
    dates = data["Start_Time"].values

    hours = []

    for date in dates:
        date = date.split(" ")
        date = date[1].split(":")
        date = date[0]
        
        hours.append(date + ":00")
    
    hours = pd.DataFrame(hours, columns=["Start_Time"])
    hours = hours["Start_Time"].value_counts().head(5)
    times = []
    
    for hour in hours.index:
        hour = hour.split(":")
        hour = hour[0]
        times.append("Day" if int(hour) < 17 else "Night")
        
    return pd.DataFrame({
        "Hour": hours.index,
        "Accidents": hours.values,
        "Time": times
    })
    
def day_with_most_accidents():
    
    dates = data["Start_Time"].values    
    days = []

    for date in dates:
        date = date.split(" ")
        date = date[0]
        
        day = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
        
        days.append(day)
            
    days = pd.DataFrame(days, columns=["Start_Time"])
    return days["Start_Time"].value_counts().head(1)

def time_with_most_cases():

    day = 0
    night = 0
    
    for index, time in enumerate(hours_with_most_accidents()["Time"]):
        if time == "Day": day += int(hours_with_most_accidents()["Accidents"][index])
        else: night += int(hours_with_most_accidents()["Accidents"][index])

    return day, night

