import matplotlib.pyplot as plt


# Generates a boxplot of the given data. Does not show the boxplot, this has to be done with plt.show()
def show_boxplot(data):
    plt.boxplot(data)
    plt.title('CPU_time (s)')