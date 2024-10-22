import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1, time2):
    total_hours = time1.hour + time2.hour
    total_minutes = time1.minute + time2.minute
    total_seconds = time1.second + time2.second

    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60
    total_hours += total_minutes // 60
    total_minutes = total_minutes % 60
    total_hours = total_hours % 24

    result = data.Time(total_hours, total_minutes, total_seconds)
    return result

# Part 4
def is_descending(lst):
    if len(lst) < 2:
        return True
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            return False
    return True

# Part 5
def largest_between(nums, lower, upper):
    if lower > upper:
        return None
    if lower < 0:
        lower = 0
    if upper >= len(nums):
        upper = len(nums) - 1
    if lower > upper:
        return None
    max_index = lower
    for i in range(lower, upper + 1):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index

# Part 6

def furthest_from_origin(points):
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    if not points:
        return None

    max_index = 0
    max_distance = distance_from_origin(points[0])
    for i in range(1, len(points)):
        distance = distance_from_origin(points[i])
        if distance > max_distance:
            max_distance = distance
            max_index = i

    return max_index