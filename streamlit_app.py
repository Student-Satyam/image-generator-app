
import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image

# Securely load the Hugging Face API token from Streamlit secrets
try:
    HF_API_TOKEN = st.secrets["HF_API_TOKEN"]
except KeyError:
    st.error("HF_API_TOKEN not found in Streamlit secrets. Please add it to your Streamlit secrets file.")
    st.stop()

# Initialize the Hugging Face Inference Client
client = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0", token=HF_API_TOKEN)

# Set the title of the Streamlit app
st.title("Text-to-Image with Stable Diffusion XL")

# Create a text input field for the user to enter their image prompt
prompt = st.text_input("Enter your image prompt:", "3D cute robot reading a book")

# Create a button for generating the image
if st.button("Generate Image"):
    if prompt:
        with st.spinner('Generating image...'):
            try:
                # Generate the image
                img = client.text_to_image(prompt=prompt)
                # Display the generated image
                st.image(img, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error generating image: {e}")
    else:
        st.warning("Please enter a prompt to generate an image.")
