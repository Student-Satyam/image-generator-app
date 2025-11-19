Streamlit Text-to-Image Generator (CPU Edition)

This repository contains a simple Streamlit application for generating images from text prompts using the Stable Diffusion v1.5 model.

Crucial Note on Deployment (Streamlit Cloud Free Tier):
This application is designed to use the powerful runwayml/stable-diffusion-v1-5 model entirely on the CPU. While this avoids costly GPU requirements, the model is very large (~5GB) and requires significant computational resources.

Expected Performance:

Local Machine (Modern CPU/Decent RAM): Generation time is typically 1-3 minutes.

Streamlit Cloud (Free Tier): Generation is highly unstable. It will likely take 5+ minutes, often exceeding memory limits and timing out. This is a demonstration of how to configure the files, but it is not recommended for production use on free cloud hosting.

Requirements

The requirements.txt file lists all necessary Python libraries. These will be automatically installed by Streamlit Cloud during deployment.

How to Deploy on Streamlit Cloud

Repository Setup: Create a new GitHub repository and upload these three files: streamlit_app.py, requirements.txt, and README.md.

Streamlit Cloud: Go to your Streamlit Cloud dashboard and click "New app."

Link Repository: Select your newly created repository and choose the main branch.

File Path: Ensure the "Main file path" is set to streamlit_app.py.

Deploy: Click "Deploy!" and wait for the application to build. (The build process may take a long time as it downloads the large model weights.)

Configuration in streamlit_app.py

Caching: The @st.cache_resource decorator ensures the large model is loaded only once when the application starts, improving efficiency after the initial load.

CPU Mode: The line pipe.to("cpu") explicitly tells the PyTorch/Diffusers library to use the CPU, which is mandatory on the free Streamlit Cloud tier.
