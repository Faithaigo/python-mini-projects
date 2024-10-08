import random


# print(random.randrange(-1, 10)) #Doesn't include the end number - upper bound range

# print(random.randint(-1, 10)) #includes the end number

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
      print("Please type a number larger than 0 next time.")
      quit() 
else:
    print("Please type a number  next time.")
    quit()

random_number = random.randint(0,top_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number  next time.")
        continue #goes back to the top of thhe loop
    
    if user_guess == random_number:
        print("Yay! You got it")
        break #stop the loop
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print ('You guessed',  guesses, 'times') #print multiple things in the same line 
