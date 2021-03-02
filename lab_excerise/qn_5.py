# A school decided to replace the desks in the three classrooms. each desk sits two students .
#given the number of students in each class, print the smallest possible number of desks that can be purchased
#the program should read three integers: the number of students in each of the three class a, b and c
#in the first test there are three groups. the first group has 20 students and thus needs 10 desks
#the second group has 21 students  so they can get by with no fewer than 11 desks.
# 11 desks are enough are also enough for the third 22 students,so we need 32 desks in total
no_student_class1=int(input("Enter the number of students in first class:"))
no_students_class2=int(input("Enter the number of students in second class:"))
no_students_class3=int(input("Enter the number of students in third class:"))
#for exact students
desk_class1=(no_student_class1//2)
print(f"the number of desk in first class is :{desk_class1}")
desk_class2=(no_students_class2//2)
print(f"the number of desk in second class is:{desk_class2}")
desk_class3=(no_students_class3//2)
print(f"the number of desk in third class is:{desk_class3}")
#for remaining student
remaining_student_in_first_class=(no_student_class1%2)
print(f"the remaining student in first class:{remaining_student_in_first_class}")
remaining_student_in_second_class=(no_students_class2%2)
print(f"The remaining student in second class: {remaining_student_in_second_class}")
remaining_student_in_third_class=(no_students_class3%2)
print(f"the remaining number of student in third class: {remaining_student_in_third_class}")
#for total desk in school
total_desk_in_school=desk_class3+desk_class1+desk_class2+remaining_student_in_third_class+remaining_student_in_second_class+remaining_student_in_first_class
print(f"the total number of desk that the school should brought is :{total_desk_in_school} ")