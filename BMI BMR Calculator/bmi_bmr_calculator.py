def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero!"

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "\033[31mUnderweight\033[0m"
    elif 18.5 <= bmi < 24.9:
        return "\033[32mHealthy Weight\033[0m"
    elif 25 <= bmi < 29.9:
        return "\033[31mOverweight\033[0m"
    else:
        return "\033[31mObese\033[0m"
    
def calculate_bmr(weight, height, age):
    bmr = float((10*weight) + (625*height) - (5*age) + 5)
    return bmr

def main():
    # Input: Get weight and height from the user
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in cm): ")) / 100
        age = int(input("Enter your age (in yr): "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        bmr = calculate_bmr(weight, height, age)

        if isinstance(bmi, float) and isinstance(bmr, float):  # Check if BMI & BMR are valid float
            print("\n")
            print("*" * 70)
            print(f"\nYour Body Mass Index(BMI) is: \033[34m{bmi:.2f}\033[0m Kg/m\u00B2")
            print(f"Category: {get_bmi_category(bmi)}")
            print(f"Your Basal Metabolic Rate(BMR) is: \033[34m{bmr:.2f}\033[0m kcal/day.\n")
            print("*" * 70)
            print("\n")
        else:
            print(f"Invalid Inputs: {bmi}, {bmr}.\n")  # Error message for invalid height


    except ValueError:
        print("Please enter valid numerical values for weight and height!\n")

if __name__ == "__main__":
    main()