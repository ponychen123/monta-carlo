import random

def craps():
    numwins = 0
    N = 10**5
    for i in range(N):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        diesum = die1 + die2

        if diesum == 7 or diesum == 11:
            numwins += 1
        elif diesum==2 or diesum == 3 or diesum == 12:
            continue
        else:
            while True:
                die1 = random.randint(1,6)
                die2 = random.randint(1,6)
                newdiesum = die1 + die2
                if newdiesum == diesum:
                    numwins += 1
                    break
                elif newdiesum == 7:
                    break

    p_exact = 244/495
    p_mc = numwins/N
    relative_error = abs((p_exact - p_mc)/p_exact)
    print("The exact probability of winning craps is %9.6f\n", p_exact)
    print("from %d simulations, we ge an approximate value of %9.6f\n", N, p_mc)
    print("The relative error of the approximate probability is %9.6f\n", relative_error)

craps()
