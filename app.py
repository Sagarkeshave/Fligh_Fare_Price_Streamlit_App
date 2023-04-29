from sklearn.ensemble import RandomForestRegressor
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import datetime

# model = RandomForestRegressor()

model = pickle.load(open("rf_model_streamlit.pkl", "rb"))

@st.cache

# Define the prediction function

def predict(Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi):



    # Date_of_Journey

    # d = st.date_input(
    #     "When\'s your birthday",
    #     datetime.date(2019, 7, 6))
    # st.title("Flight Fare Prediction")
    # st.image("https://www.google.com/search?q=flight+images+png&tbm=isch&ved=2ahUKEwjxupSg5sz-AhXu6nMBHRWVCcsQ2-cCegQIABAA&oq=flight+images+png&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgYIABAFEB4yBggAEAgQHjIGCAAQCBAeOgQIIxAnOgYIABAHEB46BwgAEIoFEEM6CAgAEIAEELEDOgsIABCABBCxAxCDAToKCAAQigUQsQMQQzoNCAAQigUQsQMQgwEQQ1C2DljaM2CGNmgAcAB4AIAB7wGIAYAWkgEGMC4xNy4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=y9lLZLGpDe7Vz7sPlaqm2Aw&bih=569&biw=1280&rlz=1C1UEAD_enIN1020IN1020#imgrc=JyEzIuYMazCYPM")
    # date_dep = st.date_input("Dep_Time", datetime.date(2019, 7, 6))
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%d").month)

    # print("Journey Date : ",Journey_day, Journey_month)

    # Departure
    # time_dep = st.time_input("Dep_Time", datetime.time(8, 45))
            
    time_dep = time_dep.split(sep=":")
    Dep_hour = int(time[0])
    Dep_min = int(time[1])

    # print("Departure : ",Dep_hour, Dep_min)

    # Arrival
    # t = st.time_input('Set an alarm for', datetime.time(8, 45))
    # date_arr = st.time_input("Arrival_Time", datetime.time(8,45))
            
    Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
    # print("Arrival : ", Arrival_hour, Arrival_min)

    # Duration
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    # print("Duration : ", dur_hour, dur_min)

    # Total Stops
    # depth = st.number_input('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)
    # Total_stops = st.number_input("Total stops : ", min_value = 1, max_value = 4, value = 1.0)
    # print(Total_stops)

    # Airline
    # AIR ASIA = 0 (not in column)
    # cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    # airline = st.selectbox("Select Airline : ", ["Jet Airways", "IndiGo", 'Air India', 'Multiple carriers','SpiceJet', 'Vistara','GoAir','Multiple carriers Premium economy','Trujet'])

    if (airline == 'Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0

    elif (airline == 'Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    # print(Jet_Airways,
    #     IndiGo,
    #     Air_India,
    #     Multiple_carriers,
    #     SpiceJet,
    #     Vistara,
    #     GoAir,
    #     Multiple_carriers_Premium_economy,
    #     Jet_Airways_Business,
    #     Vistara_Premium_economy,
    #     Trujet)

    # Source
    # Banglore = 0 (not in column)
    # color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    # Source = st.selectbox("Source:", ["Delhi", "Kolkata","Mumbai","Chennai"])
    # Source = request.form["Source"]
    if (Source == 'Delhi'):
        Source_Delhi = 1
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0

    elif (Source == 'Kolkata'):
        Source_Delhi = 0
        Source_Kolkata = 1
        Source_Mumbai = 0
        Source_Chennai = 0

    elif (Source == 'Mumbai'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 1
        Source_Chennai = 0

    elif (Source == 'Chennai'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 1

    else:
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0

    # print(s_Delhi,
    #     s_Kolkata,
    #     s_Mumbai,
    #     s_Chennai)

    # Destination
    # Banglore = 0 (not in column)
    # Destination = st.selectbox("Destination :" , ["Cochin", "Delhi","New_Delhi","Hyderabad", "Kolkata"])
    # Destination = request.form["Destination"]
    if (Destination == 'Cochin'):

        Destination_Cochin = 1
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        d_Kolkata = 0

    elif (Source == 'Delhi'):
        Destination_Cochin = 0
        Destination_Delhi = 1
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        d_Kolkata = 0

    elif (Source == 'New_Delhi'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 1
        Destination_Hyderabad = 0
        d_Kolkata = 0

    elif (Source == 'Hyderabad'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 1
        d_Kolkata = 0

    elif (Source == 'Kolkata'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        d_Kolkata = 1

    else:
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        d_Kolkata = 0



    prediction = model.predict(pd.DataFrame([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi

        ]], columns =
            ["Total_stops",
            "Journey_day",
            "Journey_month",
            "Dep_hour",
            "Dep_min",
            "Arrival_hour",
            "Arrival_min",
            "dur_hour",
            "dur_min",
            "Air_India",
            "GoAir",
            "IndiGo",
            "Jet_Airways",
            "Jet_Airways_Business",
            "Multiple_carriers",
            "Multiple_carriers_Premium_economy",
            "SpiceJet",
            "Trujet",
            "Vistara",
            "Vistara_Premium_economy",
            "Source_Chennai",
            "Source_Delhi",
            "Source_Kolkata",
            "Source_Mumbai",
            "Destination_Cochin",
            "Destination_Delhi",
            "Destination_Hyderabad",
            "Destination_Kolkata",
            "Destination_New_Delhi"]
        ))

#     output = round(prediction[0], 2)
    return prediction
prediction_flare = model.predict(pd.DataFrame([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi

        ]], columns =
            ["Total_stops",
            "Journey_day",
            "Journey_month",
            "Dep_hour",
            "Dep_min",
            "Arrival_hour",
            "Arrival_min",
            "dur_hour",
            "dur_min",
            "Air_India",
            "GoAir",
            "IndiGo",
            "Jet_Airways",
            "Jet_Airways_Business",
            "Multiple_carriers",
            "Multiple_carriers_Premium_economy",
            "SpiceJet",
            "Trujet",
            "Vistara",
            "Vistara_Premium_economy",
            "Source_Chennai",
            "Source_Delhi",
            "Source_Kolkata",
            "Source_Mumbai",
            "Destination_Cochin",
            "Destination_Delhi",
            "Destination_Hyderabad",
            "Destination_Kolkata",
            "Destination_New_Delhi"]
        ))

# #     output = round(prediction[0], 2)
#     return prediction


st.title("Flight Fare Prediction")
st.image("https://www.google.com/search?q=flight+images+png&tbm=isch&ved=2ahUKEwjxupSg5sz-AhXu6nMBHRWVCcsQ2-cCegQIABAA&oq=flight+images+png&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgYIABAFEB4yBggAEAgQHjIGCAAQCBAeOgQIIxAnOgYIABAHEB46BwgAEIoFEEM6CAgAEIAEELEDOgsIABCABBCxAxCDAToKCAAQigUQsQMQQzoNCAAQigUQsQMQgwEQQ1C2DljaM2CGNmgAcAB4AIAB7wGIAYAWkgEGMC4xNy4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=y9lLZLGpDe7Vz7sPlaqm2Aw&bih=569&biw=1280&rlz=1C1UEAD_enIN1020IN1020#imgrc=JyEzIuYMazCYPM")
date_dep = st.date_input("Dep_Day", datetime.date(2019, 7, 6))
time_dep = st.time_input("Dep_Time", datetime.time(8, 45))
date_arr = st.time_input("Arrival_Time", datetime.time(8,45))
Total_stops = st.number_input("Total stops : ", min_value = 1.0, max_value = 4.0, value = 1.0)
airline = st.selectbox("Select Airline : ", ["Jet Airways", "IndiGo", 'Air India', 'Multiple carriers','SpiceJet', 'Vistara','GoAir','Multiple carriers Premium economy','Trujet'])
Source = st.selectbox("Source:", ["Delhi", "Kolkata","Mumbai","Chennai"])
Destination = st.selectbox("Destination :" , ["Cochin", "Delhi","New_Delhi","Hyderabad", "Kolkata"])



if st.button('Predict Price'):
#     price = model.predict([[Total_stops,
#             Journey_day,
#             Journey_month,
#             Dep_hour,
#             Dep_min,
#             Arrival_hour,
#             Arrival_min,
#             dur_hour,
#             dur_min,
#             Air_India,
#             GoAir,
#             IndiGo,
#             Jet_Airways,
#             Jet_Airways_Business,
#             Multiple_carriers,
#             Multiple_carriers_Premium_economy,
#             SpiceJet,
#             Trujet,
#             Vistara,
#             Vistara_Premium_economy,
#             Source_Chennai,
#             Source_Delhi,
#             Source_Kolkata,
#             Source_Mumbai,
#             Destination_Cochin,
#             Destination_Delhi,
#             Destination_Hyderabad,
#             Destination_Kolkata,
#             Destination_New_Delhi]])




    st.success(f'Your flare for the flight is Rs{prediction_flare[0]:.2f}')
