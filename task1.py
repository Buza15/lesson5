from random import random
n = round(random() * 100)
i = 1
print("You have ten attempts to guess the result!")
while i <= 10:
    u = int(input(str(i) + ' attempt: '))
    if u > n:
        print('So much')
    elif u < n:
        print('So little')
    else:
        print('You\'ve guessed from %d attempt' % i)
        break
    i += 1
else:
    print('You have  axhausted the 10 attempts. The number was', n)


