import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
)
st.title("Customer Churn Prediction & Retention Analytics System")

st.write("Fill the values below to predict whether a customer will churn or not.")

with st.container(border=True):

    st.write("### Customer Details")

    c1, c2, c3 = st.columns(3)

    tenure = c1.number_input("Tenure", min_value=0, max_value=72, value=0, step=1, key="tenure")
    maritialstatus = c1.selectbox("Maritial Status", options=[" ", "Married", "Single", "Divorced"], key="marital_status")
    hourspendonapp = c1.number_input("Hour Spend On App", min_value=0, max_value=100, value=0, step=1, key="hour_spend_on_app")
    stisfactionscore = c1.number_input("Satisfaction Score", min_value=0, max_value=10, value=0, step=1, key="satisfaction_score")
    orderamounthikefromlastyear = c1.number_input("Order Amount Hike From Last Year", min_value=0, max_value=100, value=0, step=1, key="order_amount_hike_from_last_year")

    gender = c2.selectbox("Gender", options=[" ", "Male", "Female"], key="gender")
    ordercount = c2.number_input("Order Count", min_value=0, max_value=100, value=0, step=1, key="order_count")
    numberofdeviceregistered = c2.number_input("Number of Device Registered", min_value=0, max_value=10, value=0, step=1, key="number_of_device_registered")
    complain = c2.number_input("Complain", min_value=0, max_value=5, value=0, step=1, key="complain")
    daysincelastorder = c2.number_input("Day Since Last Order", min_value=0, max_value=365, value=0, step=1, key="day_since_last_order")


    citytier = c3.number_input("City Tier", min_value=1, max_value=3, value=1, step=1, key="city_tier")
    warehousetohome = c3.number_input("Warehouse To Home", min_value=1, max_value=100, value=1, step=1, key="warehouse_to_home")
    numberofaddress = c3.number_input("Number of Address", min_value=0, max_value=10, value=0, step=1, key="number_of_address")
    couponused = c3.number_input("Coupon Used", min_value=0, max_value=10, value=0, step=1, key="coupon_used")
    cashbackamount = c3.number_input("Cashback Amount", min_value=0, max_value=1000, value=0, step=1, key="cashback_amount")



if st.button("Predict"):
    st.markdown("---")
    model = joblib.load("models/churn_prediction_model.pkl")

    gender_female = 1 if gender == "Female" else 0
    gender_male = 1 if gender == "Male" else 0

    marital_divorced = 1 if maritialstatus == "Divorced" else 0
    marital_married = 1 if maritialstatus == "Married" else 0
    marital_single = 1 if maritialstatus == "Single" else 0

    input_data = pd.DataFrame({
        "Tenure": [tenure],
        "MaritalStatus_Divorced": [marital_divorced],
        "MaritalStatus_Married": [marital_married],
        "MaritalStatus_Single": [marital_single],
        "Gender_Female": [gender_female],
        "Gender_Male": [gender_male],
        "HourSpendOnApp": [hourspendonapp],
        "SatisfactionScore": [stisfactionscore],
        "OrderAmountHikeFromlastYear": [orderamounthikefromlastyear],
        "OrderCount": [ordercount],
        "NumberOfDeviceRegistered": [numberofdeviceregistered],
        "Complain": [complain],
        "DaySinceLastOrder": [daysincelastorder],
        "CityTier": [citytier],
        "WarehouseToHome": [warehousetohome],
        "NumberOfAddress": [numberofaddress],
        "CouponUsed": [couponused],
        "CashbackAmount": [cashbackamount]
    })

    prediction = model.predict(input_data)[0]

    try:
        probability = model.predict_proba(input_data)[0][1]
    except:
        probability = None

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is likely to stay")

    if probability is not None:
        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

        if probability < 0.30:
            st.info("Risk Level: Low")
            st.info("""
            Recommended Actions:
            - Continue regular engagement
            - Send personalized product recommendations
            - Offer loyalty rewards
            - Encourage referrals
            """)
        elif probability < 0.70:
            st.warning("Risk Level: Medium")
            st.info("""
            Recommended Actions:
            - Send targeted discount coupons
            - Offer loyalty program benefits
            - Collect customer feedback
            - Provide personalized offers
            """)
        else:
            st.error("Risk Level: High")
            st.info("""
            Recommended Actions:
            - Immediate retention campaign
            - Special discount or cashback offer
            - Priority customer support outreach
            - Dedicated account manager follow-up
            - Personalized win-back incentives
            """)
        

st.markdown("---")
st.caption(
    "Built using Python, XGBoost, Streamlit, Scikit-Learn and Joblib"
)
