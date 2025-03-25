import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

year = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
unemployment_rate = [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]

plt.plot(year, unemployment_rate)
plt.title('unemployment rate vs year')
plt.xlabel('year')
plt.ylabel('unemployment rate')
plt.show()

import seaborn as sns
df = sns.load_dataset('tips')
print(df.head())

# Prepare df for plotting
total_bill = df['total_bill']
tip = df['tip']
sex = df['sex']
smoker = df['smoker']

# Create a scatter plot
plt.figure(figsize=(10, 6))
colors = {'Male': 'blue', 'Female': 'red'}
smoker_markers = {'Yes': 'x', 'No': 'o'}

for i in range(len(total_bill)):
    plt.scatter(total_bill[i], tip[i], c=colors[sex[i]], marker=smoker_markers[smoker[i]], s=100)

# Set plot labels and title
plt.xlabel('Amount Due')
plt.ylabel('Gratuity')
plt.title('Scatter Plot of Amount Due vs. Gratuity')

# Add legend for gender and smoker status
for gender_label, color in colors.items():
    plt.scatter([], [], c=color, label=gender_label)
for smoker_label, marker in smoker_markers.items():
    plt.scatter([], [], marker=marker, label='Smoker: ' + smoker_label)

plt.legend(loc='upper right')

plt.grid(True)
plt.show()

# Group the data by 'day' and calculate the average 'total_bill' for each day
average_total_bill_by_day = df.groupby('day')['total_bill'].mean()

# Create the bar plot
plt.bar(average_total_bill_by_day.index, average_total_bill_by_day.values)
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill')
plt.title('Average Total Bill by Day of the Week')
plt.show()

# Group the data by 'sex' and calculate the total count for each category
sex_counts = df['sex'].value_counts()

# Create the pie plot
plt.figure(figsize=(6, 6))
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Sex')
plt.axis('equal')  # Equal aspect ratio ensures that the pie plot is circular.
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['total_bill'], kde=True)
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Total Bill Histogram')
plt.show()



plt.figure(figsize=(8, 6))
# Assuming 'total_bill' and 'tip' are numerical columns in your DataFrame
sns.boxplot(data=df[['total_bill', 'tip']])
plt.title('Box Plot')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='day', y='total_bill', hue='sex', data=df, split=True, palette='muted')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Total Bill Distribution by Day and Sex')
plt.legend(title='Sex', loc='upper right')
plt.show()

plt.figure(figsize=(8, 6))
# Assuming 'total_bill' and 'tip' are your intended columns
sns.stripplot(data=df, x='day', y='total_bill', jitter=True)
plt.title('Strip Plot')
plt.show()


sns.pairplot(df, hue='sex') # Change 'D' to a valid column like 'sex' or 'smoker' if intended for color differentiation.
plt.title('Pair Plot')
plt.show()

# Distribution Plot
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='total_bill', kde=True)
plt.title('Distribution Plot')
plt.show()


# Count Plot
plt.figure(figsize=(8, 6))
# Replace 'D' with an actual column name from your DataFrame 'df', such as 'day', 'time', 'sex', 'smoker', 'size'
sns.countplot(data=df, x='sex') # Example: using 'sex' column
plt.title('Count Plot')
plt.show()

# Heatmap
corr = df.select_dtypes(include=np.number).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heat Map')
plt.show()