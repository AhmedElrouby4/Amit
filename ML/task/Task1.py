import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionGD:

    def __init__(self, learning_rate=0.001, n_iters=100):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.theta_0 = 0
        self.theta_1 = 0
        self.sse_history = []

    def fit(self, X, y):
        n = len(X)

        for _ in range(self.n_iters):

            y_pred = self.theta_0 + self.theta_1 * X

            error = y_pred - y

            d_theta_0 = (2/n) * np.sum(error)
            d_theta_1 = (2/n) * np.sum(error * X)

            self.theta_0 -= self.learning_rate * d_theta_0
            self.theta_1 -= self.learning_rate * d_theta_1

            sse = np.sum(error ** 2)
            self.sse_history.append(sse)

    def predict(self, X):
        return self.theta_0 + self.theta_1 * X

    def mse(self, X, y):
        y_pred = self.predict(X)
        return np.mean((y - y_pred) ** 2)

    def plot_training(self, X, y):

        # Plot SSE
        plt.figure()
        plt.plot(self.sse_history)
        plt.title("SSE over Iterations")
        plt.xlabel("Iterations")
        plt.ylabel("SSE")
        plt.show()

        # Plot Regression Line
        plt.figure()
        plt.scatter(X, y)
        y_pred_line = self.predict(X)
        plt.plot(X, y_pred_line)
        plt.title("Regression Line")
        plt.xlabel("House Size (m²)")
        plt.ylabel("Price (thousands)")
        plt.show()

# Data

X = np.array([50, 60, 70, 80, 90])
y = np.array([150, 180, 210, 240, 270])

# Train Model


model = LinearRegressionGD(learning_rate=0.001, n_iters=100)
model.fit(X, y)

print("theta_0 =", model.theta_0)
print("theta_1 =", model.theta_1)

# Prediction

prediction = model.predict(np.array([70]))
print("Predicted price for 70 m²:", prediction)

print("MSE:", model.mse(X, y))

# Visualization

model.plot_training(X, y)

# Experimentation

print("\n--- Large Learning Rate ---")
model_large_lr = LinearRegressionGD(learning_rate=1, n_iters=100)
model_large_lr.fit(X, y)
print("Final SSE:", model_large_lr.sse_history[-1])

print("\n--- Small Learning Rate ---")
model_small_lr = LinearRegressionGD(learning_rate=0.0000001, n_iters=100)
model_small_lr.fit(X, y)
print("Final SSE:", model_small_lr.sse_history[-1])