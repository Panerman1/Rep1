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
  c = st.selectbox(label = 'Choose',options = [A,B,C]
sub = st.button(label = 'Submit')

if sub :
  st.write(a)
  st.write(b)
  st.write(c)

print(a)
print(b)
print(c)
