import snowflake.connector 
import streamlit as st


def main():
    st.header('Breakfast Menu')
    st.text('Omega 3 & Blueberry Oatmeal')
    st.text('Kale, Spinach & Rocket Smoothie')
    st.text('Hard-Boiled Free-Range Egg')
    st.session_state.number = st.number_input(label= "Column number",min_value=1,step=1)
    st.session_state.l = []
    if st.session_state.number:
        for i in range(st.session_state.number):
           st.session_state.l.append(st.text_input('column name' + str(i)))
    
    if st.button("Créer le schéma"):
        st.text(st.session_state.l)

if __name__ == "__main__":
  main()
