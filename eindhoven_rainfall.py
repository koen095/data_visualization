import csv

from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/eindhoven_2019_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and amount of rainfall from file
    dates, rainfall = [], []
    no_rain = 0
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')    
        try:
            rain = float(row[3])
        except ValueError:
            continue
        else:
            if rain == 0.0
                no_rain += 1
            dates.append(current_date)
            rainfall.append(rain)
    print(no_rain)

# Plot the rainfall
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue', alpha=0.5)
plt.fill_between(dates, rainfall, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily rainfall - 2019\nEindhoven, NL", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Amount of rain (mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
