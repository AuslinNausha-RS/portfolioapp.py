import streamlit as st
#Title and description
st.title("MY PORTFOLIO")
st.write("A showcase of my skills and projects.")

st.header("About Me")
st.subheader("Hello,I am Auslin Nausha")
st.subheader("I am a student of AI&DS")

col1, col2=st.columns([1,2])
with col1:
    st.write(''':green[LANGUAGES KNOWN]
    \n:green[INTERESTED IN]
    \n:green[EXTRA CURICULAR ACTIVITIES]
    \n:green[KNOWN GAMES]
    \n:green[HOBBIES]
    \n:green[AIM]''')
with col2:
    st.write('''\n:  Python
    \n: Coding
    \n: Painting
    \n: Throw ball,Kabbadi
    \n: Listening to music
    \n: Data scientist''')
st.write(":blue[I am passionate about developing projects that solve real-world problems.]")
st.write("""
- **Email**: auslinnausha123@gmail.com
-**Linkedin**:[linkedin.com/in/auslinnausha](https://www.linkedin.com/in/auslin nausha-267b3489)
""")    







