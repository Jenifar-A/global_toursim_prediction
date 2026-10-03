import joblib
import streamlit as st

model = joblib.load("last.pkl")

st.title("✈️ Global Tourism Trend Analysis 🌍")
st.header("💰 Tourism Spending Prediction System")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Enter Age", min_value=1, value=None, placeholder="Type your age here..."
    )

    gender_input = st.selectbox(
        "Select Gender",
        ["Male", "Female", "Other"],
        index=None,
        placeholder="Choose Gender",
    )
    gender_mapping = {"Male": 1, "Female": 0, "Other": 2}
    gender = gender_mapping.get(gender_input)

    country_input = st.selectbox(
        "Select Country of Origin",
        ["Australia", "USA", "India", "UK", "Japan", "UAE", "Germany"],
        index=None,
        placeholder="Choose Country",
    )
    country_mapping = {
        "Australia": 0,
        "USA": 1,
        "India": 2,
        "UK": 3,
        "Japan": 4,
        "UAE": 5,
        "Germany": 6,
    }
    country = country_mapping.get(country_input)

    destination_input = st.selectbox(
        "Select Destination Type",
        ["Historical", "Adventure", "Mountain", "Beach", "City Break"],
        index=None,
        placeholder="Choose Destination Type",
    )
    destination_mapping = {
        "Historical": 0,
        "Adventure": 1,
        "Mountain": 2,
        "Beach": 3,
        "City Break": 4,
    }
    destination = destination_mapping.get(destination_input)

with col2:
    travel_duration = st.number_input(
        "Enter Travel Duration Days",
        min_value=1,
        value=None,
        placeholder="Type days here...",
    )

    accommodation_input = st.selectbox(
        "Select Accommodation Type",
        ["Luxury Resort", "Airbnb", "Hostel", "Budget Hotel"],
        index=None,
        placeholder="Choose Accommodation",
    )
    accommodation_mapping = {
        "Luxury Resort": 0,
        "Airbnb": 1,
        "Hostel": 2,
        "Budget Hotel": 3,
    }
    accommodation = accommodation_mapping.get(accommodation_input)

    travel_season_input = st.selectbox(
        "Select Travel Season",
        ["Off-Peak", "Shoulder", "Peak"],
        index=None,
        placeholder="Choose Season",
    )
    season_mapping = {"Off-Peak": 0, "Shoulder": 1, "Peak": 2}
    travel_season = season_mapping.get(travel_season_input)

    flights_input = st.selectbox(
        "Pre-booked Packages",
        ["Yes", "No"],
        index=None,
        placeholder="Select Yes/No",
    )
    included_flights = 1 if flights_input == "Yes" else 0

st.write("")

if st.button("Predict Spending"):

    # Checking if ANY field is empty before predicting
    inputs_list = [
        age,
        gender_input,
        country_input,
        destination_input,
        travel_duration,
        accommodation_input,
        travel_season_input,
        flights_input,
    ]

    if any(item is None for item in inputs_list):
        st.warning("Please fill in ALL the fields before predicting!")
    else:
        input_data = [[
            age,
            gender,
            country,
            destination,
            travel_duration,
            accommodation,
            travel_season,
            included_flights,
        ]]

        prediction = model.predict(input_data)

        spending_in_usd = prediction[0]
        spending_in_inr = spending_in_usd * 83.5

        st.write("### Predicted Spending Details:")
        st.success(f"₹ {spending_in_inr:.2f} Indian Rupees")