print ("Welcome!") 
g = input("Guess the number: ") 
guess = int(g) 
if guess == 5: 
    print("You win!") 
elif guess > 5: 
    print("Too high!") 
elif guess < 5: 
    print("Too small!") 
print("Game over!") 
