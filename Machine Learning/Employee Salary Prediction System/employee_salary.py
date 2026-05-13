import pandas as pd
import numpy as np
import random

np.random.seed(42)

rows = 200

employee_id = range(1001, 1001 + rows)
age = np.random.randint(21, 60, rows)
gender = np.random.choice(['Male', 'Female'], rows)
education = np.random.choice(['Bachelor', 'Master', 'PhD'], rows)
department = np.random.choice(['HR', 'IT', 'Sales', 'Finance', 'Marketing'], rows)
experience = np.random.randint(1, 20, rows)
working_hours = np.random.randint(35, 60, rows)
performance_score = np.random.randint(50, 100, rows)
projects_completed = np.random.randint(1, 15, rows)
salary = (
    experience * 4000 +
    performance_score * 500 +
    projects_completed * 1500 +
    np.random.randint(10000, 50000, rows)
)

# Create DataFrame

df = pd.DataFrame({
    'Employee_ID': employee_id,
    'Age': age,
    'Gender': gender,
    'Education': education,
    'Department': department,
    'Experience': experience,
    'Working_Hours': working_hours,
    'Performance_Score': performance_score,
    'Projects_Completed': projects_completed,
    'Salary': salary
})

# Save dataset
df.to_csv('employee_salary_dataset.csv', index=False)

print(df.head())
