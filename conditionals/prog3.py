#Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
mark = 900

if mark >=101  :
    print("Enter a valid mark")
    exit()

if mark >= 90:
    print("A  grade")
elif mark >= 80:
    print("B  grade")
elif mark >= 70:
    print("C  grade")
elif mark >=60:
    print("D  grade")
else:
    print("F  grade")