from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"

E2E_PIC_PATH = current_dir / "assets" / "personal_projects" / "e2e.png"
THREE_MODELS_PIC_PATH = current_dir / "assets" / "personal_projects" / "three_models.png"
# ------------ CONSTANTS ----------
PAGE_TITLE = "Personal Projects | Et-tali Mouad"
PAGE_ICON = "🏛"

#-------- PERSONAL PROJECTS CONTENT----------
NLP_PROJECT_TITLE = "Dimensionality reduction and clustering of scientific articles/wikipedia summaries/news  (link)"
NLP_PROJECT_LINK = "https://github.com/MouadEttali/NLP-and-Text_Mining"
NLP_PROJECT_KEYWORDS = "NLP, text mining, clustering, dimensionality reduction, interprability, Word2Vec, GloVe, BERT, RoBERTa"
NLP_PROJECT_STACK = "PCA, t-SNE, UMAP, Autoencoders, Kmeans, Spherical Kmeans, factorial Kmeans, Hierarchal clustering (WARD, Complete, Linkage, Single Metrics), HDBSCAN, Reduced kmeans, Deep Clustering Network, deep KMeans"
NLP_PROJECT_DESCRIPTION = """
    - ✔  The project consists of two parts :
        - 💠Part 1: Text Analysis and Clustering without Dimensionality Reduction 
            - 🔸 Textual analysis and exploratory data analysis (EDA) of Scientific articles/News Headlines
            - 🔸 Clustering on the original data using different clustering algorithms
            - 🔸 Benchmarking the results for later comparison
        - 💠Part 2: Second Analysis and Clustering with Dimensionality Reduction
            - 🔸Tokenizing the data using Word2Vec, GloVe, BERT, and RoBERTa
            - 🔸Applying dimensionality reduction techniques (PCA, t-SNE, UMAP, Autoencoders)
            - 🔸Performing clustering on the reduced-dimensional data using various clustering algorithms.
    - 💡The goal is to gain insights from this data and identify clusters of similar articles/News based on their content, enabling better understanding and organization of of this sort of corpus for various purposes.
    """ 

NN_PROJECT_TITLE = "Implementation of a neural network for semi-supervised learning to predict MNIST data (link)"
NN_PROJECT_LINK = "https://github.com/MouadEttali/ComputerVision_DeepLearning/tree/main/PseudoLabelingProject"
NN_PROJECT_KEYWORDS = "Neural Networks, Semi-supervised Learning, Multi-class classification"
NN_PROJECT_STACK = "Tensorflow, Keras, Scikit-learn, Numpy"
NN_PROJECT_DESCRIPTION = """
    -  ✔  Implemented a neural network for MNIST data prediction with only <span style="color:#19A7CE; font-size: 15;">**100 labeled images**</span> using the semi-supervised learning method proposed in the scientific paper "Pseudo-label: The simple and Efficient Semi-Supervised Learning Method for Deep Neural Networks".
    -  ✔  Following the same approach as the article, the project utilizes pseudo-labels as the real labels in the learning process to maximize prediction and classify unlabeled data.
    -  ✔  The project considers pseudo-labeling as a prerequisite for semi-supervised learning, leveraging both labeled and unlabeled data simultaneously to train the neural network and <span style="color:#19A7CE; font-size: 15;">**achieve higher accuracy during testing.**</span>
    -  ✔  By incorporating the semi-supervised learning technique, the algorithm offers improved accuracy by effectively utilizing both labeled and unlabeled data in the training process and achieves a <span style="color:#19A7CE; font-size: 15;">**76.95% accuracy.**</span>
    """ 

ML_algos_PROJECT_TITLE = "Implementation of machine learning algorithms using numpy from mathematical foundations (link)"
ML_algos_PROJECT_LINK = "https://github.com/MouadEt-tali/From-scratch-MlAlgorithms"
ML_algos_PROJECT_KEYWORDS = "Coding, Machine Learning, First Principles"
ML_algos_PROJECT_STACK = "Numpy, Python"
ML_algos_PROJECT_DESCRIPTION = """
    - ✔ I coded a few classical machine learning models from scratch, starting from their basic mathematical fundamentals, and then translating that into python code.
    - ✔ Purpose :
        - 💠 Gaining a deeper understanding and insight into the inner workings of these algorithms.
        - 💠 Developing a higher level of understanding regarding their use cases, strengths, weaknesses, and various implementations.
    - ✔ Completed Algorithms: Linear Regression, Multiple Linear Regression, Logistic Regression, KNN and Support Vector Machine. Continual updates and exploration of other algorithms are in progress.
    """ 
