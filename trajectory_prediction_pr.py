import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

def predict_future_trajectory(past_trajectory, timestamps, future_timestamps):
    timestamps_in_seconds = [(timestamp - timestamps[0]).total_seconds() for timestamp in timestamps]

    degree = 2  # Adjust the polynomial degree as needed
    polynomial_features = PolynomialFeatures(degree=degree)
    X_poly = polynomial_features.fit_transform(np.array(timestamps_in_seconds).reshape(-1, 1))
    model = LinearRegression()
    model.fit(X_poly, past_trajectory)

    future_timestamps_in_seconds = [(timestamp - timestamps[0]).total_seconds() for timestamp in future_timestamps]
    future_trajectory = model.predict(polynomial_features.transform(np.array(future_timestamps_in_seconds).reshape(-1, 1)))

    return future_trajectory

# Example usage
past_trajectory = np.array([[1, 2], [2, 4], [3, 9], [4, 16]])  # Replace with your actual past trajectory data
timestamps = [datetime(2024, 1, 1, 0, i) for i in range(4)]  # Replace with corresponding timestamps

# Define the number of future points to predict (n)
n = 15

# Generate future timestamps
last_timestamp = timestamps[-1]
future_timestamps = [last_timestamp + timedelta(minutes=i) for i in range(1, n + 1)]

# Call the function to predict future trajectory
predicted_trajectory = predict_future_trajectory(past_trajectory, timestamps, future_timestamps)

# Display the results
for i, timestamp in enumerate(future_timestamps):
    print(f'Prediction at time {timestamp}: {predicted_trajectory[i]}')

# Visualization of past trajectory and predicted future points
plt.scatter(timestamps, past_trajectory[:, 1], label='Past Trajectory')
plt.scatter(future_timestamps, predicted_trajectory[:, 1], color='red', marker='x', label='Predicted Future Points')
plt.xlabel('Time')
plt.ylabel('Y Trajectory')
plt.legend()
plt.show()
