# name_file=open("names_address.txt","w")
# name_file.write("saumya_lucknow\narav_reabareli\nfatima_prayag_raj\ndivya_pune\nsanjna_mp")
# name_file.close()



# name_file=open("names_address.txt","r")
# address=name_file.read()
# print(address)
# name_file.close()





# i=0
# while i < 5:
#     print(i,end=" ")
#     i+=1
#     if i ==3:
#         break
# else:
#     print(0)

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# i=4
# j=0
# while i<len(a):
#     if j==0:
#         a[i]=15
#         j=1
#     else:
#         a[i]=20
#         j=0
#     i+=5
# print(a)


# tuple_A = ('Name = John Cleverly','Grade = Grade 2','ID = 123', 'Section = B')
# list_B  = ['Milk','Butter', 'Dessert', 'Ice cream']

# print('Tuple data is : ', tuple_A)
# print('List data is : ', list_B)

# print('size of a tuple is : ',tuple_A.__sizeof__())
# print('size of a list is : ',list_B.__sizeof__())

a={"apple","banana","cherry"}
# i=0
# while i in (a):
#     print(i)
#     i=i+1
for i in a:
    print(i)