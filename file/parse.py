



import csv
import os
import json

from configs.text import Text
from file.check import Check

# timetable_data = {
#     "departments": {
#         "cs": [
#             {"course": "CS204", "strength": 50, "credits": 3, "year": 2},
#             {"course": "CS206", "strength": 30, "credits": 2, "year": 2},
#             {"course": "CS304", "strength": 30, "credits": 2, "year": 3}
#         ],
#         "me": [
#             {"course": "ME201", "strength": 40, "credits": 3, "year": 2}
#         ]
#     },
#     "rooms": [
#         {"room": "R1", "capacity": 50},
#         {"room": "R2", "capacity": 40},
#         {"room": "R3", "capacity": 30}
#     ],
#     "slots": {"pre_lunch": 3, "post_lunch": 3},  # Slots per day
#     "days": 5
# }

timetable_data = {
    "departments": {},
    "rooms": [],
    "slots": {"pre_lunch": 3, "post_lunch": 3},
    "days": 5
}

class Parse:
    REQUIRED_COLUMNS = {"year", "department", "course", "credits", "strength"}

    @staticmethod
    def populate_timetable_data(input_folder):
        input_folder = input_folder.strip().strip('\'"')

        if not Check.checkPath(input_folder):
            return

        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.lower().endswith('.csv'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        reader = csv.DictReader(f)
                        if Parse.REQUIRED_COLUMNS.issubset(reader.fieldnames):
                            for row in reader:
                                # Skip rows with missing required values
                                if not all(row[col] for col in Parse.REQUIRED_COLUMNS):
                                    continue
                                
                                try:
                                    year = int(row['year'])
                                    department = row['department'].lower()
                                    course = row['course'].lower()
                                    credits = int(row['credits'])
                                    strength = int(row['strength'])
                                except ValueError as e:
                                    Text.FIELD_ERROR(row, e, file_path)
                                    continue

                                if department not in timetable_data["departments"]:
                                    timetable_data["departments"][department] = []

                                # Check for duplicates within the same department
                                if not any(c['course'] == course for c in timetable_data["departments"][department]):
                                    timetable_data["departments"][department].append({
                                        "course": course,
                                        "credits": credits,
                                        "strength": strength,
                                        "year": year
                                    })


    @staticmethod
    def populate_rooms(input_folder):
        rooms_file = os.path.join(input_folder, 'rooms.csv')
        if os.path.exists(rooms_file):
            with open(rooms_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    timetable_data["rooms"].append({
                        "room": row['Room'],
                        "capacity": int(row['Capacity'])
                    })

    @staticmethod
    def printdata():
        print("\nTimetable data:")
        def custom_print(data, indent=0):
            for key, value in data.items():
                if isinstance(value, dict):
                    print(' ' * indent + f'"{key}": {{')
                    custom_print(value, indent + 4)
                    print(' ' * indent + '},')
                elif isinstance(value, list):
                    print(' ' * indent + f'"{key}": [')
                    for item in value:
                        if isinstance(item, dict):
                            print(' ' * (indent + 4) + '{', end='')
                            print(', '.join(f'"{k}": {json.dumps(v)}' for k, v in item.items()), end='')
                            print('},')
                        else:
                            print(' ' * (indent + 4) + f'{json.dumps(item)},')
                    print(' ' * indent + '],')
                else:
                    print(' ' * indent + f'"{key}": {json.dumps(value)},')

        print('{')
        custom_print(timetable_data, 4)
        print('}')

    