E2E_PIC  = Image.open(E2E_PIC_PATH)
E2E_FLASK_PROJECT_TITLE = "End to End chrun prediction using Flask and aws (link)"
E2E_FLASK_PROJECT_LINK = "https://github.com/MouadEttali/End_to_END_churn_predictor"
E2E_FLASK_PROJECT_KEYWORDS = "Machine Learning application, Deployement, API"
E2E_FLASK_PROJECT_STACK = "Python, Flask, AWS"
E2E_FLASK_PROJECT_DESCRIPTION = """
    - ✔ I trained a model to predict Employee attrition based on multiple factors. such as Satisfaction Level, Number of Projects, Salary...
    - ✔ Wrote the REST API and coded a simple UI frontend for this ML project
    - ✔ Deployed it on AWS EC2 instance 
    """ 
THREE_MODELS_PIC  = Image.open(THREE_MODELS_PIC_PATH)
THREE_MODELS_PROJECT_TITLE = "Streamlit machine learning application that contains 3 models for predicting Diabetes , Parkinson's and Heart Disease (link)"
THREE_MODELS_PROJECT_LINK = "https://github.com/MouadEttali/streamlitHerokuApp"
THREE_MODELS_PROJECT_KEYWORDS = "Machine Learning application"
THREE_MODELS_PROJECT_STACK = "Python, Streamlit"
THREE_MODELS_PROJECT_DESCRIPTION = """
    - ✔ I trained binary classifiers such as Logistic regression and SVM to give an accurate prediction of these 3 of diseases :
    - ✔ The data contains fields such as insulin level, age,chest pain levels ...
    - ✔ Performances
        -💠Diabetes data : 89% recall, 91% precision
        -💠Parkinsons data : 85% recall, 89% precision
        -💠Heart Disease data : 91% recall, 96% precision
    - ✔ Deployed the application using Heroku
    """ 
# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Personal Projects")
# --------------- HELPER FUNCTIONS -----------------------

def personal_project_section(PROJECT_TITLE,PROJECT_LINK,PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION):

    st.subheader(f"[{PROJECT_TITLE}]({PROJECT_LINK})")
    st.write('---')
    st.write(f'''<span style="color:#f50057; font-size: 15;">**Keywords :**</span> {PROJECT_KEYWORDS}''', unsafe_allow_html=True)
    
    st.write(PROJECT_DESCRIPTION, unsafe_allow_html=True)
    st.write(f'''<span style="color:#f50057; font-size: 15;">**Technologies Used :**</span> {PROJECT_STACK}''', unsafe_allow_html=True)
    st.write('\n')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ Projet 1 SECTION ---------
personal_project_section(NLP_PROJECT_TITLE,NLP_PROJECT_LINK,NLP_PROJECT_KEYWORDS,NLP_PROJECT_STACK,NLP_PROJECT_DESCRIPTION)
st.write('----')
# ------ Project 2 SECTION ---------
# personal_project_section(PROJECT_TITLE,PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION)
personal_project_section(NN_PROJECT_TITLE,NN_PROJECT_LINK,NN_PROJECT_KEYWORDS,NN_PROJECT_STACK,NN_PROJECT_DESCRIPTION)
st.write('----')

# #------ Project 3 SECTION
personal_project_section(ML_algos_PROJECT_TITLE,ML_algos_PROJECT_LINK,ML_algos_PROJECT_KEYWORDS,ML_algos_PROJECT_STACK,ML_algos_PROJECT_DESCRIPTION)
st.write('----')

#------ Project 4 SECTION
personal_project_section(E2E_FLASK_PROJECT_TITLE,E2E_FLASK_PROJECT_LINK,E2E_FLASK_PROJECT_KEYWORDS,E2E_FLASK_PROJECT_STACK,E2E_FLASK_PROJECT_DESCRIPTION)
with st.expander("**Preview of deliverables :** "):
    st.image(E2E_PIC,width=1000)
st.write('----')

#------ Project 4 SECTION
personal_project_section(THREE_MODELS_PROJECT_TITLE,THREE_MODELS_PROJECT_LINK,THREE_MODELS_PROJECT_KEYWORDS,THREE_MODELS_PROJECT_STACK,THREE_MODELS_PROJECT_DESCRIPTION)
with st.expander("**Preview of deliverables :** "):
    st.image(THREE_MODELS_PIC,width=1000)
st.write('----')