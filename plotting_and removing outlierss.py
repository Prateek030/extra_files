import matplotlib.pyplot as plt
import numpy as np

def plot_circle(ax, center, radius):
    circle = plt.Circle(center, radius, edgecolor='r', facecolor='none', linestyle='dotted')
    ax.add_patch(circle)

def update_plot(ax, points):
    ax.clear()
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    if points.any():
        mean_point = np.mean(points, axis=0)
        plot_circle(ax, mean_point, 5)

        # Plot points within the circle
        inside_points = points[np.linalg.norm(points - mean_point, axis=1) <= 5]
        ax.scatter(inside_points[:, 0], inside_points[:, 1], color='b', label='Points Inside Circle')

        # Plot points outside the circle
        outside_points = points[np.linalg.norm(points - mean_point, axis=1) > 5]
        ax.scatter(outside_points[:, 0], outside_points[:, 1], color='r', label='Points Outside Circle')

        ax.legend()
    else:
        ax.set_title('No points provided yet.')

    plt.draw()
    plt.pause(0.01)

def main():
    # Default points
    #default_points = np.array([(1, 2), (3, 4), (5, 6), (-2, -3), (-5, 4)])

    fig, ax = plt.subplots()
    default_points = np.array([])
    for i in range(10):
              x,y = list(map(int,input('enter x y:').split()))
              if len(default_points)==0:
                    default_points = np.array([[x,y]])

              else:
                    np.insert(default_points,np.array([x,y]))
              
              # Update plot with default points
              update_plot(ax, default_points)

              plt.show()

if __name__ == "__main__":
    main()
