age = 15
'''if age<=45:
   print("you are an adult")


age = int(input("enter your age"))
 
if age<=12:
   print("you are a child")
elif age<=20:
   print("you are a teenage")
else:
    print("you are an adult")

score = int(input("enter your score"))

if score>=90:
   print("A")
elif score>=80:
   print("B")
elif score>=70:
   print("C")
else:
   print("F")'''

#nested if

x=input("enter u are male or female")
y = int(input("enter ur age"))
 
if x == "female":
   if y<=18:
      print("you are not eligible to vote")
   else:
      print("you are eligible")

else:
    print("you are a male")