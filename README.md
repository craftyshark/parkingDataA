# Parking Lot Capacity Analysis

![GitHub issues](https://img.shields.io/github/issues/user/repo?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/user/repo?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/user/repo?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/user/repo/CI?style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/user/repo?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/user/repo?style=flat-square)
![GitHub](https://img.shields.io/github/license/user/repo?style=flat-square)

This project analyzes the parking lot capacity of a university campus based on the number of students attending classes in various buildings and their distribution to different parking lots.

![Parking Lot Capacity Analysis](./assets/parking_lot_image.jpg)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Implementation Details](#implementation-details)
- [License](#license)

## Overview

The goal of the project is to determine the availability of parking spaces in each parking lot and the excess capacity needed to accommodate all the students. The analysis is performed for each time slot of the day for all 7 days of the week.

The project uses the following input data:

1. `output.json`: Contains the number of students attending classes in each building for every time slot throughout the week. The data is structured as a nested dictionary with the keys being the building names and the values being a list of 7 lists, each containing 96 time slots.
2. `buildingToParkingLot.json`: Contains the distribution of students from each building to the parking lots. It is a dictionary where the keys are building names and the values are dictionaries representing the distribution of students to each parking lot.

The project's output includes:

1. `daily_parking_lot_availability.json`: Contains the parking lot availability for each time slot throughout the week. It is structured as a dictionary with keys as day numbers (0-6) and values as dictionaries with parking lot names as keys and lists of 96 time slots as values.
2. `daily_excess_capacity_needed.json`: Contains the excess capacity needed for each time slot throughout the week. It is structured as a dictionary with keys as day numbers (0-6) and values as dictionaries with time slots as keys and excess capacity as values.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/user/repo.git
```

2. Change to the repository's directory:

```bash
cd repo
```

3. Make sure you have Python 3 installed. If not, download and install it from [here](https://www.python.org/downloads/).

## How to Run

1. Place the input files (`output.json` and `buildingToParkingLot.json`) in the same directory as the main script (`parking_lot_capacity_analysis.py`).
2. Run the script using the following command:

```bash
python parking_lot_capacity_analysis.py
```

This will generate the output files `daily_parking_lot_availability.json` and `daily_excess_capacity_needed.json` in the same directory.

## Implementation Details

The project is implemented using an object-oriented approach with a `ParkingLotCapacityAnalyzer` class that contains methods for processing the data and performing the capacity analysis. The main components of the class include:

1. Initialization: Loads input data, initializes parking lot capacities and other relevant data structures
2. `process_day()`: Processes a single day, calculating the parking lot availability and excess capacity needed for each time slot.
3. `distribute_students()`: Helper method to distribute students to the parking lots based on the given distribution.
4. `normalize_distribution()`: Helper method to normalize the distribution of students to parking lots after updating availability.
5. `assign_remaining_students()`: Helper method to assign remaining students to available parking lots.
6. `analyze()`: Main method to perform the analysis for all 7 days of the week and save the results to output files.

## Usage

To use the `ParkingLotCapacityAnalyzer` class in your own projects, simply import the class and create an instance with the input file paths. Then, call the `analyze()` method to perform the analysis and save the results to output files:

```python
from parking_lot_capacity_analysis import ParkingLotCapacityAnalyzer

analyzer = ParkingLotCapacityAnalyzer("output.json", "buildingToParkingLot.json")
analyzer.analyze()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](./LICENSE) 
