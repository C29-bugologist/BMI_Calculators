print("----------BMI----------\n\n")
print("Lets see What your BMI is:")
weight_kg = float(input("Enter your body Weight in KG : "))
height_meter = float(input("Enter your height in Meter : "))
BMI = weight_kg//(height_meter * height_meter)
if BMI in range(1,19):
    print("\n You Are UNDERWEIGHT", BMI)
if BMI in range(18,26):
    print("\n You Are Normal Relax", BMI)
if BMI in range(25,50):
    print("\n You Are OVERWEIGHT", BMI)