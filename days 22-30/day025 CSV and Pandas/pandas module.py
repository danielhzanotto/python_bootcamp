import pandas

data = pandas.read_csv(
    "/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day025 CSV and Pandas/forecast.csv")
# print(data["temp"])


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

average_temp = round(sum(temp_list) / len(temp_list), 2)
print(average_temp)

print(data["temp"].mean())


# print(data["temp"].max())

print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]


def temp_converter(temp):
    return int(temp) * 1.8 + 32


f = temp_converter(monday.temp)
print(f)

################################
# Creating a dataframe from scractch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv(
    "/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day025 CSV and Pandas/new_data.csv")
