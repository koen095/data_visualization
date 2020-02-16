import csv

from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/eindhoven_2019_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs and lows from file
    dates, highs, lows = [], [], []
    plus_30 = 0
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')    
        try:
            high = float(row[4])
            low = float(row[5])
        except ValueError:
            continue
        else:
            if high >= 30:
                plus_30 += 1
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    print(f"Amount of days temperatures exceeded 30 degrees: {plus_30}")

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures 2019\nEindhoven, NL", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylim(-10, 55)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

