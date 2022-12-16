num = input('Enter some numbers: ')
n = len(num)
total = int(num[0])
i = 1
while i < n:
        total = total + int(num[i])
        i += 1
print(total)
