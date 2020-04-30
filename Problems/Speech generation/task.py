digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers = input()
for char in numbers:
    print(digits[int(char)])
    #print(char)
    #print(int(char) in digits)
