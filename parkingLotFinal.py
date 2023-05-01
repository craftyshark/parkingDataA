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

# Create dictionaries to store parking lot availability and excess capacity needed for each day
daily_parking_lot_availability = {}
daily_excess_capacity_needed = {}

# Iterate over each day
for day in range(7):
    print(f"Processing Day {day + 1}")

    # Initialize parking lot availability for each time slot for the current day
    parking_lot_availability = {lot: [capacity] * 96 for lot, capacity in parking_lot_capacities.items()}
    excess_capacity_needed = {}

    # Iterate over each time slot
    for time_slot in range(96):
        print(f"Processing time slot {time_slot}")
        excess_capacity_needed[time_slot] = 0

        # Go through each building
        for building, building_timeslots in output_data.items():
            students_for_timeslot = building_timeslots[day][time_slot]

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

                # Distribute the remaining students after integer division
                remaining_students_after_distribution = remaining_students - sum(students_to_parking_lots.values())
                if remaining_students_after_distribution > 0:
                    sorted_lots = sorted(parking_lot_distribution.keys(), key=lambda x: parking_lot_distribution[x], reverse=True)
                    for lot in sorted_lots[:remaining_students_after_distribution]:
                        students_to_parking_lots[lot] += 1

                # Update the parking lot availability and normalize the distribution if needed
                new_parking_lot_distribution = {}
                for lot, students in students_to_parking_lots.items():
                    if parking_lot_availability[lot][time_slot] >= students:
                        parking_lot_availability[lot][time_slot] -= students
                        remaining_students -= students
                    elif parking_lot_availability[lot][time_slot] > 0:
                        remaining_students -= parking_lot_availability[lot][time_slot]
                        parking_lot_availability[lot][time_slot] = 0
                    new_parking_lot_distribution[lot] = parking_lot_distribution[lot]

                # Normalize the new parking lot distribution
                new_distribution_sum = sum(float(v) for v in new_parking_lot_distribution.values())
                parking_lot_distribution = {lot: float(v) / new_distribution_sum for lot, v in new_parking_lot_distribution.items()} if new_distribution_sum > 0 else {}

                # Break out of the loop if there's no change in remaining students
                if remaining_students == last_remaining_students:
                    break

            # Assign remaining students to available parking lots
            for lot in parking_lot_availability:
                if remaining_students <= 0:
                    break
                if parking_lot_availability[lot][time_slot] > 0:
                    students_assigned = min(remaining_students, parking_lot_availability[lot][time_slot])
                    parking_lot_availability[lot][time_slot] -= students_assigned
                    remaining_students -= students_assigned

            excess_capacity_needed[time_slot] += remaining_students

        print(f"Parking lot availability for time slot {time_slot}:")
        for lot, availability in parking_lot_availability.items():
            print(f"{lot}: {availability[time_slot]}")
        print(f"Excess capacity needed for time slot {time_slot}: {excess_capacity_needed[time_slot]}")
        print("\n")

    # Store the parking lot availability and excess capacity needed for the current day
    daily_parking_lot_availability[day] = parking_lot_availability
    daily_excess_capacity_needed[day] = excess_capacity_needed

# Save the daily parking lot availability and excess capacity needed to output files
with open('daily_parking_lot_availability.json', 'w') as f:
    json.dump(daily_parking_lot_availability, f)

with open('daily_excess_capacity_needed.json', 'w') as f:
    json.dump(daily_excess_capacity_needed, f)