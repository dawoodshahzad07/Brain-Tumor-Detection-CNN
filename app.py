import streamlit as st
from PIL import Image
from prediction import mri_classification
import os

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
        st.markdown(
            """
            <style>
            .reportview-container {
                background-color: #d4edda;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write('<p style="color:green;">The MRI scan shows a healthy brain</p>', unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <style>
            .reportview-container {
                background-color: #f8d7da;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write('<p style="color:red;">The MRI scan detects a brain tumor</p>', unsafe_allow_html=True)
