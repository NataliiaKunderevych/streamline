import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

if st.button('Say hello'):
    st.write('Why hello here')
else:
    st.write('Good bye')
st.write('Hello world!')

st.title('Main Page Content')

st.header('st.write')

#example 1

st.write('Hello,*World!* :sunglasses:')
st.markdown("*Streamlit* is a **really** ***cool!***")
st.markdown(''':red[Streamlit] :orange[can] write text in :rainbow[rainbow] colors and :blue-background[highlight] the text''')
multi='''If you end the line with two spaces,  
            a soft return is used for the next line.   
            
            Two or more newline characters in a row will results in a hard return'''
st.markdown(multi)

st.caption('This is a string that explains something above')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses')

#example 2

st.write(1234)

#example 3

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':([10,20,30,40])
})

st.write(df)

# Sidebar selection
#st.sidebar.header('Navigation')
#option=st.sidebar.selectbox('Choose a page:', ['Home','Dasboard','Settings'])
#st.sidebar.slider('Data range',2010,2025,(2018,2022))

# example 4 You can pass arguments

st.write('Below is a dataframe',df, 'Above is a dataframe')

#example 5  Display the plot

df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c', tooltip=['c']
)
st.write(c)

#st.sidebar.button('Logout')

#Example 5 Session State

if 'count' not in st.session_state:
    st.session_state.count=0
if st.button('increase'):
    st.session_state.count+=1
st.write(f"Count:{st.session_state.count}")

# Show Hide SideBar

#initialize toggle in a session state
if 'sidebar_mode' not in st.session_state:
    st.session_state.sidebar_mode='Profile'

#Switch content

mode=st.radio(('Select mode'),['Profile','Settings','Info'])
st.session_state.show_side_bar = mode

#Sidebar content
with st.sidebar:
        st.markdown(f"{st.session_state.sidebar_mode} ***Section*** ")
        if mode=='Profile':
            st.text_input('Name')
        elif mode=='Settings':
            st.slider('Volume',0,100)
        else:
            st.write('This is the Information panel')

