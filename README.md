# 🚕 Taxi Trip Pricing Prediction
project link = 

A Machine Learning project that predicts **taxi trip prices** based on trip distance, duration, passenger count, fare rates, time of day, day of week, traffic conditions, and weather conditions.

The project includes **data preprocessing, exploratory data analysis, Linear Regression, Polynomial Regression, model evaluation, and a Streamlit web application** for making predictions.

## Results

| Model | Test MSE | Test R² |
|---|---:|---:|
| Linear Regression | 194.72 | 0.7655 |
| **Polynomial Regression** | **90.02** | **0.8916** |

**Final model:** Polynomial Regression, degree 2  
**Test RMSE:** 9.49


## 📌 Project Overview

Taxi pricing can depend on multiple factors such as:

* Trip distance
* Trip duration
* Number of passengers
* Base fare
* Per-kilometer rate
* Per-minute rate
* Time of day
* Day of week
* Traffic conditions
* Weather conditions

The goal of this project is to build a regression model that can learn the relationship between these factors and the final **Trip Price**.

Two regression approaches were evaluated:

1. Linear Regression
2. Polynomial Regression

After comparison, **Polynomial Regression with degree 2** performed better and was selected as the final model.

---

## 🎯 Objective

The main objective is to develop a machine learning model that can:

* Predict taxi trip prices.
* Handle missing values in the dataset.
* Process numerical and categorical features.
* Capture non-linear relationships between input variables.
* Compare different regression models.
* Provide predictions through an interactive Streamlit application.

---

## 📊 Dataset

The dataset contains **1,000 taxi trip records** and **11 columns**.

### Features

| Feature                 | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `Trip_Distance_km`      | Distance travelled during the trip                        |
| `Time_of_Day`           | Time period such as Morning, Afternoon, Evening, or Night |
| `Day_of_Week`           | Weekday or Weekend                                        |
| `Passenger_Count`       | Number of passengers                                      |
| `Traffic_Conditions`    | Traffic level during the trip                             |
| `Weather`               | Weather condition during the trip                         |
| `Base_Fare`             | Base fare charged for the trip                            |
| `Per_Km_Rate`           | Fare charged per kilometer                                |
| `Per_Minute_Rate`       | Fare charged per minute                                   |
| `Trip_Duration_Minutes` | Duration of the trip in minutes                           |
| `Trip_Price`            | **Target variable**                                       |

The dataset contains both numerical and categorical variables.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Exploration
   ↓
Missing Value Detection
   ↓
Missing Value Treatment
   ↓
Categorical Encoding
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Polynomial Regression
   ↓
Model Evaluation
   ↓
Final Model Selection
   ↓
