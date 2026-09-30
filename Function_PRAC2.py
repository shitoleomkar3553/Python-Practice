# write a function to convert USD to INR

def cal_money(a, b=95.82):
    conversion = a * b

    print("USD to INR:",conversion)
    return conversion

cal_money(12)