import streamlit as st

# Function for Distance Conversion
def distance_convertor(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Function for Temperature Conversion
def temperature_convertor(from_unit, to_unit, value):
    if from_unit == "celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "celsius":
        result = (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "celsius":
        result = value  # If both units are Celsius, just return the same value
    elif from_unit == "Fahrenheit" and to_unit == "Fahrenheit":
        result = value  # If both units are Fahrenheit, just return the same value
    else:
        result = value  # You can add more units and conversions here
    return result

# Function for Weight Conversion
def weight_convertor(from_unit, to_unit, value):
    units = {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Function for Pressure Conversion
def pressure_convertor(from_unit, to_unit, value):
    units = {
        "pascal": 1,
        "Hectopascal": 100,
        "Kilopascal": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# UI
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

# Handling Distance Conversion
if category == "Distance":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = distance_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Handling Temperature Conversion
elif category == "Temperature":
    from_unit = st.selectbox("From", ["celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["celsius", "Fahrenheit"])
    value = st.number_input("Enter Value", min_value=-273.15, step=0.1)  # Celsius can't be below absolute zero

    if st.button("Convert"):
        result = temperature_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Handling Weight Conversion
elif category == "Weight":
    from_unit = st.selectbox("From", ["kilograms", "grams", "pounds", "ounces"])
    to_unit = st.selectbox("To", ["kilograms", "grams", "pounds", "ounces"])
    value = st.number_input("Enter Value")

    if st.button("Convert"):
        result = weight_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Handling Pressure Conversion
elif category == "Pressure":
    from_unit = st.selectbox("From", ["pascal", "Hectopascal", "Kilopascal", "Bar"])
    to_unit = st.selectbox("To", ["pascal", "Hectopascal", "Kilopascal", "Bar"])
    value = st.number_input("Enter Value")

    if st.button("Convert"):
        result =pressure_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


