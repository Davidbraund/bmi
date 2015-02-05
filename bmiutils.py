def bmi_float(val):
    try:
        return float(val)
    except:
        return 0.0


def bmi(length, weight):
    l = bmi_float(length)
    w = bmi_float(weight)

    return (w / (l * l))


def bmi_verdict(bmi):
    if(bmi < 18.5):
        verdict = "You are underweight"
    elif(18.5 <= bmi <= 24.9):
        verdict = "You are of normal weight"
    elif(24.9 < bmi < 30):
        verdict = "You are overweight"
    else:
        verdict = "You are obese"

    return verdict
