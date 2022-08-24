#If Statement

grade1 = float (input("type your grade of the first test : "))
grade2 = float (input("type your grade of the seconf test : "))
absences = int (input("type the number of absences: "))
total_classes = int (input("type the total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) /total_classes
print("avarage grade:",round(avg_grade,2))
print("Attendace rate :",str(round((attendance *100),2))+'%')
if (avg_grade >= 6):
    if(attendance >= 0.8):
        print("the student has been approved next sem")
    else:
        print("the student has failed this sem due to attendace rate lower than 80%.")
elif(attendance >=0.8):
    print("the student has failed due to the avarage grade lower than 6.0")
else:
        print("the student has failed this sem due to an grade lower than 6.0 and attandace rate lower than 80 .")
        
