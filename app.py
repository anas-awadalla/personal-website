import streamlit as st
# st.set_page_config(layout="wide")

# from lm_are_zeroshot_planners import lm_are_zeroshot_planners
# from chinchilla import chinchilla
# from scratchpad import scratchpad

# about_tab = st.tabs(["About"])

# with about_tab:
st.image('profile.jpg', width=300)        
st.title("Anas Awadalla")

st.write("📫 anasa2@cs.washington.edu | 🐦 [Twitter](https://twitter.com/anas_awadalla) | 🔗 [LinkedIn](https://www.linkedin.com/in/anas-awadalla/) | 🥼 [Google Scholar](https://scholar.google.com/citations?hl=en&user=gMOjp_oAAAAJ)")

# make a section for bio
st.header("👋🏽 Bio")
st.write("""I am a senior at the University of Washington studying computer science, advised
        by [Prof. Ludwig Schmidt](http://people.csail.mit.edu/ludwigs/). 
        I do research in natural language processing, robustness, and vision language models.""")

# make a section for publications
st.header("📄 Research")
st.markdown("##### 🦩 OpenFlamingo: An Open-Source Framework for Training Vision-Language Models with In-Context Learning")
st.write("**Anas Awadalla**, Irena Gao, Joshua Gardner, Jack Hessel, Yusuf Hanafy, Wanrong Zhu, Kalyani Marathe, Yonatan Bitton, Samir Gadre, Jenia Jitsev, Simon Kornblith, Pang Wei Koh, Gabriel Ilharco, Mitchell Wortsman, Ludwig Schmidt")
st.write("[blog post](https://laion.ai/blog/open-flamingo/) /  [repo](https://github.com/mlfoundations/open_flamingo) / [demo](http://open-flamingo.org/)")
st.write("")

st.markdown("##### Multimodal C4: An Open, Billion-scale Corpus of Images Interleaved With Text")
st.write("Wanrong Zhu*, Jack Hessel*, **Anas Awadalla**, Samir Yitzhak Gadre, Jesse Dodge, Alex Fang, Youngjae Yu, Ludwig Schmidt, William Yang Wang, Yejin Choi")
st.write("[paper](https://arxiv.org/abs/2304.06939) [code](https://github.com/allenai/mmc4)")
with st.expander("Abstract"):
    st.write("*In-context vision and language models like Flamingo support arbitrarily interleaved sequences of images and text as input. This format not only enables few-shot learning via interleaving independent supervised (image, text) examples, but also, more complex prompts involving interaction between images, e.g., \"What do image A and image B have in common?\" To support this interface, pretraining occurs over web corpora that similarly contain interleaved images+text. To date, however, large-scale data of this form have not been publicly available. We release Multimodal C4 (mmc4), an augmentation of the popular text-only c4 corpus with images interleaved. We use a linear assignment algorithm to place images into longer bodies of text using CLIP features, a process that we show outperforms alternatives. mmc4 spans everyday topics like cooking, travel, technology, etc. A manual inspection of a random sample of documents shows that a vast majority (90%) of images are topically relevant, and that linear assignment frequently selects individual sentences specifically well-aligned with each image (78%). After filtering NSFW images, ads, etc., the corpus contains 103M documents containing 585M images interleaved with 43B English tokens.*")
st.write("")

st.markdown("##### Exploring The Landscape of Distributional Robustness for Question Answering Models")
st.write("**Anas Awadalla**, Mitchell Wortsman, Gabriel Ilharco, Sewon Min, Ian Magnusson, Hannaneh Hajishirzi, Ludwig Schmidt")
st.write("**EMNLP Findings 2022**")
st.write("[paper](https://arxiv.org/abs/2210.12517)  /  [website](https://robustness-evaluation.streamlit.app/)")
with st.expander("Abstract"):
    st.write("*We conduct a large empirical evaluation to investigate the landscape of distributional robustness in question answering. Our investigation spans over 350 models and 16 question answering datasets, including a diverse set of architectures, model sizes, and adaptation methods (e.g., fine-tuning, adapter tuning, in-context learning, etc.). We find that, in many cases, model variations do not affect robustness and in-distribution performance alone determines out-of-distribution performance. Moreover, our findings indicate that i) zero-shot and in-context learning methods are more robust to distribution shifts than fully fine-tuned models; ii) few-shot prompt fine-tuned models exhibit better robustness than few-shot fine-tuned span prediction models; iii) parameter-efficient and robustness enhancing training methods provide no significant robustness improvements. In addition, we publicly release all evaluations to encourage researchers to further analyze robustness trends for question answering models.*")
st.write("")

st.markdown("##### Reliable and Trustworthy Machine Learning for Health Using Dataset Shift Detection")
st.write("Chunjong Park, **Anas Awadalla**, Tadayoshi Kohno, Shwetak Patel")
st.write("**NeurIPS 2021**")
st.write("[paper](https://arxiv.org/abs/2110.14019)")
with st.expander("Abstract"):
    st.write("*Unpredictable ML model behavior on unseen data, especially in the health domain, raises serious concerns about its safety as repercussions for mistakes can be fatal. In this paper, we explore the feasibility of using state-of-the-art out-of-distribution detectors for reliable and trustworthy diagnostic predictions. We select publicly available deep learning models relating to various health conditions (e.g., skin cancer, lung sound, and Parkinson's disease) using various input data types (e.g., image, audio, and motion data). We demonstrate that these models show unreasonable predictions on out-of-distribution datasets. We show that Mahalanobis distance- and Gram matrices-based out-of-distribution detection methods are able to detect out-of-distribution data with high accuracy for the health models that operate on different modalities. We then translate the out-of-distribution score into a human interpretable confidence score to investigate its effect on the users' interaction with health ML applications. Our user study shows that the confidence score helped the participants only trust the results with a high score to make a medical decision and disregard results with a low score. Through this work, we demonstrate that dataset shift is a critical piece of information for high-stake ML applications, such as medical diagnosis and healthcare, to provide reliable and trustworthy predictions to the users.*")
st.write("")

st.header("🏅 Awards")
st.write("Honorable Mention for [CRA Outstanding Undergraduate Researcher Award 2023](https://cra.org/2023-outstanding-undergraduate-researcher-award-recipients/) // [article](https://news.cs.washington.edu/2023/01/13/allen-schools-michael-duan-and-anas-awadalla-recognized-by-cra-outstanding-undergraduate-researcher-awards-program/)")

# make a section for work experience    
st.header("👨🏽‍💻 Work Experience")
st.write("Software Engineering Intern at :violet[**Stripe**] in **Summer 2022**")
st.write("")

st.write("Software Engineering Intern at :orange[**Amazon**] in **Summer 2021**")
st.write("")

st.write("Machine Learning Engineering Intern at **[Measure Labs](https://www.measurelabs.com)** in **Spring 2021**")

st.header("👨🏽‍🏫 Teaching Experience")
st.write("Teaching Assistant for [CSE 344](https://sites.google.com/cs.washington.edu/cse344-21au/home?pli=1) in **Fall 2021**")

# with blog_tab:
#     st.title("Blog Posts")
#     st.write("")
#     scratchpad(st)
#     chinchilla(st)
#     lm_are_zeroshot_planners(st)
