import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style
sns.set(style="ticks")

# Load dataset
weather = pd.read_csv('Test.csv')

# Display first few rows
print(weather.head())

# Get dataset information
print(weather.info())

# Create barplot
sns.barplot(x=weather['humidity'], y=weather['temperature'])

# Create distribution plot
sns.distplot(weather['humidity'])
plt.show()

# Create distribution plot without KDE and with rug
sns.distplot(weather['humidity'], kde=False, rug=True)
plt.show()

# Create joint plot
sns.jointplot(x=weather['humidity'], y=weather['temperature'])
plt.show()

# Create hex joint plot
sns.jointplot(x=weather['humidity'], y=weather['temperature'], kind="hex")
plt.show()

# Create KDE joint plot
sns.jointplot(x=weather['humidity'], y=weather['temperature'], kind="kde")
plt.show()

# Create pairplot for selected columns
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()

# Create stripplot
sns.stripplot(x=weather['weather_type'], y=weather['temperature'])
plt.show()

# Create stripplot with jitter
sns.stripplot(x=weather['weather_type'], y=weather['temperature'], jitter=True)
plt.show()

# Create swarmplot
sns.swarmplot(x=weather['humidity'], y=weather['temperature'])
plt.show()

# Create barplot with hue
sns.barplot(x=weather['humidity'], y=weather['temperature'], hue=weather['weather_type'])
plt.show()

# Create countplot
sns.countplot(x=weather['weather_type'])
plt.show()

# Create pointplot with hue
sns.pointplot(x=weather['humidity'], y=weather['temperature'], hue=weather['weather_type'])
plt.show()