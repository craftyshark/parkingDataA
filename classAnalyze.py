import json

# Load JSON data from file
with open('classData.json', 'r') as f:
    data = json.load(f)

# Initialize the main data structure
classrooms = {}

# Map day abbreviations to indices
day_to_index = {"Mo": 0, "Tu": 1, "We": 2, "Th": 3, "Fr": 4, "Sa": 5, "Su": 6}

# Process the data
for item in data:
    start_time = int(item["classStartTime"])
    end_time = int(item["classEndTime"])
    enrollment = item["classEnrollment"]
    days = [day_to_index[day] for day in item["classDays"].values()]
    classroom = item["classRoom"]
    
    start_slot = (start_time // 100) * 4 + (start_time % 100) // 15
    end_slot = (end_time // 100) * 4 + (end_time % 100) // 15

    if classroom not in classrooms:
        classrooms[classroom] = [[0] * 96 for _ in range(7)]

    for day in days:
        for i in range(start_slot, end_slot):
            classrooms[classroom][day][i] += enrollment

# Save the results to a file
with open('output.json', 'w') as f:
    json.dump(classrooms, f, indent=2)
