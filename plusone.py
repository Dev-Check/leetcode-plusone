#66
digits = [9]
lastdigit = list[-1] #access last digit
digits[-1] = digits[-1] + 1  # increment digit
if digits == 10:
    list.remove(10)
    list.append(1)
    list.append(0)

print(digits)

