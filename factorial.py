nr1 = 5

factorial_nr1 = 5 *4 * 3 * 2 * 1
print(f" Die Fakultät von {nr1} ist {factorial_nr1}")

def factorial(randomNr):
    counter = randomNr
    result = randomNr
    while counter > 1:
        counter = counter - 1
        result = result * counter

    return result

def factorial_imroved(randomNr):
    if randomNr == 0:
        return 1
    return randomNr * factorial_imroved(randomNr - 1)


print(f"Die Fakultät mit Funktion von {nr1} ist {factorial(nr1)}")