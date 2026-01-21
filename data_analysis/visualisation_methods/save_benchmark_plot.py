import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

from data_analysis.retrieve_data import benchmark_files


def save_benchmark_plot(generate_for_poster):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    fig, ax = plt.subplots(figsize=(6, 5))


    sizes = np.unique(benchmark_files['asp']['n'])

    asp = []
    gurobi = []
    prolog = []
    pumpkin = []
    z3 = []
    for i in sizes:
        asp.append(np.mean(benchmark_files['asp'][benchmark_files['asp']['n'] == i]['cpu time']))
        gurobi.append(np.mean(benchmark_files['gurobi'][benchmark_files['gurobi']['n'] == i]['cpu time']))
        prolog.append(np.mean(benchmark_files['prolog'][benchmark_files['prolog']['n'] == i]['cpu time']))
        pumpkin.append(np.mean(benchmark_files['pumpkin'][benchmark_files['pumpkin']['n'] == i]['cpu time']))
        z3.append(np.mean(benchmark_files['z3'][benchmark_files['z3']['n'] == i]['cpu time']))


    ax.plot(sizes, gurobi, label="ILP", color='#49c3fb')
    ax.plot(sizes, asp, label="ASP", color='red', linestyle='dashed')
    ax.plot(sizes, prolog, label="LP", color='#8c52ff', linestyle='dashdot')
    ax.plot(sizes, pumpkin, label="CSP", color='#479643', linestyle=(0, (1, 5)))
    ax.plot(sizes, z3, label="SMT", color='#e0911a', linestyle=(0, (1, 1)))

    ax.set_ylabel('Mean solving time (s)', size=15, **font)
    ax.set_xlabel('Instance size', size=15, **font)

    # Create legend and set its, and the ticks' font
    ax.legend(prop=font_manager)
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    ax.tick_params(axis='both', labelsize=15)

    # Only show ticks on the left and bottom spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    # ax.spines["bottom"].set_bounds(5, 10)
    # ax.spines["left"].set_bounds(0, 0.48)

    if generate_for_poster:
        # Set title
        ax.set_title("Solving time of five models", size=15, color='white', **font)

        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # plt.show()
        plt.savefig('figures/poster/graph_benchmark.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/graph_benchmark.svg')