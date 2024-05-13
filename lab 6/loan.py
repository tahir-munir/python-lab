import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv(r'C:/Users/dell/Downloads/Loan.csv')
print(data.head())

label_encoder = LabelEncoder()
for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = label_encoder.fit_transform(data[column])

X = data.drop(['Loan', 'Name'], axis=1)
y = data['Loan']

print(X.head())
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_scaled, y)

# Now, let's predict on a new data point
new_data = pd.DataFrame({
    'Age': [10],
    'Marital Status': [1],
    'Employment Status': [1],
    'Income': [60000]
})


# Standardize the new data
new_data_scaled = scaler.transform(new_data)

# Make predictions
prediction = model.predict(new_data_scaled)
original_data = label_encoder.inverse_transform(prediction)
print("Predicted Loan Status:", original_data)