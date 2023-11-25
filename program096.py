from  random import randint
from  random import shuffle

number = randint(1,10)
print(number)

coin = ["heads","tails"]
shuffle(coin)
for i in coin:
    print(i)