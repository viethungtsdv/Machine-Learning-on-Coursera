from matplotlib import pyplot as plt

def plotData(X, y):
# PLOTDATA Plots the data points x and y into a new figure
#   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
#   population and profit.

# ====================== YOUR CODE HERE ======================
# Instructions: Plot the training data into a figure using the
#               "figure" and "plot" commands. Set the axes labels using
#               the "xlabel" and "ylabel" commands. Assume the
#               population and revenue data have been passed in
#               as the x and y arguments of this function.
    plt.figure(1)

    plt.axes([0.2, 0.1, 0.5, 0.8])
    plt.scatter(X, y, color="red", marker='x', label = "Training data")

    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.title('Scatter plot of training data')

    #plt.show()

# ============================================================