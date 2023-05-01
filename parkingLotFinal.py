import json

# Load data from files
with open('output.json', 'r') as f:
    enrollment_data = json.load(f)

with open('buildingToParkingLot.json', 'r') as f:
    building_to_parking_lot = json.load(f)

# Initialize parking lot capacities
parking_lot_capacities = {
    "SMC1": 610, "SMC2": 606, "SMC3": 661, "SMC4": 154,
    "P1": 446, "P2": 502, "P3": 200, "P5": 665, "P6": 1050,
    "P11": 200, "P15": 203, "P20": 1335, "P27": 971
}

# Function to normalize the distribution when a parking lot is full
def normalize_distribution(distribution):
    total = sum(distribution.values())
    if total == 0:
        return {}
    return {k: v / total for k, v in distribution.items()}

# Initialize the main data structure for parking lot occupancy
parking_lot_occupancy = {lot: [[0] * 96 for _ in range(7)] for lot in parking_lot_capacities}

# Iterate over each day and timeslot
for day in range(7):
    for timeslot in range(96):
        # Iterate over each building
        for building, building_enrollment in enrollment_data.items():
            students = building_enrollment[day][timeslot]

            # Get the building-to-parking lot distribution and normalize it
            distribution = normalize_distribution(building_to_parking_lot.get(building, {}))

            # Distribute students to parking lots
            while students > 0 and distribution:
                no_more_spots = True
                for lot, ratio in distribution.items():
                    spots_to_fill = int(students * ratio)

                    if parking_lot_occupancy[lot][day][timeslot] + spots_to_fill <= parking_lot_capacities.get(lot, 200):
                        parking_lot_occupancy[lot][day][timeslot] += spots_to_fill
                        students -= spots_to_fill
                        no_more_spots = False
                    else:
                        spots_filled = parking_lot_capacities.get(lot, 200) - parking_lot_occupancy[lot][day][timeslot]
                        parking_lot_occupancy[lot][day][timeslot] = parking_lot_capacities.get(lot, 200)
                        students -= spots_filled
                        del distribution[lot]

                if no_more_spots:
                    break

                distribution = normalize_distribution(distribution)


# Save the parking lot occupancy data to a file
with open('parking_lot_occupancy.json', 'w') as f:
    json.dump(parking_lot_occupancy, f, indent=2)
