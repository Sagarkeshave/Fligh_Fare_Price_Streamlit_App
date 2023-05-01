import streamlit as st
import numpy as np
import pandas as pd
import pickle
import datetime
from PIL import Image

model = pickle.load(open("rf_model_streamlit.pkl", "rb"))


image = Image.open('download.jpg')

st.image(image)

st.header("Flight Fare Prediction App")
st.text_input("Enter your Name: ", key="name")



#User_input date for jrny day and month
date_dep = st.date_input("Departure_Day", datetime.date(2019, 7, 6))
Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

#Input time for departure

time_dep = st.time_input("Departure_Time", datetime.time(8, 45))
dep_time= str(time_dep)
time_dep_ = dep_time.split(sep=":")
Dep_hour = int(time_dep_[0])
Dep_min = int(time_dep_[1])

# Input for arrival time
date_arr = st.time_input("Arrival_Time", datetime.time(8,45))
arr_date = str(date_arr)
date_arr= arr_date.split(sep=":")
Arrival_hour = int(date_arr[0])
Arrival_min = int(date_arr[1])


#Duration
dur_hour = abs(Arrival_hour - Dep_hour)
dur_min = abs(Arrival_min - Dep_min)

#Total stops
Total_stops = st.number_input("Total stops : ", min_value = 1.0, max_value = 4.0, value = 1.0)

#Airline_feature
airline = st.selectbox("Select Airline : ", ["Jet Airways", "IndiGo", 'Air India', 'Multiple carriers','SpiceJet', 'Vistara','GoAir','Multiple carriers Premium economy','Trujet'])

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

Source = st.selectbox("Source:", ["Delhi", "Kolkata", "Mumbai", "Chennai"])

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

Destination = st.selectbox("Destination :" , ["Cochin", "Delhi", "New_Delhi", "Hyderabad", "Kolkata"])

if (Destination == 'Cochin'):

    Destination_Cochin = 1
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

elif (Destination == 'Delhi'):
    Destination_Cochin = 0
    Destination_Delhi = 1
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

elif (Destination == 'New_Delhi'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 1
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

elif (Destination == 'Hyderabad'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 1
    Destination_Kolkata = 0

elif (Destination == 'Kolkata'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 1

else:

    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0


user_input= pd.DataFrame(data= {"Total_Stops" :[Total_stops],"Journey_Day":[Journey_day], "Journey_Month":Journey_month, "Dep_Hour":[Dep_hour], "Dep_Min":[Dep_min], "Arrival_Hour":[Arrival_hour]
               ,"Arrival_Min":[Arrival_min],"Duration_Hours":[dur_hour],"Duration_Min":[dur_min],"Airline_Air India":[Air_India],"Airline_GoAir":[GoAir],
               "Airline_IndiGo":[IndiGo],"Airline_Jet Airways":[Jet_Airways],"Airline_Jet Airways Business":[Jet_Airways_Business],"Airline_Multiple carriers":[Multiple_carriers],
               "Airline_Multiple carriers Premium economy":[Multiple_carriers_Premium_economy],"Airline_SpiceJet":[SpiceJet],"Airline_Trujet":[Trujet],
               "Airline_Vistara":[Vistara],"Airline_Vistara Premium economy":[Vistara_Premium_economy],"Source_Chennai":[Source_Chennai],"Source_Delhi":[Source_Delhi],
               "Source_Kolkata":[Source_Kolkata],"Source_Mumbai":[Source_Mumbai],"Destination_Cochin":[Destination_Cochin],"Destination_Delhi":[Destination_Delhi],"Destination_Hyderabad":[Destination_Hyderabad],
               "Destination_Kolkata":[Destination_Kolkata],"Destination_New_Delhi":[Destination_New_Delhi]
                                
})

if st.button('Predict Price'):
    price = model.predict(user_input)
    st.success(f"Fare of the flight is Rs {price} ")
    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")        
    
