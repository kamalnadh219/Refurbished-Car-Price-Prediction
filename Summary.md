# Refurbished Car Price Prediction

## Objective
The project aims to predict prices for refurbished cars to assist in decision-making processes for pricing strategies, inventory management, and sales optimization.

## Approach
1. **Data Analysis and Preprocessing:**
   - Collected and cleaned car pricing data from multiple sources.
   - Handled missing values, normalized numerical features, and encoded categorical variables.
   - Conducted exploratory data analysis (EDA) to identify key features.

2. **Feature Engineering:**
   - Created new features such as car age, depreciation rate, and market demand index.
   - Selected relevant features using correlation analysis and feature importance scores.

3. **Model Development:**
   - Split data into training and testing sets.
   - Experimented with algorithms including Random Forest and CatBoost.

4. **Model Evaluation:**
   - Evaluated model accuracy using R², Mean Absolute Error (MAE), and Mean Squared Error (MSE).
   - Conducted residual analysis to check for overfitting or underfitting.

5. **Prediction Implementation:**
   - Deployed the final model using Flask for real-time price predictions.
   - Integrated the model with business systems for actionable insights.

## Results
- **R² Score:** 0.962
- **Mean Absolute Error:** 1495.59
- **Mean Squared Error:** 6213513.37
