import streamlit as st

st.set_page_config(page_title="Anas Awadalla")

st.image('profile.jpg', width=300)        
st.title("Anas Awadalla")

st.write("📫 anasa2@cs.washington.edu | 🐦 [Twitter](https://twitter.com/anas_awadalla) | 🥼 [Google Scholar](https://scholar.google.com/citations?hl=en&user=gMOjp_oAAAAJ)")

# make a section for bio
st.subheader("👋🏽 Bio")
st.write("""I am a PhD student at the [University of Washington](https://www.cs.washington.edu) advised
        by [Yejin Choi](https://homes.cs.washington.edu/~yejin/) and [Ludwig Schmidt](http://people.csail.mit.edu/ludwigs/). I am currently excited about large-scale multimodal datasets and multimodal models.""")

# make a section for publications
st.subheader("📄 Research")
st.markdown("##### 🍃 MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens")
st.write("**Anas Awadalla**, Le Xue, Oscar Lo, Manli Shu, Hannah Lee, Etash Kumar Guha, Matt Jordan, Sheng Shen, Mohamed Awadalla, Silvio Savarese, Caiming Xiong, Ran Xu, Yejin Choi, Ludwig Schmidt")
st.write("**Preprint 2024**")
st.write("[paper](https://arxiv.org/abs/2406.11271) / [blog post](https://blog.salesforceairesearch.com/mint-1t/) / [repo](https://github.com/mlfoundations/MINT-1T)")
st.write("")

st.markdown("##### xGen-MM (BLIP-3): A Family of Open Large Multimodal Models")
st.write("Le Xue, Manli Shu, **Anas Awadalla**, Jun Wang, An Yan, Senthil Purushwalkam, Honglu Zhou, Viraj Prabhu, Yutong Dai, Michael S Ryoo, Shrikant Kendre, Jieyu Zhang, many others, Caiming Xiong, Ran Xu")
st.write("**Preprint 2024**")
st.write("[models](https://huggingface.co/collections/Salesforce/xgen-mm-1-models-662971d6cecbf3a7f80ecc2e)")
st.write("")

st.markdown("##### Certainly Uncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness")
st.write("Khyathi Raghavi Chandu, Linjie Li, **Anas Awadalla**, Ximing Lu, Jae Sung Park, Jack Hessel, Lijuan Wang, Yejin Choi")
st.write("**Preprint 2024**")
st.write("[paper](https://arxiv.org/abs/2407.01942)")
st.write("")

st.markdown("##### 🦩 OpenFlamingo: An Open-Source Framework for Training Vision-Language Models with In-Context Learning")
st.write("**Anas Awadalla***, Irena Gao*, Joshua Gardner, Jack Hessel, Yusuf Hanafy, Wanrong Zhu, Kalyani Marathe, Yonatan Bitton, Samir Gadre, Shiori Sagawa, Jenia Jitsev, Simon Kornblith, Pang Wei Koh, Gabriel Ilharco, Mitchell Wortsman, Ludwig Schmidt")
st.write("**Preprint 2023**")
st.write("[paper](https://arxiv.org/abs/2308.01390) / [blog post 1](https://laion.ai/blog/open-flamingo/) / [blog post 2](https://laion.ai/blog/open-flamingo-v2/) /  [repo](https://github.com/mlfoundations/open_flamingo) / [demo](https://huggingface.co/spaces/openflamingo/OpenFlamingo)")
st.write("")

st.markdown("##### Multimodal C4: An Open, Billion-scale Corpus of Images Interleaved With Text")
st.write("Wanrong Zhu*, Jack Hessel*, **Anas Awadalla**, Samir Yitzhak Gadre, Jesse Dodge, Alex Fang, Youngjae Yu, Ludwig Schmidt, William Yang Wang, Yejin Choi")
st.write("**Neurips 2023**")
st.write("[paper](https://arxiv.org/abs/2304.06939) / [repo](https://github.com/allenai/mmc4)")
st.write("")

st.markdown("##### Catwalk: A Unified Language Model Evaluation Framework for Many Datasets")
st.write("Dirk Groeneveld, **Anas Awadalla**, Iz Beltagy, Akshita Bhagia, Ian Magnusson, Hao Peng, Oyvind Tafjord, Pete Walsh, Kyle Richardson, Jesse Dodge")
st.write("**Preprint 2023**")
st.write("[paper](https://arxiv.org/abs/2312.10253) / [repo](https://github.com/allenai/catwalk)")
st.write("")

st.markdown("##### VisIT-Bench: A Benchmark for Vision-Language Instruction Following Inspired by Real-World Use")
st.write("Yonatan Bitton*, Hritik Bansal*, Jack Hessel*, Rulin Shao, Wanrong Zhu, **Anas Awadalla**, Josh Gardner, Rohan Taori, Ludwig Schimdt")
st.write("**Neurips 2023**")
st.write("[paper](https://arxiv.org/abs/2308.06595) / [repo](https://github.com/mlfoundations/VisIT-Bench/)")
st.write("")

st.markdown("##### Exploring The Landscape of Distributional Robustness for Question Answering Models")
st.write("**Anas Awadalla**, Mitchell Wortsman, Gabriel Ilharco, Sewon Min, Ian Magnusson, Hannaneh Hajishirzi, Ludwig Schmidt")
st.write("**EMNLP 2022**")
st.write("[paper](https://arxiv.org/abs/2210.12517)  /  [website](https://robustness-evaluation.streamlit.app/)")
st.write("")

st.markdown("##### Reliable and Trustworthy Machine Learning for Health Using Dataset Shift Detection")
st.write("Chunjong Park, **Anas Awadalla**, Tadayoshi Kohno, Shwetak Patel")
st.write("**Neurips 2021**")
st.write("[paper](https://arxiv.org/abs/2110.14019)")
st.write("")

st.subheader("🏅 Awards")
st.write("Honorable Mention for [CRA Outstanding Undergraduate Researcher Award 2023](https://cra.org/2023-outstanding-undergraduate-researcher-award-recipients/) // [article](https://news.cs.washington.edu/2023/01/13/allen-schools-michael-duan-and-anas-awadalla-recognized-by-cra-outstanding-undergraduate-researcher-awards-program/)")

# make a section for work experience    
st.subheader("👨🏽‍💻 Work Experience")
st.write("AI Research Intern at :blue[**Salesforce Research**] in **2024**")
st.write("Software Engineering Intern at :violet[**Stripe**] in **Summer 2022**")
st.write("Software Engineering Intern at :orange[**Amazon**] in **Summer 2021**")
