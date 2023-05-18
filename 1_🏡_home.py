
from pathlib import Path

import streamlit as st
from PIL import Image

# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"

resume_file = current_dir / "assets" / "cv.pdf"

profile_pic = current_dir / "assets" / "profile-pic.png"

my_zone_pic = current_dir / "assets" / "my_zone.png"

# ------------ CONSTANTS ----------
PAGE_TITLE = "Digital CV | Et-tali Mouad"
PAGE_ICON = ":wave:"
NAME = "Et-tali Mouad"
DESCRIPTION = """
Data Scientist @ Aqsone,  I help clients optimize their performance with AI and data.
"""
EMAIL = "mouad.et-tali@aqsone.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mouad-et-tali/",
    "GitHub": "https://github.com/MouadEt-tali"
}
PROJECTS = {
    "🏆 Dimensionality reduction/clustering of data from scientific articles/ wikipedia summaries/news headlines": "https://github.com/MouadEttali/NLP-and-Text_Mining",
    "🏆 Implementation of a neural network for semi-supervised learning to predict MNIS data": "https://github.com/MouadEttali/ComputerVision_DeepLearning/tree/main/PseudoLabelingProject",
    "🏆 Implementation of multiple regression and logistic regression algorithms from the mathematical foundations. ": "https://github.com/MouadEttali/From-scratch-machine-learning---From-mathematical-formulas-to-functioning-algorithms",
    "🏆 This resume streamlit ": "https://github.com/MouadEttali/streamlit_resume",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


st.title("Hello There")


# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

my_zone_pic = Image.open(my_zone_pic)
# ------ HERO SECTION -----------

cols = st.columns(2, gap='small')

with cols[0]:
    st.image(profile_pic, width=230)


with cols[1]:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button( 
        label="📄 Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📫",EMAIL)


# -------- SOCIALS ---------

st.write("#")

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ------- EXPERIENCE AND QUALIFS --------

st.write("#")
st.subheader('About me')
st.write(
    """
    - ✔️ **4 years of experience** in data science consulting firms for clients like <span style="color:#f50057; font-size: 15;">Total Energies , ONCF , Nexans </span> (Details in Background page)
    - ✔️ Built multiple ML based web applications (D3js, Streamlit) with deployment in AWS, Heroku 
    - ✔️ Expertise in statistical principles and classical ML models
    - ✔️ Product and value oriented mindset ( my dream is to build valuable ML tools, my nightmare is models dying in notebooks )  
    - ✔️ Work feels best when it's **challenging enough to push me and not easy enough to make me bored**
    """
,unsafe_allow_html=True)
st.image(my_zone_pic)
st.write(""" ⚠️ Warning : if you hand me a boring task <span style="color:#f50057; font-size: 15;">I will try to automate it.</span>""",unsafe_allow_html=True)
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, pySpark
- 🧪 Data science : Machine Learning, Ensemble methods (Bagging, Boosting) / kernel methods (SVM, SPCA), Deep Learning, Natural Language Processing, Optimisation
- 📊 Data Visulization: PowerBi, Qlicksense, D3js
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
- ☁️ Cloud : AWS (Certified Cloud Practitioner (CLF)), Palantir Foundry
"""
)

# --------- work history ---------
st.write("#")
st.subheader("Recent Job Experience")
st.write('---')

st.write('\n')
st.write("🚧", "**Data Scientist | Aqsone**")
st.write("09/2022 - Present")
st.write(
    """
- ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
- ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
- ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
- ► Commercial work : Participation in the <span style="color:#f50057; font-size: 15;">the developement of multiple proofs of concept</span> to demonstrate to prospects and clients for biz dev purposes
- ► Internal work : Along 2 other data scientist and an Agile coach, we handle the management of different courses and certifications for the rest of the company.
- ► Internal work : organization monthly presentations about the state of the art in the fields of data, AI and ML. As well as introduce new tools to our collaborators
""" , unsafe_allow_html=True
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Personal Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")