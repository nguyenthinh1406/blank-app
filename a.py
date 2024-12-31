import streamlit as st
st.header('BÉ IU CHỌN BAO LÌ XÌ ĐI')
col1,col2,col3,col4,col5 = st.columns(5)
option=0
col1.image('https://img.lovepik.com/element/40018/3664.png_860.png',width=200, use_container_width=550)
with col1.popover('Mở bao số 1'):
    st.markdown('Bé trúng 1000vnd 🧧')
    st.markdown('Cung hỷ phát tài.')
    st.markdown('Tấn tài tấn lộc.')
col2.image('https://img.lovepik.com/element/40018/3664.png_860.png',width=200, use_container_width=550)
with col2.popover('Mở bao số 2'):
    st.markdown('Bé trúng 2000vnd 💵')
    st.markdown('Cung chúc tân niên.')
    st.markdown('Sức khỏe vô biên.')
col3.image('https://img.lovepik.com/element/40018/3664.png_860.png',width=200, use_container_width=550)
with col3.popover('Mở bao số 3'):
    st.markdown('Bé trúng 3000vnd 💸')
    st.markdown('Tình chặt như keo')
    st.markdown('Dẻo dai hạnh phúc.')
col4.image('https://img.lovepik.com/element/40018/3664.png_860.png',width=200, use_container_width=550)
with col4.popover('Mở bao số 4'):
    st.markdown('Bé trúng 4000vnd 💰')
    st.markdown('Túi luôn đầy tiền.')
    st.markdown('Sung sướng như tiên.')
col5.image('https://img.lovepik.com/element/40018/3664.png_860.png',width=200, use_container_width=550)
with col5.popover('Mở bao số 5'):
    st.markdown('Bé trúng 5000vnd 🤑')
    st.markdown('Vạn sự như ý.')
    st.markdown('Đắc lộc toàn gia.')