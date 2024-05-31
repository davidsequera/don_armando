import gradio as gr
import numpy as np
import pandas as pd
import joblib
model = joblib.load('models/model.pkl')


columns = [ "Gender",
    "Age",
    "Debt",
    "Married",
    "BankCustomer",
    "Industry",
    "Ethnicity",
    "YearsEmployed",
    "PriorDefault",
    "Employed",
    "CreditScore",
    "DriversLicense",
    "Citizen",
    "ZipCode",
    "Income"]

# Placeholder function for prediction (replace with your trained model)
def predict_approval(
    Gender,
    Age,
    Debt,
    Married,
    BankCustomer,
    Industry,
    Ethnicity,
    YearsEmployed,
    PriorDefault,
    Employed,
    CreditScore,
    DriversLicense,
    Citizen,
    ZipCode,
    Income
):
    x = [   Gender,
    Age,
    Debt,
    Married,
    BankCustomer,
    Industry,
    Ethnicity,
    YearsEmployed,
    PriorDefault,
    Employed,
    CreditScore,
    DriversLicense,
    Citizen,
    ZipCode,
    Income]
    for i in range(len(x)):
        c = x[i]
        if c =="Yes" or c== "Male":
            x[i] = 1
        elif c == "No" or c == "Female":
            x[i] = 0
    x = pd.DataFrame([x], columns=columns)
    y = model.predict(x)
    # Simple approval based on employment status (mock)
    if y[0]:
        return "Congratulation your card is Approved"
    else:
        return "Sorry We can not provide at this time but we will take you into account for next opportunities"

# Gradio interface definition
interface = gr.Interface(
    fn=predict_approval,
    inputs=[
        gr.Radio(["Male", "Female"], label="Gender"),
        gr.Slider(minimum=12, maximum=100, label="Age"),
        gr.Number(label="Debt"),
        gr.Radio(["Yes", "No"], label="Married"),
        gr.Radio(["Yes", "No"], label="Bank Customer"),
        gr.Radio(['CommunicationServices', 'ConsumerDiscretionary', 'ConsumerStaples',
 'Education', 'Energy', 'Financials', 'Healthcare', 'Industrials',
 'InformationTechnology', 'Materials', 'Real Estate', 'Research', 'Transport'
 'Utilities'],label="Industry"),
        gr.Radio(['Asian', 'Black', 'Latino', 'Other', 'White'], label="Ethnicity"),
        gr.Slider(minimum=0, maximum=30, label="Years Employed"),
        gr.Radio(["Yes", "No"], label="Prior Default"),
        gr.Radio(["Yes", "No"], label="Employed"),
        gr.Slider(minimum=0, maximum=100, label="Credit Score"),
        gr.Radio(["Yes", "No"], label="Driver's License"),
        gr.Radio(['ByBirth', 'ByOtherMeans', 'Temporary'], label="Citizen"),
        gr.Number(label="Zip Code"),
        gr.Number(label="Income"),
    ],
    outputs="text",
    title="Credit Card Approval Prediction",
    description="Enter applicant information to predict credit card approval (placeholder results).",
)

# Launch the Gradio interface
interface.launch()