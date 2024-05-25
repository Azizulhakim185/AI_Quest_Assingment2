user_input = input("Input the parchentage :")
x = int(user_input);
if x>= 80 :
    print("The grade is A+");
elif x<80 and x>=75 :
    print("The grade is A");
elif x<75 and x>=70 :
    print("The grade is A-");
elif x<70 and x>=65 :
    print("The grade is B+");
elif x<65 and x>=60 :
    print("The grade is B");
elif x<60 and x>=55 :
    print("The grade is c+");
elif x<55 and x>=50 :
    print("The grade is c-");
elif x<50 and x>=45 :
    print("The grade is D+");
elif x<45 and x>=40 :
    print("The grade is D");
else:
    print("The grade is F")