def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    k=0
    if a<0:
        k=k+1
    if b<0:
        k=k+1
    if c<0:
        k=k+1
    if k>1:
        return "there are a lot of negative numbers"
    if k<2:
        return "there are a lot of positive numbers"
print(main(1,2,-8))
