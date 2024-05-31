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
    print(x)
    for c in x:
        if c =="Yes" or c== "Male":
            c = 1
        elif c == "No" or c == "Female":
            c = 0
    x = np.array(x)
    x = pd.DataFrame(x, columns=columns)
    y = model.predict(x)
    # Simple approval based on employment status (mock)
    if Employed == "Yes":
        return "Approved"+y
    else:
        return "Rejected"+y

# Gradio interface definition
interface = gr.Interface(
    fn=predict_approval,
    inputs=[
        gr.Radio(["Male", "Female"], label="Gender"),
        gr.Slider(minimum=18, maximum=100, label="Age"),
        gr.Number(label="Debt"),
        gr.Radio(["Yes", "No"], label="Married"),
        gr.Radio(["Yes", "No"], label="Bank Customer"),
        gr.Radio(['CommunicationServices', 'ConsumerDiscretionary', 'ConsumerStaples',
 'Education', 'Energy', 'Financials', 'Healthcare', 'Industrials',
 'InformationTechnology', 'Materials', 'Real Estate', 'Research', 'Transport'
 'Utilities'],label="Industry"),
        gr.Radio(['Asian', 'Black', 'Latino', 'Other', 'White'], label="Ethnicity"),
        gr.Slider(minimum=0, maximum=40, label="Years Employed"),
        gr.Radio(["Yes", "No"], label="Prior Default"),
        gr.Radio(["Yes", "No"], label="Employed"),
        gr.Slider(minimum=300, maximum=850, label="Credit Score"),
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