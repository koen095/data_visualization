import csv
from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Determine the row of the station name, max and min temperature
    station_name = header_row.("NAME")
    index_tmax = header_row.index("TMAX")    
    index_tmin = header_row.index("TMIN")

    # Get dates and high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            # Get the temperature in f and convert to c
            high_f = int(row[index_tmax])
            high_c = round(((high_f - 32) / 1.8), 1)
            low_f = int(row[index_tmin])
            low_c = round(((low_f - 32) / 1.8), 1)
        except ValueError:
            continue
            #print(f"Missing data for {current_date}")
        else:    
            dates.append(current_date)
            highs.append(high_c)
            lows.append(low_c)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily low and high temperatures - 2018\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylim(-10, 55)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()