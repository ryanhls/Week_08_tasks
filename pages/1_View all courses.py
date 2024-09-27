import streamlit as st
import pandas as pd
import json

filepath = './data/courses-full.json'



with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

st.subheader("Format 1")
st.dataframe(dict_of_courses)



list_of_dict = []

for course_name, details_dict in dict_of_courses.items():
    list_of_dict.append(details_dict)

st.subheader("Format 2")
st.dataframe(list_of_dict)



st.subheader("Format 3")
df = pd.DataFrame(list_of_dict)
df
