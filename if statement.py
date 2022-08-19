#If Statement

grade1 = float (input("type your grade of the first test : "))
grade2 = float (input("type your grade of the seconf test : "))
absences = int (input("type the number of absences: "))
total_classes = int (input("type the total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) /total_classes

if (avg_grade >= 6):
    if(attemdance >= .58):
        print("the tsudent has been approved next sem")
    else:
        print("the tsudent has failed this  sem")
else:
    print("the tsudent has failed ")
        
