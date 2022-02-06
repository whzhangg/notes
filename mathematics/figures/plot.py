from mplconfig import get_acsparameter
import matplotlib.pyplot as plt

def get_permutation_arrows(n: int, permutations: list):
    result = { i+1:i+1 for i in range(n) }
    for permutation in permutations:
        for step in range(len(permutation))[::-1]:
            result[int(permutation[step])] = int(permutation[step-1])

    return result

with plt.rc_context(get_acsparameter(width = "single", n = 1, color = "line")):
    data = get_permutation_arrows(5, ['153','24'])
    fig = plt.figure()
    axs = fig.subplots()
    ratio = 1.0
    ydistance = ratio
    small_space = 0.1
    for key,value in data.items():
        axs.text(key*ratio, ydistance, str(key), ha = 'center', va = 'bottom', size = 10)
        axs.text(value*ratio, 0, str(key), ha = 'center', va = 'top', size = 10)
        axs.arrow(key*ratio, ydistance - small_space*ratio, (value-key)*ratio, -ydistance + small_space*ratio*2, head_width = 0.05, length_includes_head=True)

    axs.set_xlim(0, 6)
    axs.set_ylim(-1, 2)

    fig.savefig("try1.pdf")
