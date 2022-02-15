# Greedy Algorithm
# Richard Weaver
# 15/02/2022

coin = 0
deno_list = [0.25, 0.10, 0.05, 0.01]
coin_count = 0
coin_returned = 0

num = round(float(input("How much change is owed? -> ")),2)

# Greedy Algorithm

while num >= 0:
    for coin in deno_list:
        coin_count = round(num // coin, 2) #finding how many demonination go into input
        remainder = round(num % coin, 2) #finding remainder after highest denomination has been subtracted
        num = round(remainder, 2) #change num for next iteration in loop

        print(f"The current denomination is {coin}")
        print(f"The number of times denomination goes into num is {coin_count}")
        print(f"The remaining amount left over is {remainder}")
        
        coin_returned += 1 #counting number of loops... but needs to be number of times into!
    break
print (coin_returned)