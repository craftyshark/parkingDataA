# Parking Lot Capacity Analysis

This project analyzes the parking lot capacity of a university campus based on the number of students attending classes in various buildings and their distribution to different parking lots.

## Overview

The goal of the project is to determine the availability of parking spaces in each parking lot and the excess capacity needed to accommodate all the students. The analysis is performed for each time slot of the day for all 7 days of the week.

The project uses the following input data:

1. `output.json`: Contains the number of students attending classes in each building for every time slot throughout the week. The data is structured as a nested dictionary with the keys being the building names and the values being a list of 7 lists, each containing 96 time slots.
2. `buildingToParkingLot.json`: Contains the distribution of students from each building to the parking lots. It is a dictionary where the keys are building names and the values are dictionaries representing the distribution of students to each parking lot.

The project's output includes:

1. `daily_parking_lot_availability.json`: Contains the parking lot availability for each time slot throughout the week. It is structured as a dictionary with keys as day numbers (0-6) and values as dictionaries with parking lot names as keys and lists of 96 time slots as values.
2. `daily_excess_capacity_needed.json`: Contains the excess capacity needed for each time slot throughout the week. It is structured as a dictionary with keys as day numbers (0-6) and values as dictionaries with time slots as keys and excess capacity as values.

## How to Run

To run the project, make sure you have Python 3 installed. Place the input files (`output.json` and `buildingToParkingLot.json`) in the same directory as the main script (`parking_lot_capacity_analysis.py`). Run the script using the following command:

```bash
python parking_lot_capacity_analysis.py
```

This will generate the output files `daily_parking_lot_availability.json` and `daily_excess_capacity_needed.json` in the same directory.

## Implementation Details

The project is implemented using an object-oriented approach with a `ParkingLotCapacityAnalyzer` class that contains methods for processing the data and performing the capacity analysis. The main components of the class include:

1. Initialization: Loads input data, initializes parking lot capacities and other relevant data structures.
2. Helper methods: Implements various helper methods to break down the problem into smaller, more manageable tasks.
3. Main method: Processes each day and time slot, updates parking lot availability, and calculates excess capacity needed.

Please refer to the comments in the `parking_lot_capacity_analysis.py` file for a detailed explanation of the implementation.
