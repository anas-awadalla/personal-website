import streamlit as st

st.image('profile.jpg', width=300)        
st.title("Anas Awadalla")

st.write("📫 anasa2@cs.washington.edu | 🐦 [Twitter](https://twitter.com/anas_awadalla) | 🔗 [LinkedIn](https://www.linkedin.com/in/anas-awadalla/)")

# make a section for bio
st.header("👋🏽 Bio")
st.write("""I am a senior at the University of Washington studying computer science, advised
         by [Prof. Ludwig Schmidt](http://people.csail.mit.edu/ludwigs/). 
         I do research in natural language processing, robustness, and vision language models.""")

# make a section for publications
st.header("📄 Publications")
st.markdown("##### Exploring The Landscape of Distributional Robustness for Question Answering Models")
st.write("**Anas Awadalla**, Mitchell Wortsman, Gabriel Ilharco, Sewon Min, Ian Magnusson, Hannaneh Hajishirzi, Ludwig Schmidt")
st.write("**EMNLP Findings 2022**")
st.write("[paper](https://arxiv.org/abs/2210.12517)  /  [website](https://robustness-evaluation.streamlit.app/)")
st.write("Abstract: *We conduct a large empirical evaluation to investigate the landscape of distributional robustness in question answering. Our investigation spans over 350 models and 16 question answering datasets, including a diverse set of architectures, model sizes, and adaptation methods (e.g., fine-tuning, adapter tuning, in-context learning, etc.). We find that, in many cases, model variations do not affect robustness and in-distribution performance alone determines out-of-distribution performance. Moreover, our findings indicate that i) zero-shot and in-context learning methods are more robust to distribution shifts than fully fine-tuned models; ii) few-shot prompt fine-tuned models exhibit better robustness than few-shot fine-tuned span prediction models; iii) parameter-efficient and robustness enhancing training methods provide no significant robustness improvements. In addition, we publicly release all evaluations to encourage researchers to further analyze robustness trends for question answering models.*")

st.markdown("##### Reliable and Trustworthy Machine Learning for Health Using Dataset Shift Detection")
st.write("Chunjong Park, **Anas Awadalla**, Tadayoshi Kohno, Shwetak Patel")
st.write("**NeurIPS 2021**")
st.write("[paper](https://arxiv.org/abs/2110.14019)")
st.write("Abstract: *Unpredictable ML model behavior on unseen data, especially in the health domain, raises serious concerns about its safety as repercussions for mistakes can be fatal. In this paper, we explore the feasibility of using state-of-the-art out-of-distribution detectors for reliable and trustworthy diagnostic predictions. We select publicly available deep learning models relating to various health conditions (e.g., skin cancer, lung sound, and Parkinson's disease) using various input data types (e.g., image, audio, and motion data). We demonstrate that these models show unreasonable predictions on out-of-distribution datasets. We show that Mahalanobis distance- and Gram matrices-based out-of-distribution detection methods are able to detect out-of-distribution data with high accuracy for the health models that operate on different modalities. We then translate the out-of-distribution score into a human interpretable confidence score to investigate its effect on the users' interaction with health ML applications. Our user study shows that the confidence score helped the participants only trust the results with a high score to make a medical decision and disregard results with a low score. Through this work, we demonstrate that dataset shift is a critical piece of information for high-stake ML applications, such as medical diagnosis and healthcare, to provide reliable and trustworthy predictions to the users.*")


# make a section for work experience    
st.header("👨🏽‍💻 Work Experience")
st.write("Software Engineering Intern at **Stripe** in Summer 2022")
st.write("")

st.write("Software Engineering Intern at **Amazon** in Summer 2021")

st.write("")

st.write("Machine Learning Engineering Intern at **Allen Institute for AI Incubator startup** in Spring 2021")

st.header("👨🏽‍🏫 Teaching Experience")
st.write("Teaching Assistant for [CSE 344](https://sites.google.com/cs.washington.edu/cse344-21au/home?pli=1) in **Fall 2021**")
