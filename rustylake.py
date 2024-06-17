import streamlit as st
st.title('Welcome')
st.divider()

col1, col2 = st.columns(2)
with col1:
    with open('all is found take 3.mp4', 'rb') as all_is_found:
        all_is_found_bytes = all_is_found.read()
        st.video(all_is_found_bytes)
    st.write(':grey[回忆之湖]')
    st.caption('All is found')
    st.caption('_Kristen Anderson-Lopez, Robert Lopez_')

with col2:
    with open('we will rock you.mp4', 'rb') as rockyou:
        rockyou_bytes = rockyou.read()
        st.video(rockyou_bytes)
    st.write(':grey[家庭乐队]')
    st.caption('We will rock you')
    st.caption('_Queen_')