
# Text-to-Image Generator with Streamlit and Hugging Face

This application is a simple web interface built with Streamlit that allows users to generate images from text prompts using the Hugging Face Inference API with a Stable Diffusion XL model.

## Features

*   **Text-to-Image Generation:** Input a text prompt and get an AI-generated image.
*   **Hugging Face Integration:** Utilizes `stabilityai/stable-diffusion-xl-base-1.0` model via the Hugging Face Inference API.
*   **Secure API Key Handling:** Loads Hugging Face API token securely from Streamlit secrets.

## Setup and Deployment

Follow these steps to set up and deploy your application.

### 1. Get Your Hugging Face API Token

Before running the application, you'll need a Hugging Face API token.

1.  Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
2.  Generate a new token with at least **"Read"** access.
3.  Keep this token secure; you will need it for deployment.

### 2. Prepare Your GitHub Repository

1.  **Create a New GitHub Repository:**
    *   Go to [github.com/new](https://github.com/new).
    *   Give your repository a name (e.g., `streamlit-image-generator`).
    *   Choose whether it's public or private.
    *   Initialize with a `README.md` (optional, but good practice).

2.  **Add Application Files:**
    *   Create a file named `streamlit_app.py` in the root of your repository and paste the Streamlit application code into it.
    *   Create a file named `requirements.txt` in the root of your repository.

    **`streamlit_app.py` content:**
    ```python
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
    ```

    **`requirements.txt` content:**
    ```
    streamlit
    huggingface_hub
    Pillow
    