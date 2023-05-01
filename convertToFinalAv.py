import json

# Define parking lot capacities
parking_lot_capacities = {
    "SMC1": 610, "SMC2": 606, "SMC3": 661, "SMC4": 154,
    "P1": 446, "P2": 502, "P3": 200, "P5": 665,
    "P6": 1050, "P11": 200, "P15": 203, "P20": 1335, "P27": 971
}

# Load daily_parking_lot_availability.json
with open('daily_parking_lot_availability.json', 'r') as f:
    daily_availability_data = json.load(f)

# Convert the data into the specified format
converted_data = {}
days = ['mon', 'tue', 'wed', 'thu', 'fri']

for day_index, day in enumerate(days):
    day_data = daily_availability_data[str(day_index)]
    converted_data[day] = {}

    for time_slot in range(96):
        time_slot_key = f"{(time_slot // 4 + 1) * 100:04d}"
        time_slot_data = {}

        for lot, availability in day_data.items():
            capacity = parking_lot_capacities[lot]
            occupancy_ratio = 1 - (availability[time_slot] / capacity)
            time_slot_data[lot] = occupancy_ratio

        converted_data[day][time_slot_key] = time_slot_data

# Save the converted data to a new JSON file
with open('converted_availability_data.json', 'w') as f:
    json.dump(converted_data, f)
