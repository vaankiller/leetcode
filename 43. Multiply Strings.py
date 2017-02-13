__author__ = 'vaan'


def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product)-1

    for n1 in reversed(num1):
        tempPos = pos
        for n2 in reversed(num2):
            product[tempPos] += int(n1) * int(n2)
            product[tempPos-1] += product[tempPos]/10
            product[tempPos] %= 10
            tempPos -= 1
        pos -= 1

    pt = 0
    while pt < len(product)-1 and product[pt] == 0:
        pt += 1

    return ''.join(map(str, product[pt:]))