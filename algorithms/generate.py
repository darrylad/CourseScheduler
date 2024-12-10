import numpy as np

# Input Data Structure
timetable_data = {
    "departments": {
        "Dept1": [
            {"course": "Course1", "strength": 50, "lectures": 3},
            {"course": "Course2", "strength": 30, "lectures": 2}
        ],
        "Dept2": [
            {"course": "Course3", "strength": 40, "lectures": 3}
        ]
    },
    "rooms": [
        {"room": "R1", "capacity": 50},
        {"room": "R2", "capacity": 40},
        {"room": "R3", "capacity": 30}
    ],
    "slots": {"pre_lunch": 3, "post_lunch": 3},  # Slots per day
    "days": 5
}

def create_empty_timetable(days, slots_per_day, rooms_count):
    return [[[] for _ in range(rooms_count)] for _ in range(days * slots_per_day)]

def allocate_lectures():
    room_capacities = [room["capacity"] for room in timetable_data["rooms"]]
    pre_lunch_slots = timetable_data["slots"]["pre_lunch"]
    post_lunch_slots = timetable_data["slots"]["post_lunch"]
    num_days = timetable_data["days"]
    time_slots_per_day = pre_lunch_slots + post_lunch_slots

    # Create timetable matrix
    timetable = create_empty_timetable(num_days, time_slots_per_day, len(room_capacities))
    
    for department, courses in timetable_data["departments"].items():
        for course in courses:
            lectures_remaining = course["lectures"]
            possible_days = list(range(num_days))  # Randomize days to distribute evenly
            np.random.shuffle(possible_days)
            
            for day in possible_days:  # Iterate through available days randomly
                if lectures_remaining <= 0:
                    break
                for time_slot in range(time_slots_per_day):
                    allocated = False
                    for room_index, room_capacity in enumerate(room_capacities):
                        if any(allocated_course["course"] == course["course"] for allocated_course in timetable[day * time_slots_per_day + time_slot][room_index]):
                            continue
                        if sum(allocated_course["strength"] for allocated_course in timetable[day * time_slots_per_day + time_slot][room_index]) + course["strength"] <= room_capacity:
                            timetable[day * time_slots_per_day + time_slot][room_index].append({
                                "course": course["course"],
                                "strength": course["strength"]
                            })
                            lectures_remaining -= 1
                            allocated = True
                            break
                    if allocated:
                        break  # Stop slot iteration once a lecture is allocated into a day slot
    
    return timetable

timetable = allocate_lectures()

# Output timetable
for day in range(timetable_data["days"]):
    print(f"Day {day + 1}:")
    for slot_index in range(timetable_data["slots"]["pre_lunch"] + timetable_data["slots"]["post_lunch"]):
        print(f"  Slot {slot_index + 1}: {timetable[day * (timetable_data['slots']['pre_lunch'] + timetable_data['slots']['post_lunch']) + slot_index]}")
