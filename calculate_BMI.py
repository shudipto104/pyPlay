# Body mass index (BMI) is a value derived from the mass (weight) and  height of a person. the BMI is defined as the boidy mass de=ivided by the sqaure of the body height, and universally espressed in unites of kg/m2. What is the programe which is aska for the length and the weight of a person and return the BMI with category.

lenght = input("enter the length in metres: ")
weight = input("enter the mass in kgs: ")
lenght = float(lenght)
weight = float(weight)
BMI = weight/(lenght * lenght)
print("Your BMI is: ",BMI)
BMI = float(BMI)
if BMI > 0 and BMI <= 15:
    print("Very severely underweight.")
elif BMI > 15 and BMI <= 16:
    print("Severely underweight.")
elif BMI > 16 and BMI <= 18.5:
    print("Underweight.")
elif BMI > 18.5 and BMI <= 25:
    print("Normal.")
elif BMI > 25 and BMI <= 30:
    print("Overweight.")
elif BMI > 30 and BMI <= 35:
    print("obese class 1.")
elif BMI > 35 and BMI <= 40:
    print("obese class 2.")
elif BMI > 40 and BMI <= 45:
    print("obese class 3.")
elif BMI > 45 and BMI <= 50:
    print("obese class 4")
elif BMI > 50 and BMI <= 60:
    print("obese class 5")
else:
    print("Obese class 6")