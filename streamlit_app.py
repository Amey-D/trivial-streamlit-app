import streamlit as st

print("*** before ***")

"""
# Trivial Streamlit App

This is the most basic Streamlit app _ever_!
"""

v = st.slider("Choose a value", 0, 100)

"You selected:", v

"This is an update"


print("*** after, you selected: ", v)

st.write("pushing an update to github")
st.write("pushing another update to github")


