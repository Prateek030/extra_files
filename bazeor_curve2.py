import numpy as np
from scipy.interpolate import CubicBezier, interp1d
import matplotlib.pyplot as plt

def plot_bezier_curve(control_points, num_points=100, show=True):
    t = np.linspace(0, 1, len(control_points))
    curve_x, curve_y = zip(*CubicBezier(t, control_points).transpose())
    control_x, control_y = zip(*control_points)

    plt.plot(curve_x, curve_y, label='Bezier Curve', color='blue')
    plt.scatter(control_x, control_y, label='Control Points', color='red')
    plt.title('Bezier Curve Interpolation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    if show:
        plt.show()

# Example usage:
# Specify your control points as a list of (x, y) coordinates
control_points = [(0, 0), (1, 3), (2, 1), (3, 4)]
plot_bezier_curve(control_points)
