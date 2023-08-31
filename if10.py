def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<=0:
        return "Freezing"
    if 1<=temp and 10>=temp:
        return "Very Cold"
    if 11<=temp and 20>=temp:
        return "Cold"
    if 21<=temp and 30>=temp:
        return "Normal"
    if 31<=temp and 40>=temp:
        return "Hot"
    if 40<temp:
        return "Very Hot"
print(main(15))