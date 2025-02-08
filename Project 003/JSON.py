import requests  # For fetching data from the web
from bs4 import BeautifulSoup  # For parsing web content (not needed in this case)
import pandas as pd  # For handling and analyzing data
import numpy as np  # For numerical operations
import re  # For regular expressions (cleaning data)
import matplotlib.pyplot as plt  # For visualizations
import seaborn as sns  # For statistical data visualization

# ------------------- Step 1: Fetch JSON Data ------------------- #

# URL containing the JSON dataset
url = "https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/grades.json"

# Fetching data from the URL
req = requests.get(url)

# Reading JSON data into a Pandas DataFrame
df = pd.read_json(url, lines=True)

# ------------------- Step 2: Data Cleaning ------------------- #

# Function to clean unwanted characters from the '_id' column
def clean_id(value):
    return re.sub(r"^{.*: '|'}", " ", value)

# Converting '_id' to string type and cleaning it
df['_id'] = df['_id'].astype(str).apply(clean_id)

# Converting relevant columns to string type
df['student_id'] = df['student_id'].astype(str)
df['class_id'] = df['class_id'].astype(str)

# ------------------- Step 3: Extracting Scores ------------------- #

# The 'scores' column contains a list of dictionaries (exam, quiz, homework)
# We need to extract the 'score' values from this list

df['exam_score'] = df['scores'].apply(lambda x: x[0]['score'] if isinstance(x, list) else None)  # Extract exam score
df['quiz_score'] = df['scores'].apply(lambda x: x[1]['score'] if isinstance(x, list) else None)  # Extract quiz score
df['homework_score'] = df['scores'].apply(lambda x: x[2]['score'] if isinstance(x, list) else None)  # Extract homework score

# Dropping the 'scores' column as we have extracted the required data
df.drop(columns=['scores'], inplace=True)

# ------------------- Step 4: Display Cleaned Data ------------------- #

print(df.head())  # Display first few rows of cleaned data

# ------------------- Step 5: Data Visualization ------------------- #

# Setting up the style for plots
sns.set_style("whitegrid")

# Histogram of Exam Scores
plt.figure(figsize=(8, 5))
sns.histplot(df['exam_score'], bins=20, kde=True, color='blue')
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Exam Score vs Quiz Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['exam_score'], y=df['quiz_score'], color='red')
plt.title("Exam Score vs Quiz Score")
plt.xlabel("Exam Score")
plt.ylabel("Quiz Score")
plt.show()

# ------------------- Step 6: Statistical Insights ------------------- #

# Calculate the mean, median, and standard deviation for scores
stats_summary = df[['exam_score', 'quiz_score', 'homework_score']].describe()
print(stats_summary)

