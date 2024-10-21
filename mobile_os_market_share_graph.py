# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# Paste or type your script code here:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset_path = ".\\data\\mobile_os_market_share.csv"

# Read CSV file
df = pd.read_csv(dataset_path)
df = df.drop_duplicates()

data = df.items()

bar_width = 0.4

content_columns = []
labels = []

i = 0
for label, content in data:
    content_columns.append(content)

    if i != 0:
        labels.append(label)
    i += 1

# Set the figsize to prevent the labels from getting cut off
fig, ax = plt.subplots(layout='constrained', figsize=(12, 6))
ax.set_ylabel('Percentage')
ax.set_xlabel('Dates')
ax.set_title('Percentage of the Mobile Market Share')

colors = ['blue', 'orange', 'green', 'purple', 'brown']
handles = [plt.Rectangle((0,0),1,1, color=colors[i]) for i in range(len(colors))]

ax.legend(handles, labels)

# index of the dates of the bars
index = np.array(content_columns[0])

# Plot the data of each column (scan by column)
for i in range(len(content_columns)):
    if i == 0:
        continue

    ax.plot(index, content_columns[i])

# Show the plot
plt.show()