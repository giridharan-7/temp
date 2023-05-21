import matplotlib.pyplot as plt

import csv

state_data = {}

with open('dataset_tk.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    header = csv_reader.fieldnames

    for row in csv_reader:
        for state in header[1:]:
            state_value = float(row[state])
            if state not in state_data:
                state_data[state] = []
            state_data[state].append(state_value)

data = state_data
data = {
    "Punjab": state_data["Punjab"],
    "Haryana": state_data["Haryana"],
    "Rajasthan": state_data["Rajasthan"],
    "Delhi": state_data["Delhi"],
    "UP": state_data["UP"],
    "Uttarakhand": state_data["Uttarakhand"],
    "HP": state_data["HP"],
    "J&K": state_data["J&K"],
    "Chandigarh": state_data["Chandigarh"],
    "Chhattisgarh": state_data["Chhattisgarh"],
    "Gujarat": state_data["Gujarat"],
    "MP": state_data["MP"],
    "Maharashtra": state_data["Maharashtra"],
    "Goa": state_data["Goa"],
    "DNH": state_data["DNH"],
    "Andhra Pradesh": state_data["Andhra Pradesh"],
    "Telangana": state_data["Telangana"]
}

dates = []

with open('dataset_tk.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        date = row[0]
        dates.append(date)

# Plotting the graph
for state, values in data.items():
    plt.plot(dates, values, label=state)

plt.xlabel('Date')
plt.ylabel('Power Consumption')
plt.title('Power Consumption by State')
plt.legend()
# plt.xticks(rotation=45)
plt.show()
