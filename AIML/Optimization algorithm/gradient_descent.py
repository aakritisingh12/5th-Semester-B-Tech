# # function is (x + 5)^2
# x = -3
# learning_rate = 0.01
# precesion = 0.00001
# iters = 0  # iteration counter
# # differenciation of function will be 2(x+5)
# while True:
#     dybydx = 2 * (x + 5)
#     x1 = x - learning_rate * dybydx
#     if x - x1 <= precesion:
#         break
#     x = x1
#     iters = iters + 1  # iteration count
#     print("Iteration", iters, "\nX value is", x)  # Print iterations
#
# print("The local minimum occurs at", x)

# # Gradient descent in Python
#
# # Step 1 : Initialize parameters
#
# cur_x = -3  # The algorithm starts at x=-3
# rate = 0.01  # Learning rate
# precision = 0.000001  # This tells us when to stop the algorithm
# previous_step_size = 1  #
# # max_iters = 10000  # maximum number of iterations
# # iters = 0  # iteration counter
# # df = lambda x: 2 * (x + 5)  # Gradient of our function
# #
# # # Step 2 : Run a loop to perform gradient descent
# #
# # while previous_step_size > precision and iters < max_iters:
# #     prev_x = cur_x  # Store current x value in prev_x
# #     cur_x = cur_x - rate * df(prev_x)  # Grad descent
# #     previous_step_size = abs(cur_x - prev_x)  # Change in x
# #     iters = iters + 1  # iteration count
# #     print("Iteration", iters, "\nX value is", cur_x)  # Print iterations
# #
# # print("The local minimum occurs at", cur_x)


# data = {1: 3, 2: 4}
# c = 0
# m = 2
# alfha = 0.001
# precision = 0.01
#
# while True:
#     derivative_cost_function0 = 0
#     derivative_cost_function1 = 0
#     ln = len(data)
#     for x in data:
#         y = c + m * x
#         derivative_cost_function0 += (1 / ln) * (y - data[x])
#         derivative_cost_function1 += (1 / ln) * (y - data[x]) * x
#     temp0 = c - alfha * derivative_cost_function0
#     temp1 = m - alfha * derivative_cost_function1
#     if temp1 == m and temp0 == c:
#         break
#     c = temp0
#     m = temp1
#     print("c = ", c)
#     print("m = ", m)
#
# print("y intersect is ", c, "slope is  ", m)
#
#
# import numpy as np
#
#
# def Gradient_descent(x, y):
#     slope = const = 0
#     iterations = 100000
#     n = len(x)
#     rate_of_learning = 0.01
#     for i in range(iterations):
#         pred_y = slope * x + const
#         # cost = (1/n) * sum([val ** 2 for val in (y - pred_y)])
#         D_slope = -(2 / n) * sum(x * (y - pred_y))
#         D_Const = -(2 / n) * sum(y - pred_y)
#         slope = slope - rate_of_learning * D_slope
#         const = const - rate_of_learning * D_Const
#         print("Slope = {}, Constant = {}, iterations = {}".format(slope, const, i))
#
#
# x = np.array([1, 3])
# y = np.array([5, 7])
# Gradient_descent(x, y)


import numpy as np

data_x = np.linspace(1.0, 10.0, 100)[:, np.newaxis]
data_y = np.sin(data_x) + 0.1 * np.power(data_x, 2) + 0.5 * np.random.randn(100, 1)
data_x /= np.max(data_x)
data_x = np.hstack((np.ones_like(data_x), data_x))
order = np.random.permutation(len(data_x))
portion = 20
test_x = data_x[order[:portion]]
test_y = data_y[order[:portion]]
train_x = data_x[order[portion:]]
train_y = data_y[order[portion:]]


def gradient(w, x, y):
    y_estimate = x.dot(w).flatten()
    error = (y.flatten() - y_estimate)
    gradient = -(1.0 / len(x)) * error.dot(x)
    return gradient, np.power(error, 2)


w = np.random.randn(2)
alpha = 0.5
tolerance = 1e-5

iterations = 1
while True:
    gradient, error = gradient(w, train_x, train_y)
    new_w = w - alpha * gradient

    if np.sum(abs(new_w - w)) < tolerance:
        print("Converged.")
        break

    if iterations % 100 == 0:
        print("Iteration: %d - Error: %.4f" % (iterations, error))

    iterations += 1
    w = new_w