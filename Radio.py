# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:06:14 2024

@author: user
"""

import streamlit as st 
import pickle


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img5.pic.in.th/file/secure-sv1/smsk-1e26f337bb6ec6813.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: black ; font-size: 25px ;'>Sakhon Allergy Prediction tool(S.A.P.)</h1>", unsafe_allow_html=True)


filename = "lastfinalmodel.pickle"
loaded_model = pickle.load(open(filename, "rb"))

s=[]

#st.title(r"$\textsf{\small ประเมินความเสี่ยงต่อการแพ้สารทึบรังสี }$")
#st.title('ประเมินความเสี่ยงต่อการแพ้สารทึบรังสี')


q1 = st.radio("ผู้ป่วยแพ้Iopamiroหรือไม่", ["ไม่แพ้" , "แพ้"],  horizontal = True)
if q1 == "ไม่แพ้" :
    a = int(0)
else :
    a = int(1)
    
q2 = st.radio("ผู้ป่วยแพ้Iopromideหรือไม่" , ["ไม่แพ้" , "แพ้"],  horizontal = True)
if q2 == "ไม่แพ้" :
    b = int(0)
else :
    b = int(1)
    
q3 = st.radio("ผู้ป่วยแพ้Iobitridolหรือไม่" , ["ไม่แพ้" , "แพ้"],  horizontal = True)
if q3 == "ไม่แพ้" :
    c = int(0)
else :
    c = int(1)
    
q4 = st.radio("ผู้ป่วยแพ้Iodixanol(Visipaque)หรือไม่" , ["ไม่แพ้" , "แพ้"],  horizontal = True)
if q4 == "ไม่แพ้" :
    d = int(0)
else :
    d = int(1)
    
q5 = st.radio("ผู้ป่วยแพ้Iomeprol(Iomeron)หรือไม่" , ["ไม่แพ้" , "แพ้"],  horizontal = True)
if q5 == "ไม่แพ้" :
    e = int(0)
else :
    e = int(1)  
    
q6 = st.radio("ผู้ป่วยกินยาแก้แพ้หรือไม่" , ["ไม่กิน" , "กิน"],  horizontal = True)  
if q6 == "ไม่กิน" :
    f = int(0)
else :
    f = int(1)   
    
q7 = st.radio("ผู้ป่วยกินยาแก้หอบหืด(Theophylline)หรือไม่" , ["ไม่กิน" , "กิน"],  horizontal = True)  
if q7 == "ไม่กิน" :
    g = int(0)
else :
    g = int(1)   
    
q8 = st.radio("ผู้ป่วยเป็นโรคเอดส์หรือไม่" , ["ไม่" , "เป็น"],  horizontal = True)  
if q8 == "ไม่" :
    h = int(0)
else :
    h = int(1)   
    
q9 = st.radio("ผู้ป่วยเป็นความดันโลหิตสูงหรือไม่" , ["ไม่" , "เป็น"],  horizontal = True)  
if q9 == "ไม่" :
    i = int(0)
else :
    i = int(1) 
    
q10 = st.radio("ผู้ป่วยเป็นโรคหัวใจขาดเลือดหรือไม่" , ["ไม่" , "เป็น"],  horizontal = True)  
if q10 == "ไม่" :
    j = int(0)
else :
    j = int(1) 
    
if st.button('ประเมินความเสี่ยง'):
    s=[a,b,c,d,e,f,g,h,i,j]
    array = loaded_model.predict([s])
    k=loaded_model.predict_proba([s]).round(2)
    if array[0] == 0: 
           st.code(f"""ผู้ป่วยมีความเสี่ยงน้อยที่จะแพ้สารทึบแสง ค่าความเชื่อมั่น {k[0][0]*100}%""")
    else:
           st.code(f"""ผู้ป่วยมีความเสี่ยงที่จะแพ้สารทึบแสง ควรpre-med ค่าความเชื่อมั่น {k[0][1]*100}%""")

           

            
    





    
