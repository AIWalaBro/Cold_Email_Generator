import streamlit as st

st.title("📧 Lead Generator via Cold Email")
url_input = st.text_input("Enter a URL:", value = "https://jobs.nike.com/job/R-32222?from=job%20search%20funnel")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring manager , i am from AIWalaBro Company")
