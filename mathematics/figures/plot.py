from mplconfig import get_acsparameter
import matplotlib.pyplot as plt

def plot_permuting_figures():

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

        fig.savefig("permutation_arrow.pdf")

def plot_mapping_types():
    injective = {
        'left': "1 2 3".split(), 
        'right': "A B C D".split(),
        'edge': {
        "1": 'A',
        "2": 'B',
        "3": 'D' }
    }

    surjective = {
        'left': "1 2 3 4".split(), 
        'right': "A B C".split(),
        'edge': {
        "1": 'A',
        "2": 'B',
        "3": 'C',
        '4': 'C' }
    }

    bijective = {
        'left': "1 2 3 4".split(), 
        'right': "A B C D".split(),
        'edge': {
        "1": 'A',
        "2": 'B',
        "3": 'C',
        "4": 'D' }
    }
    
    with plt.rc_context(get_acsparameter(width = "double", n = 1, color = "line")):
        fig = plt.figure()
        axs = fig.subplots()
        
        axs.set_xlim(0, 16)
        axs.set_ylim(-1, 11)

        axs.text(2,9,'Injective', ha = 'center', va = 'bottom')
        axs.text(8,9,'Surjective', ha = 'center', va = 'bottom')
        axs.text(14,9,'Bijective', ha = 'center', va = 'bottom')
        
        y = [7,5,3,1]
        for i,data in enumerate([injective, surjective, bijective]):
            x1 = i * 6 + 1
            x2 = i * 6 + 3
            position = {}
            for j,label in enumerate(data["left"]):
                axs.text(x1, y[j], label, ha = 'right', va = 'center')
                position[label] = (x1, y[j])
            for j, label in enumerate(data['right']):
                axs.text(x2, y[j], label, ha = 'left', va = 'center')
                position[label] = (x2, y[j])

            print(position)

            for f,t in data['edge'].items():
                x0 = position[f]
                x1 = position[t]
                x0 = (x0[0]+0.2, x0[1])
                x1 = (x1[0]-0.2, x1[1])
                diff = (x1[0]-x0[0], x1[1]-x0[1])
                axs.arrow(x0[0], x0[1], diff[0], diff[1], head_width = 0.1, head_length = 0.1, length_includes_head=True)

            

        fig.savefig("mapping.pdf")

plot_mapping_types()