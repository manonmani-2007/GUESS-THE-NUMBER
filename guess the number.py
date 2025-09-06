print("hello! let's play a game:")
print("GUESS THE NUMBER!")
print("IT'S A NUMBER BETWEEN 1 TO 100! both inclusive")
print("HINT:1 IT IS THE SMALLEST NUMBER WITH SIX DIVISORS!!")
print("HINT:2 THIS NUMBER HAS RELIGIOUS SIGNIFICANCE!")
count=1
while True:
    a=int(input("enter a number: "))
    if a not in range(1,101):
        print("enter number between 1 and 100 please! both inclusive")
        continue
    elif 12<a:
        print("too high")
    elif 12>a:
        print("too low")
    else:
        print("you are correct")
        print("you have tried",count,"times")
        print("12 is the smallest number with 6 divisors...")
        print("12 has reigious significance for eg: 12 Olympian Gods in Greek Mythology,12 Apostles in Christianity...")
        break
    count=count+1

    
    
