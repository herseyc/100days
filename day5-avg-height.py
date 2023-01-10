# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
num_students = 0
total_height = 0
for student in student_heights:
    num_students += 1
    total_height += student

#calculate average
avg_height = round(total_height / num_students)

print(avg_height)


#easy way sum() len()
average_height = round(sum(student_heights) / len(student_heights))
print(average_height)
