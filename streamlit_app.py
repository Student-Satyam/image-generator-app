import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

st.title("Free Text-to-Image Generator (CPU Mode)")
st.subheader("Using `runwayml/stable-diffusion-v1-5`")

# CRITICAL WARNING for free cloud deployment
st.warning(
    "⚠️ **Performance Warning for Streamlit Cloud (Free Tier):** "
    "The Stable Diffusion v1.5 model is ~5GB and is running on CPU only. "
    "Generation will be extremely slow (often 5+ minutes or may fail due to timeouts/memory limits)."
    "For a better experience, consider using a much smaller model or a dedicated hosting service."
)

@st.cache_resource
def load_model():
    """Loads the Stable Diffusion pipeline and forces it onto the CPU."""
    try:
        # Load the model from Hugging Face
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32 # Use float32 for CPU compatibility
        )
        # Explicitly move to CPU
        pipe = pipe.to("cpu")
        st.success("Model loaded successfully (CPU mode).")
        return pipe
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()
        return None

pipe = load_model()

# User input for the prompt
prompt = st.text_input(
    "Enter your image prompt:",
    "A vintage, 3D, cute robot reading a book in a cozy library, highly detailed, photorealistic."
)

if st.button("Generate Image"):
    if pipe and prompt:
        with st.spinner("⏳ Generating... This will take a long time on CPU (5 minutes or more on free cloud hosting)."):
            try:
                # Generate the image
                image = pipe(prompt).images[0]
                
                # Display the results
                st.image(image, caption="Generated Image", use_column_width=True)
                st.balloons()
            except Exception as e:
                st.error(f"Image generation failed. This is often due to memory limits (OOM error) on free cloud tiers. Error: {e}")
