import streamlit as st
st.title('Demo App')
st.write('This is a Demo App')

with st.sidebar:
  st.write('This is a sidebar')

col1,col2 = st.columns(2)
with col1:
  a = st.number_input('Enter a Value',value = 10)
with col2:
  b = st.text_input('Enter a text')
sub = st.button(label = 'Submit')

if sub :
  st.write(a)
  st.write(b)
print(a)
print(b)
