# 🚕 Taxi Trip Fare Prediction

Taxi trip price prediction using **Polynomial Regression (degree 2)** with a Streamlit web app.

## Results

| Model | Test MSE | Test R² |
|---|---:|---:|
| Linear Regression | 194.72 | 0.7655 |
| **Polynomial Regression** | **90.02** | **0.8916** |

**Final model:** Polynomial Regression, degree 2  
**Test RMSE:** 9.49

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Retrain
```bash
python train_model.py
```
