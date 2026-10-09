# 1
numbers = [10, 20, 10, 30, 20, 40, 10, 50]
numbers_set = set(numbers)
print(numbers)
print(numbers_set)
print(len(numbers_set))
print(30 in numbers_set)
print(100 in numbers_set)

# 2
data = [15, "Python", 15, True, "Python", 3.14, False, True]
data_set = set(data)
print(data_set)
data_set.add("Redis")
data_set.add(100)
data_set.remove("Python")
print(data_set)
print(True in data_set)
print(False in data_set)

# 3
python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"}
union_1 = python_students | redis_students
union_2 = python_students.union(redis_students)
print(union_1)
print(union_2)
print(union_1 == union_2)

# 4
print(python_students & redis_students)
print(python_students.intersection(redis_students))

# 5
all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students = {"Anna", "Oleh", "Ivan"}
print(all_students - python_students)
print(all_students.difference(python_students))

# 6
numbers = {10, 20, 30}
numbers.add(40)
numbers.add(40)
numbers.update([50, 60, 70])
numbers.remove(20)
numbers.discard(100)
print(numbers.pop())
print(numbers)