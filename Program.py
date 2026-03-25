name = input("Enter your name: ")

marks = []
total = 0

for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)
    total += m

average = total / 5

print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
