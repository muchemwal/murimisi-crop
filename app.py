from img_classification import murimisi_classification
from PIL import Image, ImageOps
import streamlit as st
import numpy as np
import os

st.set_page_config(
    page_title="Murimisi Image Classification",
    layout='wide',
    initial_sidebar_state='auto',
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.image("https://github.com/muchemwal/crop_disease_model/raw/main/images/murimisi_model_logo.jpg", use_column_width=True) 
#t1, t2 = st.beta_columns(2)
#with t1:
#    st.markdown('# Keras model for multi-label classification')
#
#with t2:
#    st.write("")
#    st.write("")
#    st.write("""
#    **Murimisi crop disease ML Webap ** | Data science team
#    """)
st.write("")
st.markdown("""
The Keras model used in this app is a supervised learning algorithm that supports multi-label classification. 
It takes an image as input and outputs one or more labels assigned to that image. It uses a convolutional neural network 
(ResNet) that can be trained from scratch using Google's Teachable Machine. We have focused on Maize ( *Common rust, Northen leaf blight, Gray leaf spot*) and Potatoe (*Late blight, Early blight*) crops for now.   
For additional information please contact **datascience@murimisi.com** or visit https://www.murimisi.com.  
""")


st.sidebar.header('User Input')
#data = st.sidebar.file_uploader('Upload here',type='csv')
st.sidebar.markdown("""
[Example crop input file](https://github.com/muchemwal/crop_disease_model/blob/main/images/com_rust.jpg)
""")
#st.text("Upload a Crop Image for disease image classification")



uploaded_file = st.sidebar.file_uploader("Choose a 🌿 crop image ...", type="jpg")

st.sidebar.write('Summary of the model:')
st.sidebar.image('model_plot.png', use_column_width = True)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded a Crop 🌿 leaf image.', use_column_width=False)
    st.write("")
    st.write("Classifying...")
    # run the inference
    label = murimisi_classification(image, 'keras_model.h5')
    if label == 0:
        st.write(" The 🌽 Maize crop has ** Common rust**.") # image from https://emojipedia.org/potato/
        st.write(" **Causes**: Common rust is caused by the fungus Puccinia sorghi. Late occurring infections have limited impact on yield.")
        st.write("**Common Rust Fact Sheet**: https://fieldcrops.cals.cornell.edu/sites/fieldcrops.cals.cornell.edu/files/shared/documents/rust_factsheet.pdf")
        st.markdown('## Management Strategies')
        st.write("**> ** The use of resistant hybrids is the primary management strategy for the control of common rust. Apply foliar fungicide sprays e.g Abacus, Amistar, Bravo, Duett and Score when lesions occur on 1/3 of the leaves before pollination")
        #Display the input image using matplotlib
        #my_img = Image.open(os.path.join('D:\downloads\dev\maize_disease\model files\converted_keras', 'abacus.jpg'))
        abacus_img = Image.open('abacus.jpg')
        amistar_img = Image.open('amistar.jpg')
        abacus_resized = abacus_img.resize((100, 100)) #cv2.resize(my_img, dim, interpolation=cv2.INTER_AREA)
        amistar_resized = amistar_img.resize((100, 100))
        Abacus = '[Buy Abacus](https://leroymerlin.co.za/complete-350sc-50ml-81426272)'
        Amistar = '[Buy Amistar](https://leroymerlin.co.za/complete-350sc-50ml-81426272)'
        st.write("**> **Pesticide")
        t01,mid,t02,t03 = st.beta_columns([1,1,1,20])
        with t01:
            st.image(abacus_resized)
        with t02:
            st.markdown(Abacus, unsafe_allow_html=True)
        with t03:
            st.write("**R150**")
        t11,mid,t12,t13 = st.beta_columns([1,1,1,20])
        with t11:
            st.image(amistar_resized)
        with t12:
            st.markdown(Amistar, unsafe_allow_html=True)
        with t13:
            st.write("**R150**")
        #st.image("https://media.leroymerlin.co.za/media/306449/format/jpg/resize/566x566", caption='Abacus.', width = 300, height = 100)
        #st.markdown(Abacus, unsafe_allow_html=True)
        #st.write("https://leroymerlin.co.za/complete-350sc-50ml-81426272")
    if label == 1:
        st.write("The 🌽 Maize crop is healthy")
    if label == 2:
        st.write("The 🌽 Maize crop has Northen leaf blight")
        st.write(" **Causes**: Northern corn leaf blight caused by the fungus Exerohilum turcicum.")
        st.write("**Northen leaf blight Fact Sheet**: https://fieldcrops.cals.cornell.edu/sites/fieldcrops.cals.cornell.edu/files/shared/documents/nclb_factsheet.pdf")
        st.markdown('## Management Strategies')
        st.write("**> ** The use of resistant hybrids is the primary management strategy for the control of Northen leaf blight. Apply foliar fungicide sprays e.g Abacus, Amistar, Bravo, Duett and Score when lesions occur on 1/3 of the leaves before pollination")
        #Display the input image using matplotlib
        abacus_img = Image.open('abacus.jpg')
        amistar_img = Image.open('amistar.jpg')
        abacus_resized = abacus_img.resize((100, 100))
        amistar_resized = amistar_img.resize((100, 100))
        Abacus = '[Buy Abacus](https://leroymerlin.co.za/complete-350sc-50ml-81426272)'
        Amistar = '[Buy Amistar](https://leroymerlin.co.za/complete-350sc-50ml-81426272)'
        st.write("**> ** Pesticide")
        t01,mid,t02,t03 = st.beta_columns([1,1,1,20])
        with t01:
            st.image(abacus_resized)
        with t02:
            st.markdown(Abacus, unsafe_allow_html=True)
        with t03:
            st.write("**R150**")
        t11,mid,t12,t13 = st.beta_columns([1,1,1,20])
        with t11:
            st.image(amistar_resized)
        with t12:
            st.markdown(Amistar, unsafe_allow_html=True)
        with t13:
            st.write("**R150**")
    if label == 3:
        st.write("The 🌽 Maize crop has Gray leaf spot")
        st.write(" **Causes**: Gray leaf spot is caused by the fungus Cercospora zeae-maydis.")
        st.write(" **Management Strategies**: Management strategies for gray leaf spot include tillage, crop rotation and planting resistant hybrids.")
        st.write("**Gray leaf spot Fact Sheet**: https://fieldcrops.cals.cornell.edu/sites/fieldcrops.cals.cornell.edu/files/shared/documents/grayleafspot_factsheet.pdf")

    if label == 4:
        st.write("The 🥔 Potato crop is healthy")
    if label == 5:
        st.write("The Potato crop has Late blight")
        st.write("**Causes**: Late blight is a serious disease of potato family (Solanaceous) crops worldwide, caused by the pathogen Phytophthora infestans. ")
        st.write(" **Management Strategies**: Late blight epidemics are much more likely to occur during periods of extended leaf wetness. Therefore, production of tomatoes in high tunnels with drip irrigation should dramatically reduce late blight risk by eliminating the contribution of rain and overhead irrigation to leaf wetness.")
        st.write("**Late blight Fact Sheet**: http://www.pestnet.org/fact_sheets/potato_late_blight_265.htm")

    if label == 6:
        st.write("The 🥔 Potato crop has Early blight")
        st.write("**Causes**: Early blight (EB) is a disease of potato caused by the fungus Alternaria solani.")
        st.write(" **Management Strategies**: (1) Plant only diseasefree, certified seed. (2) Follow a complete and regular foliar fungicide spray program. (3) Practice good killing techniques to lessen tuber infections. (4) Allow tubers to mature before digging, dig when vines are dry, not wet, and avoid excessive wounding of potatoes during harvesting and handling. (5) Plow underall plant debris and volunteer potatoes after harvest. (6) Avoid replanting potatoes (and tomatoes or eggplants) in the affected fields for at least 2 years if severe outbreaks have been experienced. (7) Although no cultivar is immune to EB, several cultivars are moderately resistant and should be planted if blight is a continuing problem. ")
        st.write("**Early blight Fact Sheet**: https://www.pestnet.org/fact_sheets/tomato_early_blight_211.htm")


