n1 = int(input())
n2 = int(input())
operator = str(input())

if n2 == 0 and (operator == '/' or operator == '%'):
    print(f"Cannot divide {n1} by zero")
elif operator == '+' or operator == '-' or operator == "*":
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    if result % 2 == 0:
        even_or_odd = "even"
    elif result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")
elif operator == '/':
    print(f"{n1} / {n2} = {(n1 / n2):.02f}")
elif operator == '%':
    print(f"{n1} % {n2} = {n1 % n2}")