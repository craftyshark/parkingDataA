
import json

# Load data from output.json and buildingToParkingLot.json
with open('output.json', 'r') as f:
    output_data = json.load(f)

with open('buildingToParkingLot.json', 'r') as f:
    building_to_parking_lot_data = json.load(f)

# Initialize parking lot capacities and availability for each time slot
parking_lot_capacities = {
    "SMC1": 610, "SMC2": 606, "SMC3": 661, "SMC4": 154,
    "P1": 446, "P2": 502, "P3": 200, "P5": 665,
    "P6": 1050, "P11": 200, "P15": 203, "P20": 1335, "P27": 971
}

parking_lot_availability = {lot: [capacity] * 96 for lot, capacity in parking_lot_capacities.items()}
excess_capacity_needed = {}

# Iterate over each time slot
for time_slot in range(96):
    print(f"Processing time slot {time_slot}")
    excess_capacity_needed[time_slot] = 0

    # Go through each building
    for building, building_timeslots in output_data.items():
        students_for_timeslot = sum(day_slots[time_slot] for day_slots in building_timeslots)

        if students_for_timeslot == 0:
            continue

        # Get the distribution of students from the building to the parking lots
        parking_lot_distribution = building_to_parking_lot_data[building]
        remaining_students = students_for_timeslot

        # Calculate the number of students going to each parking lot and update availability
        while remaining_students > 0 and parking_lot_distribution:
            last_remaining_students = remaining_students
            remaining_distribution_sum = sum(float(v) for v in parking_lot_distribution.values())
            students_to_parking_lots = {lot: int(remaining_students * float(p) / remaining_distribution_sum) for lot, p in parking_lot_distribution.items()}

            # Update the parking lot availability and normalize the distribution if needed
            new_parking_lot_distribution = {}
            for lot, students in students_to_parking_lots.items():
                if parking_lot_availability[lot][time_slot] >= students:
                    parking_lot_availability[lot][time_slot] -= students
                    remaining_students -= students
                else:
                    remaining_students -= parking_lot_availability[lot][time_slot]
                    parking_lot_availability[lot][time_slot] = 0
                    new_parking_lot_distribution[lot] = parking_lot_distribution[lot]

            parking_lot_distribution = new_parking_lot_distribution

            # Break out of the loop if there's no change in remaining students
            if remaining_students == last_remaining_students:
                excess_capacity_needed[time_slot] += remaining_students
                break

    print(f"Parking lot availability for time slot {time_slot}:")
    for lot, availability in parking_lot_availability.items():
        print(f"{lot}: {availability[time_slot]}")
    print(f"Excess capacity needed for time slot {time_slot}: {excess_capacity_needed[time_slot]}")
    print("\n")