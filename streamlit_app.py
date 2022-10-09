import snowflake.connector 
import streamlit as st


def main():
    st.header('Breakfast Menu')
    st.text('Omega 3 & Blueberry Oatmeal')
    st.text('Kale, Spinach & Rocket Smoothie')
    st.text('Hard-Boiled Free-Range Egg')
    with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

if __name__ == "__main__":
  main()
