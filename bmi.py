#!/usr/bin/env python3

def main():
    weight = get_float("Weight (kg): ")
    length = get_float("Length  (m): ")

    bmi = calculate_bmi(weight, length)

    print_bmi(bmi)
    print_category(bmi)

def get_float(text):
    """ We only want a float value """

    while True:
        try:
            float_value = float(input(text))
        except ValueError:
            print("Floats only")
            continue
        break

    return float_value

def calculate_bmi(weight, length):
    bmi = weight / (length * length)

    return bmi

def print_bmi(bmi):
    print("Your BMI is {0:2.1f}".format(bmi))

def print_category(bmi):
    if(bmi < 18.5):
        print("You are underweight")
    elif(18.5 <= bmi <= 24.9):
        print("You are of normal weight")
    elif(24.9 < bmi < 30):
        print("You are overweight")
    else:
        print("You are obese")

if __name__ == '__main__':
    main()
