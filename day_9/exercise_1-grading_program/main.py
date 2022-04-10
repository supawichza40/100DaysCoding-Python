student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
def number_grade(number):
    if(number>=91 and number<=100):
        return "Outstanding"
    elif(number>=81 and number<=90):
        return "Exceeds Expectations"
    elif(number>=71 and number<=80):
        return "Acceptable"
    else:
        return "Fail"
    
for key,value in student_scores.items():
    student_grades.update({key:number_grade(value)})

# 🚨 Don't change the code below 👇
print(student_grades)