import pandas

data = pandas.read_csv(
    "days 22-30/day025 CSV and Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# print(data["Primary Fur Color"])

fur_color_dict = {
    "colors": ["cinnamon", "gray", "black", "other"],
    "population": [0, 0, 0, 0],
}

for squirrell in data["Primary Fur Color"]:

    if squirrell == "Cinnamon":
        fur_color_dict["population"][fur_color_dict["colors"].index(
            "cinnamon")] += 1
    elif squirrell == "Gray":
        fur_color_dict["population"][fur_color_dict["colors"].index(
            "gray")] += 1
    elif squirrell == "Black":
        fur_color_dict["population"][fur_color_dict["colors"].index(
            "black")] += 1
    else:
        fur_color_dict["population"][fur_color_dict["colors"].index(
            "other")] += 1


fur_color_frame = pandas.DataFrame(fur_color_dict)

fur_color_frame.to_csv(
    "days 22-30/day025 CSV and Pandas/Squirrel Count.csv")
