from random import randint

n = randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number... :"))

    if(a>n):
        print("guess the lower number!")
        guesses +=1

    elif(a<n):
        print("guess the higher number!")
        guesses +=1

print(f"Congrats u guessed the number {n} in {guesses} guesses!!")

if(guesses <= 5):
    print("Your rank is : God")
    print(f"Arent you cheating? {guesses} guesses is crazzy ")
elif(guesses <= 10):
    print("Your rank is : pro")
    print("damn you are good")
elif(guesses <= 15):
    print("Your rank is : Pro")
    print("Neverming Get better!")
elif(guesses <= 20):
    print("Your rank is : Pro")
    print("Arent you granny are you ?")

#hiscore fetch programme

with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0

if(hiscore == 0 or guesses < hiscore):
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
        hiscore = guesses

print(f"Your current hiscore is {hiscore} guesses only!")
