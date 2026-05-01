# Return Prediction Model

In this project, I worked on a fashion retail dataset and tried to build a simple model to predict product returns.

## Why I did this

Returns are an important issue for retail businesses because they can affect profit, customer experience, and campaign performance.  
So I wanted to see if the data could give any early signal about which orders might be more likely to be returned.

## What I did

I used customer and order information to build a basic Logistic Regression model.

Before training the model, I cleaned the data and prepared a few useful features, such as:
- margin
- age group
- visit frequency
- return flag

I also encoded categorical variables and scaled the numerical columns so the model could work with them properly.

## Result

The model reached about **89% accuracy**.

At first, this looks strong, but the confusion matrix showed something important: the model mostly predicts non-returned orders and has difficulty detecting the returned ones.

This probably happens because most orders in the dataset were not returned, so the data is imbalanced.

## Example Prediction

I tested the model with a sample customer.

For that customer, the model estimated around a **28% probability of return**.  
So I would read this as a low-to-medium return risk, not a very high one.

## What I learned

The main thing I learned is that accuracy alone is not enough to judge a model.

Even though the accuracy is high, the confusion matrix gives a much clearer picture of what the model is actually doing.

This helped me understand why evaluation is so important in machine learning.

## Limitations

This is a simple first version of the model.

The biggest limitation is the class imbalance in the dataset. If I continue improving this project, I would try balancing the data, testing different models, and adding more useful features.
