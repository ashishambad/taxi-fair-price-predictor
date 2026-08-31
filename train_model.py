import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("taxi_trip_pricing.csv")
num = ["Trip_Distance_km","Passenger_Count","Base_Fare","Per_Km_Rate","Per_Minute_Rate","Trip_Duration_Minutes","Trip_Price"]
cat = ["Time_of_Day","Day_of_Week","Traffic_Conditions","Weather"]
for c in num: df[c] = df[c].fillna(df[c].mean())
for c in cat: df[c] = df[c].fillna(df[c].mode()[0])

X = pd.get_dummies(df.drop("Trip_Price", axis=1), drop_first=True)
y = df["Trip_Price"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
model = LinearRegression().fit(X_train_poly,y_train)
pred = model.predict(X_test_poly)

print("MSE:", mean_squared_error(y_test,pred))
print("R2:", r2_score(y_test,pred))
print("RMSE:", mean_squared_error(y_test,pred)**0.5)

artifact = {
 "model": model, "poly": poly, "feature_columns": X.columns.tolist(),
 "numeric_fill_values": {c:float(df[c].mean()) for c in num},
 "categorical_fill_values": {c:df[c].mode()[0] for c in cat},
 "metrics": {"poly_test_mse":float(mean_squared_error(y_test,pred)),
             "poly_test_r2":float(r2_score(y_test,pred))}
}
with open("model.pkl","wb") as f: pickle.dump(artifact,f)
