# student_heights = [180, 124, 165, 173, 189, 169, 146]

print("Please input a list of heights")
heights = input()
heights_num = heights.replace(",", "")

student_heights = heights_num.split()

sum = 0
length = 0

for height in student_heights:
    sum += int(height)
    length += 1

average_height = sum / length

print(round(average_height))
