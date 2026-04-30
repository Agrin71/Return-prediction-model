# Return Prediction Model

This project focuses on predicting the probability of product returns in a fashion retail dataset.

## Objective

The goal is to estimate whether an order is likely to be returned, helping the business better understand return behavior and reduce potential losses.

## Approach

A Logistic Regression model was built using customer and transaction data.

The process includes:
- Data cleaning and preprocessing  
- Feature engineering (such as margin, age group, and visit frequency)  
- Encoding categorical variables  
- Scaling numerical features  
- Training and evaluating the model  

The focus of this project was to build a simple and understandable baseline model rather than a highly complex one.

## Results

The model achieved an accuracy of around **89%**.

However, looking at the confusion matrix shows that the model mainly predicts the majority class (non-returned orders) and struggles to correctly identify returned orders. This is likely due to the dataset being imbalanced.

## Example Prediction

To better understand how the model works in practice, a sample customer was tested.

The model estimated that this order has around a **28% probability of being returned**, which indicates a relatively low to moderate level of risk.

## Key Insight

Even a simple model can provide useful insights into customer behavior.  
This approach can help businesses take early actions, such as improving product descriptions or guiding customers more effectively.

## Limitations

This is a baseline model, and there is still room for improvement.

The main limitation is the imbalance in the dataset, which affects the model’s ability to detect returned orders. Future improvements could include:
- Handling class imbalance  
- Trying different models  
- Adding more relevant features  

## Final Note

This project demonstrates a basic but complete machine learning workflow, from data preparation to prediction, with a focus on clarity and practical understanding.
