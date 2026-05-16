import streamlit as st
import requests

st.set_page_config(page_title="SHL Recommender")

st.title("SHL Assessment Recommender")

query = st.text_input(
    "Enter hiring requirement or job role"
)

if st.button("Get Recommendations"):
    response = requests.post(
    "https://shl-api-katu.onrender.com/chat",
    json={"query": query}
    )
    data = response.json()

    st.subheader("AI Response")
    st.write(data["response"])

    st.subheader("Recommended Assessments")

    for item in data["recommended_assessments"]:
        st.markdown(f"### {item['name']}")
        st.write(f"Category: {item['category']}")
        st.write(f"Skills: {', '.join(item['skills'])}")
        st.write(f"Description: {item['description']}")
        st.write("---")