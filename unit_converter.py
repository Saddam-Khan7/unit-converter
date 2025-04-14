# unit_converter.py

import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.title("🔄 Unit Converter")
st.markdown("Convert between different units of **Length**, **Weight**, and **Time**.")

# --- Conversion Dictionaries ---
length_units = {    
    "Meter": 1,
    "Kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Mile": 0.000621371,
    "Yard": 1.09361,
    "Foot": 3.28084,
    "Inch": 39.3701
}

weight_units = {
    "Kilogram": 1,
    "Gram": 1000,
    "Milligram": 1e6,
    "Pound": 2.20462,
    "Ounce": 35.274
}

time_units = {
    "Second": 1,
    "Minute": 1 / 60,
    "Hour": 1 / 3600,
    "Day": 1 / 86400,
    "Week": 1 / (86400 * 7)
}

# --- Conversion Functions ---
def convert_length(value, from_unit, to_unit):
    return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
    return value * weight_units[to_unit] / weight_units[from_unit]

def convert_time(value, from_unit, to_unit):
    return value / time_units[from_unit] * time_units[to_unit]

# --- Sidebar for Unit Category ---
st.sidebar.markdown("Developed by **Saddam Khan**")
category = st.sidebar.selectbox("Select Unit Category", ["Length", "Weight", "Time"])

# --- Input Section ---
st.subheader(f"{category} Converter")
value = st.number_input("Enter value:",)

if category == "Length":
    from_unit = st.selectbox("From:", list(length_units.keys()))
    to_unit = st.selectbox("To:", list(length_units.keys()))
    result = convert_length(value, from_unit, to_unit)

elif category == "Weight":
    from_unit = st.selectbox("From:", list(weight_units.keys()))
    to_unit = st.selectbox("To:", list(weight_units.keys()))
    result = convert_weight(value, from_unit, to_unit)

elif category == "Time":
    from_unit = st.selectbox("From:", list(time_units.keys()))
    to_unit = st.selectbox("To:", list(time_units.keys()))
    result = convert_time(value, from_unit, to_unit)

# --- Display Result ---
st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
