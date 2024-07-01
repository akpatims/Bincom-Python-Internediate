import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load data
df = pd.read_csv("/home/tim/Downloads/test_Y3wMUE5_7gLdaTN.csv")
non_numeric_cols = df.select_dtypes(include=['object']).columns
for col in non_numeric_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

df.dropna(inplace= True)

# Preprocess data
X = df.drop(["Loan_ID"], axis=1)
y = df["Loan_ID"]
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model performance
y_pred = model.predict(X_test)
print("Accuracy:", (y_test, y_pred))