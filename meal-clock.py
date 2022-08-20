def main():
    a = input("what is the time? ")
    time = convert(a)
    if 6.9 < time < 8.0:
        print("Breakfast time!")
    elif 11.9 < time < 14.0:
        print("lunch time!")
    elif 18.9 < time < 21.0:
        print("supper time!")
    else:
        print("Walk away from the fridge you greedy bastard!")

def convert(a):    
    b = a.split(":")
    hour = int(b[0])
    minute = int(b[1])
    c = minute/60
    d = hour+c
    return(d)
    
main()
