import streamlit as st
from PIL import Image
from prediction import mri_classification
import os

# Function to set background color using st.markdown
def set_background_color(color: str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Title and header
st.title("Brain Tumor or Healthy Brain")
st.header("Brain Tumor MRI Classifier")
st.text("Upload a brain MRI Image for image classification as tumor or Healthy Brain")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Credits
st.markdown("""###### Credits:
- Osama Raheem
- Dawood Shahzad
- KongKhan
""")

# If a file is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("")
    app_folder = os.path.dirname(os.path.abspath(__file__))
    mri_classifier_path = os.path.join(app_folder, "mri_classifier.h5")
    label = mri_classification(image, mri_classifier_path)
    
    st.write("Result:")
    
    # Dynamically change background color based on the result
    if label == 0:
        set_background_color("#d4edda")  # Green for a healthy brain
        st.write('<p style="color:green;">The MRI scan shows a healthy brain</p>', unsafe_allow_html=True)
    else:
        set_background_color("#f8d7da")  # Red for a brain tumor
        st.write('<p style="color:red;">The MRI scan detects a brain tumor</p>', unsafe_allow_html=True)
