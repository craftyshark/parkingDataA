import json

# Load the original buildingToParkingLot.json
with open('buildingToParkingLot.json', 'r') as f:
    original_data = json.load(f)

# Convert string values to floats
converted_data = {
    building: {lot: float(value) for lot, value in lots.items()}
    for building, lots in original_data.items()
}

# Save the converted data to a new file
with open('buildingToParkingLot_converted.json', 'w') as f:
    json.dump(converted_data, f, indent=2)
