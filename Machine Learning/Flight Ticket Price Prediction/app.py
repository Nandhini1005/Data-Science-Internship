import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Flight Ticket Price Predictor",
    page_icon="✈️",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

#Model
model = joblib.load("flight_price_model.pkl")

# =========================
# SIDEBAR
# =========================
st.sidebar.title("✈️ Navigation")
page = st.sidebar.radio(
    "Go To",
    ["Home", "About", "Prediction", "Results"]
)

# =========================
# HOME PAGE
# =========================
if page == "Home":

    st.markdown(
        """
        <div class='hero-section'>
            <h1>✈️ Flight Ticket Price Prediction</h1>
            <p>
                Predict airline ticket prices instantly using Machine Learning.
            </p>
        </div>
        """,
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class='info-card'>
                <h3>⚡ Fast Prediction</h3>
                <p>Instant airfare estimation using trained ML model.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='info-card'>
                <h3>📊 Accurate Results</h3>
                <p>Uses Random Forest Regressor for better prediction.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """<div class='info-card'>
                <h3>🌍 Real Airline Data</h3>
                <p>Based on actual flight dataset records.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.image(
        "https://images.unsplash.com/photo-1436491865332-7a61a109cc05",
        use_container_width=True
    )

#About Page
elif page == "About":

    st.markdown("<h1 class='main-title'>About SkyFare AI</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='about-box'>

        <h2>✈️ Smarter Flight Booking Starts Here</h2>

        <p>
        SkyFare AI helps travelers make better booking decisions by predicting
        airline ticket prices before they book. Using advanced Machine Learning,
        our system analyzes travel patterns, airline trends, booking timings,
        and route information to estimate expected airfare prices instantly.
        </p>

        <p>
        Whether you're planning a business trip, vacation, or last-minute journey,
        our intelligent prediction engine provides quick fare insights that help
        you decide the best time to book your flight.
        </p>

        <h3>🌍 What We Offer</h3>

        <ul>
            <li>Real-time airfare estimation</li>
            <li>Smart price prediction using AI</li>
            <li>Easy flight search experience</li>
            <li>Clean and modern airline-style interface</li>
            <li>Fast and reliable prediction system</li>
        </ul>

        <h3>💡 Why Use SkyFare AI?</h3>

        <p>
        Flight ticket prices change frequently based on demand, travel season,
        airline availability, booking time, and route popularity. SkyFare AI
        simplifies this complexity by giving users a quick estimate of ticket
        pricing trends using data-driven intelligence.
        </p>

        <p>
        Our goal is to make flight booking smarter, faster, and more transparent
        for travelers around the world.
        </p>

        <br>

        <p style='text-align:center; font-size:18px;'>
        ✈️ Travel Smart • Predict Better • Save More
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
#Prediction Page
elif page == "Prediction":

    st.markdown("<h1 class='main-title'>🎫 Book Your Flight</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        airline = st.selectbox(
            "Airline",
            ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India']
        )

        source_city = st.selectbox(
            "Source City",
            ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
        )

        departure_time = st.selectbox(
            "Departure Time",
            ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night']
        )

        stops = st.selectbox(
            "Stops",
            ['zero', 'one', 'two_or_more']
        )

        arrival_time = st.selectbox(
            "Arrival Time",
            ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night']
        )

    with col2:

        destination_city = st.selectbox(
            "Destination City",
            ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
        )

        travel_class = st.selectbox(
            "Class",
            ['Economy', 'Business']
        )
        duration = st.slider(
            "Duration (Hours)",
            1.0,
            50.0,
            5.0
        )

        days_left = st.slider(
            "Days Left Before Journey",
            1,
            50,
            10
        )

    if st.button("Predict Ticket Price"):

        input_data = pd.DataFrame({
            'airline': [airline],
            'source_city': [source_city],
            'departure_time': [departure_time],
            'stops': [stops],
            'arrival_time': [arrival_time],
            'destination_city': [destination_city],
            'class': [travel_class],
            'duration': [duration],
            'days_left': [days_left]
            })

        prediction = model.predict(input_data)[0]

        st.session_state['prediction'] = round(prediction, 2)

        st.success(f"Estimated Flight Ticket Price: ₹ {round(prediction, 2)}")

#Result Page
elif page == "Results":

    st.markdown("<h1 class='main-title'>📈 Prediction Result</h1>", unsafe_allow_html=True)

    if 'prediction' in st.session_state:

        prediction = st.session_state['prediction']

        st.markdown(
            f"""
            <div class='result-box'>
                <h2>✈️ Estimated Fare</h2>
                <h1>₹ {prediction}</h1>
                <p>Your AI-powered airfare prediction is ready.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if prediction < 5000:
            st.info("🔥 Best time to book! Prices are low.")

        elif prediction < 15000:
            st.warning("⚠️ Moderate pricing detected.")

        else:
            st.error("🚨 High airfare detected. Consider early booking.")

    else:
        st.warning("Please make a prediction first.")