guess=input('please guess a number from 1 to 10'  )
guess=int(guess)
import random
number=random.randint(1,10)
print(number==guess)