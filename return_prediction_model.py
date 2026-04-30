import pandas as pd
df = pd.read_excel('/Users/avanickzad/Desktop/python_project/fashion_retail_project_dataset.xlsx')
df['campaign_type'] = df['campaign_type'].fillna('No Campaign')
df["age_group"] = pd.cut(df["customer_age"], bins=[18, 25, 34, 42, 50], labels=["18-25", "26-34", "35-42", "43-50"],)

df_ml = df.copy()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler




drop_cols = ["order_id", "customer_id", "order_datetime", "flag_returned"]
for col in drop_cols:
     if col in df_ml.columns:
        df_ml = df_ml.drop(columns=col)
df_ml = df_ml.dropna()

le = LabelEncoder()
for col in df_ml.select_dtypes(include=["object", "string"]).columns:
    df_ml[col] = le.fit_transform(df_ml[col])
df_ml["age_group"] = LabelEncoder().fit_transform(df_ml["age_group"].astype(str))

X = df_ml.drop(columns=["returned"])
y = df_ml["returned"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)  
X_test  = scaler.transform(X_test)       

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

new_customer = pd.DataFrame([{"customer_age": 30, "customer_gender": "Female", "city": "Istanbul", "customer_segment": "Returning", "product_category": "Dress", "size": "M", "quantity": 1, "sales_channel": "Instagram","payment_method": "Card", "campaign_type": "Email Promotion","unit_price_try": 1200,"gross_sales_try": 1200, "discount_rate": 0.1, "discount_amount_try": 120, "net_sales_try": 1080,"shipping_cost_try": 50, "estimated_cogs_try": 700, "estimated_profit_try": 380, "visit_frequency_last_90d": 5, "profit_calc": 380, "satisfaction_score": 4,"margin": 0.35,"flag_segment": 1,"order_daytime": 14,"age_group": "26-34"}])
for col in new_customer.select_dtypes(include=["object", "string"]).columns:new_customer[col] = LabelEncoder().fit_transform(new_customer[col])

new_customer = new_customer[X.columns]
new_customer_scaled = scaler.transform(new_customer)
proba = model.predict_proba(new_customer_scaled)[0]

print("Probability of NOT returned:", proba[0])
print("Probability of RETURNED:", proba[1])



