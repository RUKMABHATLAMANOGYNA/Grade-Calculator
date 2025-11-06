# Problem 2:
m = int(input("Marks in Math: "))
s = int(input("Marks in Science: "))
e = int(input("Marks in English: "))
Total_marks = m + s + e
Average_marks = Total_marks / 3
percentage = (Total_marks / 300) * 100
grade = ""
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <= 90:
    grade = "B"
elif percentage > 70 and percentage <= 80:
    grade = "C"
else:
    grade = "P"
print(f"Total Marks: {Total_marks}\nAverage Marks: {Average_marks}\nGrade: {grade}")
