with open("days 22-30/day026 List Comprehension/list1.txt") as data_1:
    list_1 = data_1.readlines()

with open("days 22-30/day026 List Comprehension/list2.txt") as data_2:
    list_2 = data_2.readlines()

intersection_list = [
    int(n.strip()) for n in list_1 if n in list_2]
print(intersection_list)
