import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def save_scatter_cycles_vs_time(csv, generate_for_poster):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    fig, ax = plt.subplots(figsize=(7, 5))
    color = "#49c3fb"
    whisker_props_color = 'black'

    if generate_for_poster:
        whisker_props_color = 'white'

    ax.scatter(csv['cpu time'], csv['number of cycles'], color=color)
    ax.set_xlabel('Time (s)', size=15, **font)
    ax.set_ylabel('Number of cycles', size=15, **font)
    ax.set_title("Influence of number of cycles in duplicates model on runtime", size=15, color='white', **font)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    if generate_for_poster:
        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # plt.show()
        plt.savefig('figures/poster/scatter_cycles_vs_time_poster.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/scatter_cycles_vs_time.svg')