Streamlit Deployment
```

---

## 🧹 Data Preprocessing

The dataset contains missing values.

### Numerical Features

Missing values in numerical columns were handled using the **mean** of the corresponding column.

The numerical columns include:

* `Trip_Distance_km`
* `Passenger_Count`
* `Base_Fare`
* `Per_Km_Rate`
* `Per_Minute_Rate`
* `Trip_Duration_Minutes`
* `Trip_Price`

### Categorical Features

Missing values in categorical columns were replaced using the **mode** of the respective column.

Categorical columns include:

* `Time_of_Day`
* `Day_of_Week`
* `Traffic_Conditions`
* `Weather`

This preprocessing resulted in a dataset with no remaining missing values.

---

## 🔎 Exploratory Data Analysis

Exploratory analysis was performed to understand the dataset and relationships between variables.

Some of the analysis includes:

* Dataset inspection
* Data types
* Descriptive statistics
* Missing-value analysis
* Feature distributions
* Relationship between trip distance and trip price

For example, a scatter plot was used to examine the relationship between `Trip_Distance_km` and `Trip_Price`.

---

## 🤖 Models Used

### 1. Linear Regression

Linear Regression was first implemented as a baseline model.

**Test Results:**

* **MSE:** 194.72
* **R² Score:** 0.7655

The model explains approximately **76.55% of the variation** in the target variable.

---

### 2. Polynomial Regression

Polynomial Regression was then implemented to capture non-linear relationships between the features and taxi trip price.

A **degree-2 polynomial transformation** was used:

```python
PolynomialFeatures(degree=2, include_bias=False)
```

The transformed features were then used with Linear Regression.

**Test Results:**

* **MSE:** 90.02
* **R² Score:** 0.8916
* **RMSE:** 9.49

**Training Results:**

* **MSE:** 105.12
* **R² Score:** 0.9394

---

## 📈 Model Comparison

| Model                     |  Test MSE |    Test R² | Test RMSE |
| ------------------------- | --------: | ---------: | --------: |
| Linear Regression         |    194.72 |     0.7655 |     13.95 |
| **Polynomial Regression** | **90.02** | **0.8916** |  **9.49** |

### 🏆 Final Model

**Polynomial Regression (Degree 2)** was selected as the final model because it achieved:

* Lower MSE
* Lower RMSE
* Higher R² score

Compared with Linear Regression, the Polynomial Regression model reduced the test MSE by approximately **53.8%** and improved the R² score from **0.7655 to 0.8916**.

---

## 📊 Final Model Performance

### Training

```text
R² Score : 0.9394
MSE      : 105.12
```

### Testing

```text
R² Score : 0.8916
MSE      : 90.02
RMSE     : 9.49
```

The difference between training and testing R² is approximately **0.048**, indicating that the model generalizes reasonably well to the test data.

---

## 🌐 Streamlit Application

The project also includes an interactive **Streamlit application**.

The application allows users to enter taxi trip information and receive a predicted trip price.

### User Inputs

The application can take inputs corresponding to the model features, including:

* Trip distance
* Time of day
* Day of week
* Passenger count
* Traffic conditions
* Weather
* Base fare
* Per-kilometer rate
* Per-minute rate
* Trip duration

The trained Polynomial Regression model is then used to generate the predicted taxi trip price.

---

## 🗂️ Project Structure

```text
taxi-trip-pricing/
│
├── app.py
│
├── train_model.py
│
├── model.pkl
│
├── taxi_trip_pricing.csv
│
├── taxi_trip_fair_prediction(1).ipynb
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

### File Description

| File                                 | Purpose                                  |
| ------------------------------------ | ---------------------------------------- |
| `app.py`                             | Streamlit application                    |
| `train_model.py`                     | Script for training the model            |
| `model.pkl`                          | Saved trained model                      |
| `taxi_trip_pricing.csv`              | Dataset                                  |
| `taxi_trip_fair_prediction(1).ipynb` | Complete ML analysis and experimentation |
| `requirements.txt`                   | Python dependencies                      |
| `README.md`                          | Project documentation                    |
| `.gitignore`                         | Git ignored files                        |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**
* **Jupyter Notebook**

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd taxi-trip-pricing
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔁 Retrain the Model

If you want to retrain the model using the dataset:

```bash
python train_model.py
```

This will train the model and save the trained model for use by the Streamlit application.

---

## 💡 Key Learnings

Through this project, I worked with:

* Data loading and inspection
* Exploratory Data Analysis
* Missing-value handling
* Numerical and categorical data preprocessing
* Train-test splitting
* Linear Regression
* Polynomial Regression
* Model evaluation using MSE and R²
* RMSE calculation
* Model comparison
* Model serialization
* Streamlit deployment

---

## 🚀 Future Improvements

Possible improvements include:

* Testing additional regression algorithms such as Random Forest and Gradient Boosting.
* Hyperparameter tuning.
* Using cross-validation for more reliable model evaluation.
* Creating additional visualizations.
* Improving the Streamlit interface.
* Adding prediction confidence/error analysis.
* Deploying the application publicly.

---

## 📌 Results

The final Polynomial Regression model achieved an **R² score of 0.8916 on the test data**, meaning it explains approximately **89.16% of the variation in taxi trip prices** in the test set.

The model achieved a **test MSE of 90.02** and a **test RMSE of approximately 9.49**.

Overall, Polynomial Regression performed substantially better than the baseline Linear Regression model for this dataset.

---

## 👨‍💻 Author

**Ashish Ambad**

Machine Learning / AI-ML Project

---

## ⭐ Project Status

**Completed ✅**

The project includes the complete machine learning workflow from data preprocessing and model comparison to a Streamlit prediction application.

