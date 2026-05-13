# Predictive Modeling Using Machine Learning 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Create Simple Dataset
data = {
    "Age": [21, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "Salary": [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("\n Dataset:")
print(df)
# 2. Split Features and Target
X = df[["Age", "Salary"]]
y = df["Purchased"]
# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# 4. Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# 5. Model Training
model = LogisticRegression()
model.fit(X_train, y_train)
# 6. Prediction
y_pred = model.predict(X_test)
# 7. Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\n📊 Model Accuracy:", accuracy)

print("\n Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n Classification Report:")
print(classification_report(y_test, y_pred))
# 8. Visualization
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
# 9. New Prediction Example
new_data = [[28, 35000]]
new_data_scaled = scaler.transform(new_data)

prediction = model.predict(new_data_scaled)

print("\n🔮 Prediction for new data (Age=28, Salary=35000):", prediction[0])

if prediction[0] == 1:
    print(" Customer will Purchase:")
else:
    print(" Customer will NOT Purchase:")