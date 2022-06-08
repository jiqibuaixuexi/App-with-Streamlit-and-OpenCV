# Core Okgs
import streamlit as st
import cv2
from PIL import Image,ImageEnhance
import numpy as np
import os

@st.cache
def load_img(img):
    im = Image.open(img)
    return im


def main():
    """Face Detection App"""

    st.title("Face Detection App")
    st.text("Build with Streamlit and OpenCV")

    activities = ["Detection","About"]
    choice = st.sidebar.selectbox("Select Activity",activities)

    if choice =="Detection":
        st.subheader("Face Detection")

        image_file = st.file_uploader("Upload Image",type = ['jpg','png','jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.write(type(our_image))
            st.image(our_image)
        
        enhance_type = st.sidebar.radio("Enhance Type",["Original","Gray-Scale","Contrast","Brightness","Blurring"])
        if enhance_type == "Gray-Scale":
            new_img = np.array(our_image.convert('RGB'))
            img = cv2.cvtColor(new_img,1) #好像是选择转灰度之后保留哪个channel     
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            # st.write(new_img)
            st.image(gray)

        elif enhance_type == "Contrast":
            c_rate= st.sidebar.slider("Contrast",0.5,3.5)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)

        elif enhance_type == "Brightness":
            c_rate= st.sidebar.slider("Brightness",0.5,3.5)
            enhancer = ImageEnhance.Brightness(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)            

        elif enhance_type == "Blurring":
            new_img = np.array(our_image.convert('RGB'))
            blur_rate= st.sidebar.slider("Blurring",0.5,3.5)
            img = cv2.cvtColor(new_img,1) #好像是选择转灰度之后保留哪个channel     
            blur_img = cv2.GaussianBlur(img,(11,11),blur_rate)
            # st.write(new_img)
            st.image(blur_img)

        else:
            st.image(our_image,width=300)

        # Face Detection #TODO

    elif choice == "About":
        st.subheader("About")




if __name__=="__main__":
    main()