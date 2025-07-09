import random
cards = [10,10,10,1,2,3,4,5,6,7,8,9,10]

def main():
    while True:
        feedback = input("Do you want to play BLACK JACK? (y / n)\n").lower()
        if feedback == "y":
            p1 , c = game_strt()
            ss = score(p1)
            if ss == 21:
                print("BLACK JACK")
                continue
        else:
            quit()

        check , p , co = hit_or_stand(p1,c)
        n1 = score(p)
        if check == 0:
            print("Bust")
            print(f"CURRENT SCORE - {n1}")
            print("you lose!")
            continue
        elif check == 1:
            print("BLACK JACK")
            continue
        elif check == 2:
            cp = comp_turn(co)

        game_end(p,cp)

def game_strt():
    global cards
    n = 0
    p1 = random.choices(cards , k =2)
    comp = random.choices(cards , k =1)

    if 1 in p1:
        p1 = ace(p1)

    n = score(p1)
    print(f"Player - {p1}    Current score - {n} ")
    print(f"Dealer - {comp}")
    return p1 , comp

def hit_or_stand(p1 , comp):
    global cards
    while True:
        choice = input("Type 'h' for HIT or 's' for STAND: ").lower()
        if choice == "h":
            p1.append(random.choice(cards))
            print(f"{p1}    CURRENT SCORE: {score(p1)}")
            if score(p1) > 21:
                return 0 , p1 , comp
            elif score(p1) == 21:
                return 1 , p1 , comp
        else:
            return 2 , p1 , comp
        
def comp_turn(co):
    global cards
    face_down = random.choice(cards)
    co.append(face_down)
    print(f"Dealer - {co}" )
    t = score(co)
    while t < 17:
        new = random.choice(cards)
        co.append(new)
        t =score(co)
        print(co)
        if t > 21:
            print("Dealer Busted")
            break
    return co
        
def ace(l):
    for i in range(len(l)):
        if l[i] == 1:
            choose = int(input("You got ACE. Pick a value '1' or '11'"))
            if choose == 11:
                l[i] = 11
            elif choose == 1:
                l[i] = 1
            else:
                return l
    return l


def score(l):
    total = 0
    for num in l:
        total += num
    return total

def game_end(p , cp):
    s1 = score(p)
    s2 = score(cp)
    p1 = 21 - s1
    c1 = 21 - s2
    if c1 < 0:
        print(f"You won!")
        print(f"PLAYER = {s1}   DEALER = {s2}")
    else:
        if p1 < c1:
            print("You won")
            print(f"PLAYER = {s1}   DEALER = {s2}")
        elif p1 > c1:
            print("Dealer won")
            print(f"PLAYER = {s1}   DEALER = {s2}")
        else:
            print("TIE")
            print(f"PLAYER = {s1}     DEALER = {s2}")


if __name__ == "__main__":
    main()


