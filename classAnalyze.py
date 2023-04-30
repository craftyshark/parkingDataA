import json

# Load JSON data from file
with open('classData.json', 'r') as f:
    data = json.load(f)

# Initialize time slots for each day of the week
time_slots = [[0] * 96 for _ in range(7)]  # 7 days, 96 time slots each

# Map day abbreviations to indices
day_to_index = {"Mo": 0, "Tu": 1, "We": 2, "Th": 3, "Fr": 4, "Sa": 5, "Su": 6}

# Process the data
for item in data:
    start_time = int(item["classStartTime"])
    end_time = int(item["classEndTime"])
    enrollment = item["classEnrollment"]
    days = [day_to_index[day] for day in item["classDays"].values()]
    
    start_slot = (start_time // 100) * 4 + (start_time % 100) // 15
    end_slot = (end_time // 100) * 4 + (end_time % 100) // 15

    for day in days:
        for i in range(start_slot, end_slot):
            time_slots[day][i] += enrollment

# Normalize the data
normalized_slots = []
for day_slots in time_slots:
    max_enrollment = max(day_slots)
    min_enrollment = min(day_slots)
    
    if max_enrollment == min_enrollment:
        normalized_day_slots = [0] * len(day_slots)
    else:
        normalized_day_slots = [(x - min_enrollment) / (max_enrollment - min_enrollment) for x in day_slots]
        
    normalized_slots.append(normalized_day_slots)

# Prepare the output in JSON format
output = {
    "total_enrollment": time_slots,
    "normalized_enrollment": normalized_slots
}

# Print the output in JSON format
print(json.dumps(output, indent=2))
