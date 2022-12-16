# Determining the greater number
def num(a,b):
        if a > b:
                return(f'{a} is greater than {b}')
        elif a == b:
                return('Both are equal')
        return(f'{b} is greater than {a}')
a,b = input('Enter two numbers(comma separated): ').split(',')
print(num(a,b))

