#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Names of people
people = ['Farrah', 'Fred', 'Felicia']

# X locations for bars
x = np.arange(len(people))

# Plotting the stacked bars
apples = plt.bar(x, fruit[0], color='red', width=0.5, label='apples')
bananas = plt.bar(x, fruit[1], bottom=fruit[0], color='yellow', width=0.5, label='bananas')
oranges = plt.bar(x, fruit[2], bottom=fruit[0] + fruit[1], color='#ff8000', width=0.5, label='oranges')
peaches = plt.bar(x, fruit[3], bottom=fruit[0] + fruit[1] + fruit[2], color='#ffe5b4', width=0.5, label='peaches')

# Labels, legend, and title
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.xticks(x, people)
plt.yticks(np.arange(0, 81, 10))
plt.legend()

# Show the plot
plt.show()
