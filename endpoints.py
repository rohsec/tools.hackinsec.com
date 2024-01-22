import streamlit as st
from urllib.parse import urlparse

def extract_endpoints(urls):
    endpoints = set()

    for url in urls:
        # Parse the URL
        parsed_url = urlparse(url)

        # Extract the path (endpoint) from the URL
        endpoint = parsed_url.path

        # Add the endpoint to the set
        endpoints.add(endpoint)

    return endpoints

def app():
    st.header("↗️ Extract Endpoints",divider=True)
# Streamlit User Input
    user_input_urls = st.text_area("Enter URLs (one per line):",height=200,placeholder="Enter your urls here...")

# Split the input into lines and remove empty lines
    url_lines = [line.strip() for line in user_input_urls.split('\n') if line.strip()]

    if st.button("Extract Endpoints"):
            if(user_input_urls!=""):
# Extract endpoints
                unique_endpoints = extract_endpoints(url_lines)

# Display the results in a new text_area
                st.text_area("Unique Endpoints", '\n'.join(sorted(unique_endpoints)))

            else:
                 st.error("Please validate the required fields !!")
                 st.info("The input should be in the form https://example.com/docs/")
