import streamlit as st
import pickle 
import numpy as np
from PIL import Image

reg_model=pickle.load(open('reg_model.pkl','rb'))

st.markdown("""
    <style>
    body{
        backgroundColor="#aaa6e8";
        secondaryBackgroundColor="#f4f5f9";
        textColor="#060606";
    }
    </style>
        """,unsafe_allow_html=True
        )

def predict_price(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j):
    input=np.array([[q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j]])
    prediction_value=reg_model.predict(input)
    return float(prediction_value)
    # print(float(prediction_value))



def main():
    st.backgroundColor="#d3c2ff"
    st.markdown("<h1 style='text-align: center; color:black;'>House Price Predictor</h1>", unsafe_allow_html=True)
    # st.title("House Price Predictor")





    im=Image.open("C:/Users/Suruchi/Downloads/house-prices.jpg")
    st.image(im,width=700)


    col1,col2=st.columns(2)
    with col1:
        a=st.selectbox("Select the number of Bedrooms",("1","2","3","4","5"))
    with col2:
        b=st.number_input("Enter the number of bathoroms")
    col1,col2=st.columns(2)
    with col1:
        c=st.text_input("Enter sqft_living")
    with col2:
        d=st.text_input("sqft_lot")
    e=st.selectbox("Enter floors",("1.0","1.5","2.0"))
    col1,col2=st.columns(2)
    with col1:
        f=st.radio(label="Mark Waterfront ( 0 / 1 )",options=["0","1"])
    with col2:
        g=st.radio(label="Mark View ( 0 / 1 )",options=["0","1"])
    h=st.slider("Slide for condition(3-8)",3,10,5)
    st.write(h)
    col1,col2,col3=st.columns(3)
    with col1:
        i=st.selectbox("Selct the grade",("6","7","8","9","10","11"))
    with col2:
        j=st.text_input("Enter the sqft_above")
    with col3:
        k=st.text_input("Enter the sqft_base")

    col1,col2=st.columns(2)
    with col1:
        l=st.number_input("Enter the year bulit",1900)
    with col2:
        m=st.text_input("Enter the year of renovation")
    col1,col2=st.columns(2)
    with col1:
        n=st.number_input("Enter the latitude value",47.0)
    with col2:
        o=st.text_input("Enter the longitude value")
    with col1:
       p=st.text_input("Enter sqft_living15")
    with col2:
        q=st.text_input("sqft_lot15")
   
    output=""
    btn=st.button("Predict")
    if btn:
        output=predict_price(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)
        st.success("The price value of your house is nearly : {} $".format(output))
        last=Image.open("answer.png")
        st.image(last,width=590)
if __name__=='__main__':
    main()




