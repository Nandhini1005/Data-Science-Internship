import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load Titanic dataset
data = pd.read_csv("titanic.csv")

# Simple preprocessing
data = data[["Survived", "Pclass", "Sex", "Age"]].dropna()
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

X = data[["Pclass", "Sex", "Age"]]
y = data["Survived"]

# Train logistic regression
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "titanic_model.pkl")
print("✅ Model saved as titanic_model.pkl")
