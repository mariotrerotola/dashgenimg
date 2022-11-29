import streamlit as st
import pandas as pd
import openai
import os

os.environ["OPENAI_API_KEY"] = "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" 

openai.api_key = "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"

frame_shape = ['cat eye','oversized','pilot','round','square','circular','oval']
lenses = ['gradient','mirrored','tinted']
color = ['blue','black','brown','green','grey','gold','metallic','multicolour','neutrals','neutrals','orange','pink','purple','red','silver','white','yellow']




season = st.sidebar.selectbox(
            "For which season are you designing your product?",
            ("Spring/Summer", "Autumn/Winter"),
        )

year = st.sidebar.selectbox(
        "For which year are you designing your product?",
        ("2022", "2023"),
    )

gender = st.sidebar.selectbox(
        "Who are you designing for?",("Male","Female","unisex")
    )

shape = st.sidebar.selectbox(
            "Frame shape",
            set(frame_shape),
        )

lenses = st.sidebar.selectbox(
        "Lenses type:",
        set(lenses),
    )

color = st.sidebar.selectbox(
        "Color:",set(color)
    )

query = color + " sunglasses " + " " + shape + " " + lenses + " " + gender + " "

def gen_img(query):
    image_resp = openai.Image.create(prompt=query, n=6, size="1024x1024")
    img_urls = [d['url'] for d in image_resp['data']]
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(img_urls[0])
        st.image(img_urls[1])

    with col2:
        st.image(img_urls[2])
        st.image(img_urls[3])



search = st.sidebar.button("Search", on_click=gen_img,args=(query, ))

data = pd.read_csv('data.csv', header=None)

data.rename(columns = {0:'property', 
                       1:'sentiment'}, 
            inplace = True)
frame_shape = ['cat eye','oversized','pilot','round','square','circular','oval']
lenses = ['gradient','mirrored','tinted']
color = ['blue','black','brown','green','grey','gold','metallic','multicolour','neutrals','neutrals','orange','pink','purple','red','silver','white','yellow']
p_list = {}
for i in frame_shape:
    p_list[i] = 'shape'
for i in lenses:
    p_list[i] = 'lenses'
for i in color:
    p_list[i] = 'color'
data['type'] = data['property'].apply(lambda x: p_list[x])
typedatas = []
for tp in data['type'].unique():
    typedata = data[data['type']==tp].sort_values(by=['sentiment'],ascending=False).iloc[0]
    typedatas.append(typedata)

st.header('Market Analytics')
col1, col2, col3 = st.columns(3)

col1.metric(typedatas[0]['property'], int(typedatas[0]['sentiment']*100))
col1.caption(typedatas[0]['type'])

col2.metric(typedatas[1]['property'], int(typedatas[1]['sentiment']*100))
col2.caption(typedatas[1]['type'])

col3.metric(typedatas[2]['property'], int(typedatas[2]['sentiment']*100))
col3.caption(typedatas[2]['type'])

