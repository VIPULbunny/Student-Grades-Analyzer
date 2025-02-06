import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

# URL containing the JSON dataset
url = "https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/grades.json"

# Fetching data from the URL
req = requests.get(url)

# Parsing the content using BeautifulSoup
soup = BeautifulSoup(req.content, "html.parser")

# Reading JSON data into a Pandas DataFrame
df = pd.read_json(url, lines=True)

# Function to clean unwanted characters from the '_id' column
def clean_id(value):
    return re.sub(r"^{.*: '|'}", " ", value)

# Converting '_id' to string type and cleaning it
df['_id'] = df['_id'].astype(str).apply(clean_id)

# Converting relevant columns to string type
df['student_id'] = df['student_id'].astype(str)
df['class_id'] = df['class_id'].astype(str)
df['scores'] = df['scores'].astype(str)

# Display the DataFrame
print(df)

# Extracting individual scores (exam, quiz, homework) from the 'scores' column
# TODO: Process and extract score values into separate columns

# Columns expected:
# 1. _id
# 2. student_id
# 3. class_id
# 4. exam_score
# 5. quiz_score
# 6. homework_score
