import json

# List of valid buildings
valid_buildings = [
    "Kremen Education Bldg", "University Center", "Peters Business Bldg", "Social Science Bldg",
    "Agricultural Building", "Ag Mechanic Building", "Engineering East Bldg", "Family Food & Sci Bldg",
    "McLane Hall", "Science Building", "Engineering West Bldg", "Science 2 Building", "Conley Art Building",
    "Music Building", "Industrial Tech Bldg", "ANIMAL SCIENCE PAVILION", "DAIRY UNIT", "MEATS LAB",
    "North Gym", "Learning Center", "Prof Human Srvce Bldg", "LAB School Building", "South Gym", "PTIA",
    "Speech Arts Building", "McKee-Fisk Building", "Enology Building", "Lyles Center 208", "Kinesiology Pool",
    "Athletic Track", "Spalding Wathen Tennis Courts", "Peters Education Center", "Saint Agnes Hospital",
    "Community Behavioral Health Ce", "Community Regional Medical Ctr", "Madera Health Department",
    "Fresno Health Department", "Tulare County Health Dept", "Horticulture Unit Laboratory"
]

# Load class data from the JSON file
with open('classData.json', 'r') as f:
    class_data = json.load(f)

# Filter out any classes not in the specified buildings
filtered_class_data = [class_info for class_info in class_data if class_info["classRoom"] in valid_buildings]

# Save the filtered class data to a new JSON file
with open('filtered_class_data.json', 'w') as f:
    json.dump(filtered_class_data, f)
