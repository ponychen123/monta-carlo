import numpy as np
import matplotlib.pyplot as plt

def calculate_probability(player1_choice, player2_choice):
    numwins = 0
    N = 10**4

    coin = np.array(["T", "H"])

    for i in range(N):
        three_gram = coin[np.random.randint(2, size=3)]
        three_gram_string = "".join(three_gram)
        if player2_choice == three_gram_string:
            numwins += 1
        elif player1_choice == three_gram_string:
            continue
        else:
            while True:
                three_gram[0:2] = three_gram[1:3]
                three_gram[2] = coin[np.random.randint(2)]
                three_gram_string = "".join(three_gram)
                if player2_choice == three_gram_string:
                    numwins += 1
                    break
                elif player1_choice == three_gram_string:
                    break
    return numwins/N

def penney():
    three_grams = np.array(['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH'])
    n = len(three_grams)
    p_array = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if j != i:
                p_array[i,j] = calculate_probability(three_grams[i],three_grams[j])

    fig, ax = plt.subplots()
    im = ax.imshow(p_array)

    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(three_grams)
    ax.set_yticklabels(three_grams)
    plt.setp(ax.get_xticklabels(), rotation=45,ha="right",rotation_mode="anchor")
    for i in range(n):
        for j in range(n):
            text = ax.text(i, j, p_array[i,j],
                    ha="center",va="center",color="w")
    ax.set_title("probabilities of penney game")
    fig.tight_layout()
    plt.show()
    

penney()
