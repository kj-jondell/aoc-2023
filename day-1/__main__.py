import sys, re

part = 2

sum = 0
### PART 1
if part == 1:
    for line in sys.stdin: 
        digits = [char for char in line if char.isdigit()]
        sum += int(f"{digits[0]}{digits[-1]}")

### PART 2
elif part == 2:
    names_of_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in sys.stdin: 
        digits = []
        for num, name in enumerate(names_of_digits):
            try:
                digits += [(str(num), match.start()) for match in re.finditer(name, line)]
            except:
                pass
        digits += [(char, index) for index, char in enumerate(line) if char.isdigit()]
        digits = sorted(digits, key=lambda tup: tup[1])
        sum += int(f"{digits[0][0]}{digits[-1][0]}")
        print(line.strip(), f"{digits[0][0]}{digits[-1][0]}")

print(f"The sum of all of the calibration values is: {sum}")