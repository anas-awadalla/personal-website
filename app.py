import streamlit as st

# make a personal website with sections for name, bio, publications, work experience, and contact info

st.image('profile.jpg', width=300)        
st.title("Anas Awadalla")

st.write("📫 anasa2@cs.washington.edu | 🐦 [Twitter](https://twitter.com/anas-awadalla) | 🔗 [LinkedIn](https://www.linkedin.com/in/anas-awadalla/)")

# make a section for bio
st.header("👋🏽 Bio")
st.write("""I am a senior at the University of Washington studying Computer Science, advised
         by [Prof. Ludwig Schmidt](http://people.csail.mit.edu/ludwigs/). 
         I do research in natural language processing, robustness, and vision+language models.""")

# make a section for publications
st.header("📄 Publications")
st.write("[Exploring The Landscape of Distributional Robustness for Question Answering Models](https://arxiv.org/abs/2210.12517)")
st.write("**Anas Awadalla**, Mitchell Wortsman, Gabriel Ilharco, Sewon Min, Ian Magnusson, Hannaneh Hajishirzi, Ludwig Schmidt")
st.write("**EMNLP Findings 2022**")

st.write("")

st.write("[Reliable and Trustworthy Machine Learning for Health Using Dataset Shift Detection](https://arxiv.org/abs/2110.14019)")
st.write("Chunjong Park, **Anas Awadalla**, Tadayoshi Kohno, Shwetak Patel")
st.write("**NeurIPS 2021**")

# make a section for work experience    
st.header("👨🏽‍💻 Work Experience")
st.write("Software Engineering Intern at Stripe in **Summer 2022**")
st.write("")

st.write("Software Engineering Intern at Amazon in **Summer 2021**")

st.write("")

st.write("Machine Learning Engineering Intern at Allen Institute for AI Incubator startup in **Spring 2021**")

st.header("👨🏽‍🏫 Teaching Experience")
st.write("Teaching Assistant for [CSE 344](https://sites.google.com/cs.washington.edu/cse344-21au/home?pli=1) in **Fall 2021**")
