import codecademylib3
import pandas as pd
import numpy as np

# code goes here

# Read diabetes.csv into a variable called diabetes_data
diabetes_data = pd.read_csv('diabetes.csv')

# Examine the first five rows of diabetes_data
print(diabetes_data.head())

# Print the number of columns of diabetes_data
print(len(diabetes_data.columns))

# Print the nmber of rows of diabetes_data
print(len(diabetes_data))

# Check for missing values in diabetes_data
print(diabetes_data.isnull().sum())

# Display a concise summary of diabetes_data
print(diabetes_data.info())

# Calculate summary statistics on diabetes_data
print(diabetes_data.describe())

#  Replace the instances of 0 with NaN in the columns 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin' and 'BMI'
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

# Check for null values in all of the columns in diabetes_data
print(diabetes_data.isnull().sum())

# Print concise summary  of diabetes_data
print(diabetes_data.info())

# Print out all of the rows that contain missing (null) values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# Print the data types of each column
print(diabetes_data.dtypes)

# Print concise summary  of diabetes_data
print(diabetes_data.info())

# Print out the unique values in the Outcome column
print(diabetes_data.Outcome.unique())

# Replace instances of 'O' with 0 in the Outcome column
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)

# Covert the dtype of the 'Outcome' column to the type int64
diabetes_data.Outcome = pd.to_numeric(diabetes_data.Outcome)

# Display the values on each column
for col in diabetes_data.columns:
  print(diabetes_data[col].value_counts())

# The maximum value of the Insulin column is 846, which is abnormally high.

# Replace 846 with the mean of the 'Insulin' column
diabetes_data['Insulin'] = diabetes_data['Insulin'].replace(846, diabetes_data['Insulin'].mean())

#  Replace the instances of nan with the mean of the 'Glucose' column in the column 'Glucose'
diabetes_data['Glucose'] = diabetes_data['Glucose'].replace(np.NaN,diabetes_data['Glucose'].mean())

#  Replace the instances of nan with the mean of the 'BloodPressure' column in the column 'BloodPressure'
diabetes_data['BloodPressure'] = diabetes_data['BloodPressure'].replace(np.NaN,diabetes_data['BloodPressure'].mean())

#  Replace the instances of nan with the mean of the 'SkinThickness' column in the column 'SkinThickness'
diabetes_data['SkinThickness'] = diabetes_data['SkinThickness'].replace(np.NaN,diabetes_data['SkinThickness'].mean())

#  Replace the instances of nan with the mean of the 'Insulin' column in the column 'Insulin'
diabetes_data['Insulin'] = diabetes_data['Insulin'].replace(np.NaN,diabetes_data['Insulin'].mean())

#  Replace the instances of nan with the mean of the 'BMI' column in the column 'BMI'
diabetes_data['BMI'] = diabetes_data['BMI'].replace(np.NaN,diabetes_data['BMI'].mean())

print(diabetes_data.head())