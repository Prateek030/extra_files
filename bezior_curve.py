import numpy as np
import matplotlib.pyplot as plt

def binomial_coefficient(n, k):
    """
    Calculate binomial coefficient C(n, k)
    """
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

def bezier(t, control_points):
    """
    Calculate a point on the Bezier curve at parameter t
    """
    n = len(control_points) - 1
    x, y = 0, 0
    for k in range(n+1):
        x += binomial_coefficient(n, k) * (1-t)**(n-k) * t**k * control_points[k][0]
        y += binomial_coefficient(n, k) * (1-t)**(n-k) * t**k * control_points[k][1]
    return x, y

def generate_bezier_curve(control_points, num_points=100):
    """
    Generate points on the Bezier curve
    """
    t_values = np.linspace(0, 1, num_points)
    curve_points = [bezier(t, control_points) for t in t_values]
    return list(zip(*curve_points))

def plot_bezier_curve(control_points, num_points=100, show=True):
    """
    Plot the Bezier curve
    """
    curve_x, curve_y = generate_bezier_curve(control_points, num_points)
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
