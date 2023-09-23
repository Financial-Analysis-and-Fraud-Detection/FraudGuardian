# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime
from imblearn.over_sampling import RandomOverSampler
from keras.models import Sequential
from keras.layers import Dense
import random

# Step 1: Data Collection
# Load NSFAS CSV data and University of Limpopo CSV data
nsfas_df = pd.read_csv('C:/Users/Tau/Desktop/Repository/FraudGuardian/FraudGuardian/Financial analysis and fraud dection AI/data/nsfas_data.csv')  # Replace with the actual path to nsfas_data.csv
university_df = pd.read_csv('C:/Users/Tau/Desktop/Repository/FraudGuardian/FraudGuardian/Financial analysis and fraud dection AI/data/university_data.csv')  # Replace with the actual path to university_data.csv

# Step 2: Data Preprocessing
# Merge the datasets based on a common key (Student ID)
merged_df = pd.merge(nsfas_df, university_df, left_on='ID Number', right_on='Student ID', suffixes=('_nsfas', '_university'))

# Handle missing data and data cleaning if needed
# For simplicity, we assume data is clean in this example

# Step 3: Feature Engineering
# Calculate age from the Date of Birth
merged_df['Date of Birth_nsfas'] = pd.to_datetime(merged_df['Date of Birth_nsfas'])
merged_df['Age'] = ((datetime.now() - merged_df['Date of Birth_nsfas']).dt.total_seconds() / (365.25 * 24 * 3600)).astype(int)

# Step 4: Machine Learning Model Selection
# Prepare features and target variable
X = merged_df[['Gender_nsfas', 'Age', 'Course_nsfas']]
y = merged_df['Financial Need']

# Convert categorical variables to numerical using label encoding
label_encoder = LabelEncoder()
X['Gender_nsfas'] = label_encoder.fit_transform(X['Gender_nsfas'])
X['Course_nsfas'] = label_encoder.fit_transform(X['Course_nsfas'])

# Step 5: Address Class Imbalance (Random Oversampling)
oversampler = RandomOverSampler(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = oversampler.fit_resample(X, y)

# Step 6: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Ensure y_train is in numerical format (0 and 1)
label_encoder_y = LabelEncoder()
y_train = label_encoder_y.fit_transform(y_train)

# Step 7: Model Training and Evaluation (using Deep Learning - Neural Network)
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Single neuron for binary classification

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=64, verbose=1)

# Step 8: Model Evaluation
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)  # Convert probabilities to binary predictions

# Convert y_test to numerical format if needed
y_test = label_encoder_y.transform(y_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Neural Network Classifier:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Step 9: SMS Confirmation Security Techniques
# Generate a random confirmation code
confirmation_code = str(random.randint(1000, 9999))

# Simulate sending an SMS with the confirmation code
student_phone_number = "0783592495"  # Replace with the student's actual phone number
sms_message = f"Your NSFAS application confirmation code is: {confirmation_code}"

# In a real application, you would send this SMS using a SMS gateway API
print(f"Sending SMS to {student_phone_number}: {sms_message}")
