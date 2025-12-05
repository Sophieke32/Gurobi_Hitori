import matplotlib.pyplot as plt

def save_scatter_cycles_vs_time(csv):
    fig, ax = plt.subplots(figsize=(7, 5))

    zipped_values = list(zip(range(1, 14), range(14, 27)))
    # zipped_values = list(zip(csv4['number of cycles'], csv4['cpu time']))
    print(zipped_values)
    ax.scatter(csv['cpu time'], csv['number of cycles'], color='#49c3fb')
    ax.set_xlabel('Time (s)', size=15)
    ax.set_ylabel('Number of cycles', size=15)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # # Set axes colours to white
    ax.spines["bottom"].set_color("white")
    ax.spines['left'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # plt.show()
    plt.savefig('figures/scatter_cycles_vs_time.png', transparent=True)