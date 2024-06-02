import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_decibel_range(file_path):
    # Your plotting code here
    plt.figure(figsize=(5, 3))
    # Example plot for demonstration
    plt.plot([0, 1, 2, 3], [10, 20, 10, 30])
    plot_path = 'decibel_range.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path
