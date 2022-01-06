
batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")
students_file.write("<html>\n")
students_file.write("<head>\n")
students_file.write("<title>NavGurukul Students</title>\n")
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<ul>")
for student in batch1_students:
    students_file.write("<li>" + student + "</li>\n")
students_file.write("</ul>\n")
students_file.write("</body>\n")
students_file.write("</html>\n")
students_file.close()



































# day=input("enter the day:")
# meal=input("enter the breakfast:")
# if day=="monday":
#     if meal=="breakfast":
#         print("poha")
#     elif meal== "lunch":
#         print ("Rajama chawal")
#     else:
#         print("Roti sabzi")
# elif day == "tuesday":
#     if meal == "breakfast":
#         print("poori sabzi")
#     elif meal == "lunch":
#         print("Thukapa")
#     else:
#         print("chicken chawal")
# else:
#     print("Aur kisi bhi din hum daal roti sabzi khaynege")
#     print("monday")


