import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Recreating the dataset
data = {
    'Year': list(range(2000, 2022)),
    '18-29': [70, 72, 76, 78, 77, 83, 86, 89, 89, 92, 92, 94, 96, 97, 97, 99, 98.5, 98, 100, 99.5, 99],
    '30-49': [61, 65, 70, 72, 75, 79, 82, 85, 84, 84, 85, 87, 91, 92, 92, 95, 96, 96.5, 97, 97, 97.5, 98],
    '50-64': [46, 50, 54, 56, 61, 66, 70, 71, 72, 75, 74, 77, 79, 81, 81, 82, 87, 87, 88, 92, 96],
    '65+': [14, 14, 18, 22, 24, 28, 32, 35, 38, 40, 43, 46, 54, 56, 57, 63, 64, 65, 66, 73, 74, 75]
}

df = pd.DataFrame(data)

# Prepare the data for modeling
years = df['Year'].values.reshape(-1, 1)  # Reshape years for sklearn
usage_18_29 = df['18-29'].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(years, usage_18_29, test_size=0.2, random_state=42)

# Train models
lin_reg = LinearRegression()
dec_tree = DecisionTreeRegressor()
rand_forest = RandomForestRegressor()

lin_reg.fit(X_train, y_train)
dec_tree.fit(X_train, y_train)
rand_forest.fit(X_train, y_train)

# Make predictions
y_pred_lin_reg = lin_reg.predict(X_test)
y_pred_dec_tree = dec_tree.predict(X_test)
y_pred_rand_forest = rand_forest.predict(X_test)

# Evaluate models
mse_lin_reg = mean_squared_error(y_test, y_pred_lin_reg)
mse_dec_tree = mean_squared_error(y_test, y_pred_dec_tree)
mse_rand_forest = mean_squared_error(y_test, y_pred_rand_forest)

r2_lin_reg = r2_score(y_test, y_pred_lin_reg)
r2_dec_tree = r2_score(y_test, y_pred_dec_tree)
r2_rand_forest = r2_score(y_test, y_pred_rand_forest)

# Displaying results
results = {
    'Model': ['Linear Regression', 'Decision Tree', 'Random Forest'],
    'MSE': [mse_lin_reg, mse_dec_tree, mse_rand_forest],
    'R2 Score': [r2_lin_reg, r2_dec_tree, r2_rand_forest]
}

results_df = pd.DataFrame(results)
print(results_df)