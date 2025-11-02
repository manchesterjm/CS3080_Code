"""
Subplot demonstration for sine wave visualization.

This module creates multiple subplots displaying sine waves with different frequencies.
It demonstrates the use of matplotlib for creating multi-panel visualizations.
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    """
    Create and display sine wave subplots with varying frequencies.

    Generates 6 subplots, each showing a sine wave with frequency 1x through 6x
    the base frequency over the interval [0, 2π].

    Returns:
        None
    """
    x_pts = np.linspace(0, 2 * np.pi)

    for i in range(1, 7):
        y_pts = np.sin(x_pts * i)
        plt.subplot(7, 1, i)
        plt.plot(x_pts, y_pts)

    plt.show()


if __name__ == '__main__':
    main()
