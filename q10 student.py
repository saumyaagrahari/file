a=open("student_file.txt","w")
student=["saumya\n","sanjna\n","arti\n","sandhya\n","anshuman"]
for i in student:
    a.write(i)
a.close()



a=open("student_file.txt","r")
student=a.read()
print(student)
a.close()





