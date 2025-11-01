import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the NExt Days")
place = st.text_input("Place Name: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days to forecast")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} Weather Forecast for the next {days} days in {place}")

if place:
    # Get the temmperature/sky data
    try:
        filtered_data = get_data(place,days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]

            dates = [dict["dt_txt"]for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = { "Clear":"images/images.png", "Clouds":"images/download (1).jpeg",
                       "Rain":"images/images (1).png", "Snow":"images/download (2).jpeg"}

            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width = 100)
    except KeyError:
        st.write("No place found")