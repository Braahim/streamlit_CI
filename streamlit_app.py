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

import snowflake.connector 

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
if 'my_cnx' not in st.session_state:
  my_cur = st.session_state.my_cnx.cursor()
my_cur.execute("use warehouse pc_rivery_wh")
#sql = 'create or replace table handled as (select "DATA":"%s"::STRING as %s, "DATA":"%s"::STRING as %s, "DATA":"%s"::STRING as %s, "DATA":"%s"::String as %s,"DATA":"%s"::STRING as %s from test);'
my_cur.execute('create or replace table handled as (select "DATA":"%s"::STRING as %s, "DATA":"%s"::STRING as %s, "DATA":"%s"::STRING as %s,"DATA":"%s"::String as %s,"DATA":"%s"::STRING as %s from test);'
,st.session_state.l[0],st.session_state.l[0],st.session_state.l[1],st.session_state.l[1],st.session_state.l[2],st.session_state.l[2],st.session_state.l[3],st.session_state.l[3],st.session_state.l[4],st.session_state.l[4])


if __name__ == "__main__":
  main()
