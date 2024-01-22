import streamlit as st
from urllib.parse import urlparse, parse_qs
import re
def extract_parameters(urls):
    parameters = set()

    for url in urls:
        # Parse the URL
        parsed_url = urlparse(url)

        # Extract query parameters from the URL
        query_params = parse_qs(parsed_url.query)

        # Add unique parameters to the set
        for param in query_params:
            parameters.add(param)

    return parameters

# User Input
# user_input_urls = [
#     "https://example.com?q=123",
#     "http://example.com/?s=12&a=nice",
#     "example.com?search=nice_finding",
#     "google.com?q=hello+mister"
# ]


def app():
    st.header("✂️ Extract Parameters",divider=True)
    inp = st.text_area(label="Enter URLs (one per line):",height=200,placeholder="Enter your urls here...")
    url_lines=[line.strip() for line in inp.split('\n') if line.strip()]
    if st.button("Extract"):
        if(inp!=""):
            print(type(inp))
            print(inp)
            # Extract parameters
            unique_parameters = extract_parameters(url_lines)
            # Initialize results_string as an empty string
            results_string = ""
            # Print the result
            for param in unique_parameters:
                print(f"{param}=")
                results_string += f"{param}=\n"
            # Display the results in a text_area
            st.text_area("Results", value=results_string,height=200)
        else:
            st.error("Please validate the required fields !!")