## **Student Grades Data Analysis Using JSON**  

### **📌 Project Description**  
This project analyzes student grades using a dataset stored in JSON format. The dataset includes:  
- **Student ID**
- **Class ID**
- **Exam Scores**
- **Quiz Scores**
- **Homework Scores**  

The objective is to extract, clean, and analyze this data using **Python, Pandas, and Matplotlib/Seaborn** for visualization.  

---

## **📂 Table of Contents**  
- [Project Description](#-project-description)  
- [Technologies Used](#-technologies-used)  
- [Dataset Overview](#-dataset-overview)  
- [Project Workflow](#-project-workflow)  
- [Installation & Setup](#-installation--setup)  
- [Usage](#-usage)  
- [Results & Visualization](#-results--visualization)  
- [Future Improvements](#-future-improvements)  
- [Contributors](#-contributors)  

---

## **🛠 Technologies Used**  
🔹 Python  
🔹 Pandas  
🔹 NumPy  
🔹 Matplotlib  
🔹 Seaborn  
🔹 Requests (for data fetching)  
🔹 BeautifulSoup (for HTML parsing)  

---

## **📊 Dataset Overview**  
The dataset is obtained from a publicly available JSON file. Each student has three types of scores:  
- **Exam Score**  
- **Quiz Score**  
- **Homework Score**  

Example JSON entry:  
```json
{
  "_id": {"$oid": "50906d7fa3c412bb040eb577"},
  "student_id": 10,
  "class_id": 2,
  "scores": [
    {"type": "exam", "score": 89.23},
    {"type": "quiz", "score": 76.55},
    {"type": "homework", "score": 91.12}
  ]
}
```

---

## **🔄 Project Workflow**  

✅ **Step 1:** Fetch JSON data from the remote URL  
✅ **Step 2:** Convert the JSON file into a Pandas DataFrame  
✅ **Step 3:** Extract individual scores (exam, quiz, homework)  
✅ **Step 4:** Clean and preprocess the dataset  
✅ **Step 5:** Perform statistical analysis  
✅ **Step 6:** Visualize results using Matplotlib and Seaborn  

---

## **⚙ Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/VIPULbunny/student-grades-json-analysis.git
cd student-grades-json-analysis
```

### **2️⃣ Install Dependencies**  
Ensure you have Python 3 installed. Then, install the required packages:  
```bash
pip install pandas numpy matplotlib seaborn requests beautifulsoup4
```

### **3️⃣ Run the Script**  
Execute the Python script:  
```bash
python analysis.py
```

---

## **🚀 Usage**  
1. **Run the script** to fetch the JSON data and process it.  
2. **View the statistical summary** of student grades.  
3. **Visualize the results** using histograms and scatter plots.  

---

## **📈 Results & Visualization**  

### **📌 Distribution of Exam Scores**  
![image](https://github.com/user-attachments/assets/ca727ee0-0731-422c-abcd-343fd44737de)
 <!-- Replace with actual image URL -->

### **📌 Relationship Between Exam & Quiz Scores**  
![image](https://github.com/user-attachments/assets/82a91844-50e4-44cd-ae59-8a1d9e323738)
---

## **🔮 Future Improvements**  
🚀 Add advanced **data visualizations** (box plots, heatmaps)  
🚀 Implement **machine learning models** for predicting student performance  
🚀 Integrate a **web dashboard** using Streamlit or Dash  

---

## **👨‍💻 Contributors**  
💡 Vipul Solanki(https://github.com/VIPULbunny)  

---

## **📜 License**  
This project is licensed under the **MIT License**.  
