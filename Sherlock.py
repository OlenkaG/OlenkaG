try:
    a = int(input( 'Enter the number: ' ))
except ValueError:
    print("invalid")

sum = 0


for digit in str(a):
    sum += int(digit)

print(sum)