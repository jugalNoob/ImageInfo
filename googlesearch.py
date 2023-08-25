from googlesearch import search
import streamlit as st

st.title("Google Search Results")

data = st.text_input("Enter your search:")
num_results = 10  # Number of search results to show
st.button("search", data)
if data:
    
    st.write(f"Showing results for: {data}")

    for i, result in enumerate(search(data, num_results, advanced=True), 1):
        st.write(f"Result {i}")
        st.write("URL:", result.url)
        st.write("Title:", result.title)
        st.write("Description:", result.description)
        st.write("---")

