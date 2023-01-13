# with open("forecast.csv", "r") as d:
#     list_days = d.readlines()

# new_list_days = []
# for day in list_days:
#     new_day = day.strip()
#     new_list_days.append(new_day)

#############################################

import csv

temp = []
with open("forecast.csv", "r") as d:
    data = csv.reader(d)
    for row in data:
        print(row)
        if row[1] != "temp":
            temp.append(int(row[1]))


print(temp)
