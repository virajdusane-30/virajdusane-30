name = input("Enter your name ")
print("Welcome " + str(name) + " to the game")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Lets play: ")
score = 0

answer = input("CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect")
    
answer = input("WHO stands for? ")
if answer.lower() == "world health organization":
    print('Correct')
    score += 1
else:
    print("Incorrect")
    
answer = input("RAM stands for? ")
if answer.lower() =="random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect")
    
answer = input("ROM stands for? ")
if answer.lower() == "read only memory":
    print('Correct')
    score += 1
else:
    print("Incorrect")
    
answer = input("GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect")
    
answer = input("BIOS stands for? ")
if answer.lower() == "basic input output system":
    print('Correct')
    score += 1
    print("Hurrah!!")
else:
    print("Incorrect")

print("You got " + str(score) + " correct")
   