row0 = ["0", " 1", " 2", " 3 "]
row1 = ["1", "⬜️", "⬜️", "⬜️"]
row2 = ["2", "⬜️", "⬜️", "⬜️"]
row3 = ["3", "⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row0}\n{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
row_final = f"row{int(position[0])}"
column_final = int(position[1])

if row_final == "row1":
    row1[column_final] = " X"
elif row_final == "row2":
    row2[column_final] = " X"
elif row_final == "row3":
    row3[column_final] = " X"

print(f"{row0}\n{row1}\n{row2}\n{row3}")
