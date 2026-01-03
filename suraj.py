import streamlit as st
st.title("join SAH BHOJNALAYA ")
st.header("NOTE : Kam jitna pesa utna !")
name=st.text_input("enter your name")
fname=st.text_input("ente your father name")
adr=st.text_area("enter your address")
classdata=st.selectbox("enter your class :",(8,9,10,11,12))
button=st.button("done")
if button :
    st.markdown(f""" name{name}\nfatheer name={fname}\n address={adr}\nclass={classdata}""")