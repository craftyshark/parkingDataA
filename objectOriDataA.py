import json


class ParkingLotSystem:
    def __init__(self, output_file, building_to_parking_lot_file):
        self.output_data = self.load_json_data(output_file)
        self.building_to_parking_lot_data = self.load_json_data(building_to_parking_lot_file)

        self.parking_lot_capacities = {
            "SMC1": 610, "SMC2": 606, "SMC3": 661, "SMC4": 154,
            "P1": 446, "P2": 502, "P3": 200, "P5": 665,
            "P6": 1050, "P11": 200, "P15": 203, "P20": 1335, "P27": 971
        }

    @staticmethod
    def load_json_data(file):
        with open(file, 'r') as f:
            return json.load(f)

    def calculate_parking_availability(self):
        daily_parking_lot_availability = {}
        daily_excess_capacity_needed = {}

        for day in range(7):
            parking_lot_availability, excess_capacity_needed = self.process_day(day)
            daily_parking_lot_availability[day] = parking_lot_availability
            daily_excess_capacity_needed[day] = excess_capacity_needed

        return daily_parking_lot_availability, daily_excess_capacity_needed

    def process_day(self, day):
        parking_lot_availability = {lot: [capacity] * 96 for lot, capacity in self.parking_lot_capacities.items()}
        excess_capacity_needed = {}

        for time_slot in range(96):
            excess_capacity_needed[time_slot] = 0

            for building, building_timeslots in self.output_data.items():
                students_for_timeslot = building_timeslots[day][time_slot]

                if students_for_timeslot == 0:
                    continue

                parking_lot_distribution = self.building_to_parking_lot_data[building]
                remaining_students = students_for_timeslot
                
                while remaining_students > 0 and parking_lot_distribution:
                    last_remaining_students = remaining_students
                    remaining_distribution_sum = sum(float(v) for v in parking_lot_distribution.values())
                    students_to_parking_lots = {lot: int(remaining_students * float(p) / remaining_distribution_sum) for lot, p in parking_lot_distribution.items()}

                    remaining_students_after_distribution = remaining_students - sum(students_to_parking_lots.values())
                    if remaining_students_after_distribution > 0:
                        sorted_lots = sorted(parking_lot_distribution.keys(), key=lambda x: parking_lot_distribution[x], reverse=True)
                        for lot in sorted_lots[:remaining_students_after_distribution]:
                            students_to_parking_lots[lot] += 1

                    new_parking_lot_distribution = {}
                    for lot, students in students_to_parking_lots.items():
                        if parking_lot_availability[lot][time_slot] >= students:
                            parking_lot_availability[lot][time_slot] -= students
                            remaining_students -= students
                        elif parking_lot_availability[lot][time_slot] > 0:
                            remaining_students -= parking_lot_availability[lot][time_slot]
                            parking_lot_availability[lot][time_slot] = 0
                        new_parking_lot_distribution[lot] = parking_lot_distribution[lot]

                    new_distribution_sum = sum(float(v) for v in new_parking_lot_distribution.values())
                    parking_lot_distribution = {lot: float(v) / new_distribution_sum for lot, v in new_parking_lot_distribution.items()} if new_distribution_sum > 0 else {}

                    if remaining_students == last_remaining_students:
                        break

                for lot in parking_lot_availability:
                    if remaining_students <= 0:
                        break
                    if parking_lot_availability[lot][time_slot] > 0:
                        students_assigned = min(remaining_students, parking_lot_availability[lot][time_slot])
                        parking_lot_availability[lot][time_slot] -= students_assigned
                        remaining_students -= students_assigned

                excess_capacity_needed[time_slot] += remaining_students

        return parking_lot_availability, excess_capacity_needed


def main():
    parking_lot_system = ParkingLotSystem('output.json', 'buildingToParkingLot.json')
    daily_parking_lot_availability, daily_excess_capacity_needed = parking_lot_system.calculate_parking_availability()

    with open('daily_parking_lot_availability.json', 'w') as f:
        json.dump(daily_parking_lot_availability, f)

    with open('daily_excess_capacity_needed.json', 'w') as f:
        json.dump(daily_excess_capacity_needed, f)


if __name__ == "__main__":
    main()
