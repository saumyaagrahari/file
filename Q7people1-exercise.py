character = open("people1-exercise.txt","w")
character.write("rishabh - meerut") 
character.write("imtiyaz - delhi\n")
character.write("nilima - cochin\n")
character.write("rati - shimla\n")
character.write("ayishah - delhi\n")
character.write("raghu - shimla\n")
character.write(" naseer - kanpur\n")
character.write("karthikeyan - delhi\n")
character.write("salma - jaipur\n")
character.write("pankaj - delhi\n")
character.write("brijesh - delhi\n")
character.write("govind - delhi\n")
character.write("puneet - shimla\n")
character.write("siddhi - delhi\n")
character.write("suman - jaipur\n")
character.write("rajeev - shimla\n")
character.write(" mohinder - delhi\n")
character.write("rajendra - jaipur\n")
character.write("priyanka - shimla\n")
character.write("neela - delhi\n")
character.write("sashi - jaipur\n")
character.write("sarika - delhi\n")
character.write("deepti - shimla\n")
character.write("harshad - delhi\n")
character.write("trishna - raipur\n")
character.write("pradeep - jaipur\n")
character.write("sekhar - delhi\n")
character.write("nand - delhi\n")
character.write("anoop - delhi\n")
character.write("balwinder - tokyo")
character.close()

# character = open("people1-exercise.txt")
# file_data = character.read()
# print(file_data)
# character.close()

file = open("people1-exercise.txt","r")
for i in file:
    if "delhi" in i:
        a=open("delhi.txt","a")
    elif "shimla" in i:
        b=open("shimla.txt","a")
        b.write(i)
    else:
        c=open("other.txt","a")
        c.write(i)

# Iss text ko people1-exercise.txt ke naam ki file mein save karo.

# Ab apne code se iss file ko kholo aur fir, uske saare contents ko print karo.