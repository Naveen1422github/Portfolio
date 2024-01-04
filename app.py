import streamlit as st
import time

st.title("Hi! I'm Naveen")
st.header('A Fresh Data Analyst')
st.subheader('Below are some of projects')

"## Experiments with python"

tab1, tab2 = st.tabs(["File Shortner", "First CSS Site"])


"## Web dev experiments"

tab1, tab2 = st.tabs(["First Html Site", "First CSS Site"])
# You can also use "with" notation:
with tab1:
    st.components.v1.iframe("https://naveen1422github.github.io/My-Cv/", height=300, scrolling=True)
    st.markdown("[Click here](https://naveen1422github.github.io/My-Cv/) to visit")

with tab2:
    st.components.v1.iframe("https://naveen1422github.github.io/My-first-css-site/", height=300, scrolling=True)
    st.markdown("[Click here](https://naveen1422github.github.io/My-first-css-site/) to visit")

# Insert containers separated into tabs:

st.markdown("[click here](https://www.loom.com/share/b46517a3e6b84d9aa5bf1aad2756a7d4?sid=5a5b02c1-4474-45ad-a37b-99bbaf9043e4) to visit")