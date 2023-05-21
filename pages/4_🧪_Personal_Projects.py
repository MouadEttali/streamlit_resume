from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"


# ------------ CONSTANTS ----------
PAGE_TITLE = "Personal Projects | Et-tali Mouad"
PAGE_ICON = "🏛"

#-------- WORK EXPERIENCE CONTENT----------
NLP_PROJECT_TITLE = "Dimensionality reduction and clustering of scientific articles/wikipedia summaries/news headlines"
NLP_PROJECT_KEYWORDS = "NLP, text mining, clustering, dimensionality reduction, interprability, Word2Vec, GloVe, BERT, RoBERTa"
NLP_PROJECT_STACK = "PCA, t-SNE, UMAP, Autoencoders, Kmeans, Spherical Kmeans, factorial Kmeans, Hierarchal clustering (WARD, Complete, Linkage, Single Metrics), HDBSCAN, Reduced kmeans, Deep Clustering Network, deep KMeans"
NLP_PROJECT_DESCRIPTION = """
    - ✔  The project consists of two parts :
        - 💠Part 1: Text Analysis and Clustering without Dimensionality Reduction 
            - 🔸 Textual analysis and exploratory data analysis (EDA) of resumes
            - 🔸 Clustering on the original resume data using different clustering algorithms
            - 🔸 Benchmarking the results for later comparison
    """ 
# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Personal Projects")
# --------------- HELPER FUNCTIONS -----------------------

def personal_project_section(PROJECT_TITLE,PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION):

    st.subheader(PROJECT_TITLE)
    st.write('---')
    st.write(f'''**Keywords :** {PROJECT_KEYWORDS}''', unsafe_allow_html=True)
    
    st.write(PROJECT_DESCRIPTION, unsafe_allow_html=True)
    st.write(f'''**Technologies Used :** {PROJECT_STACK}''', unsafe_allow_html=True)
    st.write('\n')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ Projet 1 SECTION ---------
personal_project_section(NLP_PROJECT_TITLE,NLP_PROJECT_KEYWORDS,NLP_PROJECT_STACK,NLP_PROJECT_DESCRIPTION)
st.write('----')
# ------ ASTEK SECTION ---------
# personal_project_section(PROJECT_TITLE,PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION)

# st.write('----')

# #------ Alexsys Solutions SECTION
# personal_project_section(PROJECT_TITLE,PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION)

# st.write('----')
# #------ Digital Advisor SECTION
# personal_project_section(PROJECT_TITLE,PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION)

# st.write('----')