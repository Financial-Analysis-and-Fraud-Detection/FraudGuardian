import pandas as pd

# Load the financial data from a CSV file
data = pd.read_csv('C:/Users/Tau/Desktop/Repository/FraudGuardian/FraudGuardian/AI_Fraud_Detector/data_set/financial_data.csv')

# Data cleaning (if necessary)
# For example, you can handle missing values, duplicate rows, or outliers.
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

# Example: Selecting relevant columns
selected_features = ['age', 'transaction amount', 'account type']

# Subset the DataFrame with selected features
data = data[selected_features]

from sklearn.model_selection import train_test_split

X = data.drop('account type', axis=1)  # Features (input)
y = data['account type']  # Target (output)

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

from sklearn.ensemble import RandomForestClassifier

# Create and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_resampled, y_train_resampled)

from sklearn.metrics import classification_report, confusion_matrix

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
