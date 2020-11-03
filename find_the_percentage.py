"""
    Author: Frank Olson

    Finding the percentage
    You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
    The marks can be floating values. The user enters some integer N followedby the names and marks for N students.
    You are required to save the record in a dictionary data type. The user then enters a student's name.
    Output the average percentage marks obtained by that student, correct to two decimal places.
    
    Input Format:
        The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space.
        The final line contains the name of a particularstudent previously listed.
    
    Constraints:
        2 <= N <= 10
        0 <= Marks <= 100
    
    Output Format:
        Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
"""
n = 10
student_marks = {
    "Tom":65,
    "Dick":75,
    "Harry":95,
    "Bob":45,
    "Sue":96,
    "Mary":88.3
}
print(round((sum(student_marks.values())) / (len(student_marks.values())), 2))