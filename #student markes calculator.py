#student grade calculator

hall_ticket=2606111786

hallticket=int(input("enter your hall ticket number ="))

if hallticket==hall_ticket:
    print("==please fill the below detailes ==")
else:
    print("please check your hall ticket number")    


telugu=int(input("enter telugu markes ="))
english=int(input("enter english markes ="))
maths=int(input("enter maths markes ="))

total=telugu+english+maths
print("total markes =",total)

print("----------student grades----------")
 
if telugu>=25:
    print("telugu ------> A+")
else:
    print("telugu ------> B")
if english>=30:
    print("english ------> A+")
else:
    print("english ------> B")
if maths>=30:
    print("math -----> A")
else:
    print("math ------> B")

print("==========student result==========")      

if total>=85:
    print("you are pass")
else:
    print("you are fail")

