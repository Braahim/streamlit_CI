import snowflake.connector 
import streamlit as st


def main():
    st.header('Breakfast Menu')
    st.text('Omega 3 & Blueberry Oatmeal')
    st.text('Kale, Spinach & Rocket Smoothie')
    st.text('Hard-Boiled Free-Range Egg')
    st.session_state.number = st.number_input(label= "Column number",min_value=1,step=1)

    if st.session_state.number:
        for i in range(st.session_state.number):
            st.text_input('column name' + str(i))
    
    with st.form("my_form"):
        st.write("Inside the form")

            
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")



        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")

if __name__ == "__main__":
  main()
