from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image



# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"
AQSONE_PIC_PATH = current_dir / "assets" / "aqsone.png"
ASTEK_PIC_PATH = current_dir / "assets" / "astek.png"
example_paths = [f"""{current_dir}/assets/{example}""" for example in ['example_1.png','example_2.png']]


# ------------ CONSTANTS ----------
PAGE_TITLE = "Work Experiences | Et-tali Mouad"
PAGE_ICON = "🏛"
DESCRIPTION = """
My Academic Journey was always influenced by my love for maths and coding Starting from my Mathematical sciences Baccalaureate down to my latest experience 
"""

#-------- WORK EXPERIENCE CONTENT----------
COMMUN_ROLE  = "Data Scientist"
AQSONE_PIC  = Image.open(AQSONE_PIC_PATH)
AQSONE_COMPANY = "Aqsone"
AQSONE_PERIOD = "09/2022 - Present"
AQSONE_DESCRIPTION = """
    - ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
    - ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
    - ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
    - ► Commercial work : Participation in the <span style="color:#f50057; font-size: 15;">the developement of multiple proofs of concept</span> to demonstrate to prospects and clients for biz dev purposes
    - ► Internal work : Along 2 other data scientist and an Agile coach, we handle the management of different courses and certifications for the rest of the company.
    - ► Internal work : organization monthly presentations about the state of the art in the fields of data, AI and ML. As well as introduce new tools to our collaborators
    """ 

ASTEK_PIC  = Image.open(ASTEK_PIC_PATH)
ASTEK_COMPANY = "Astek Researche Lab"
ASTEK_PERIOD = "02/2022 - 08/2022"
ASTEK_DESCRIPTION = """
    - ► Implementation of a model that utilizes a user's tactile, orientation, and acceleration phone usage data to determine whether he is the owner of the phone or an impostor.
    - ► Developed an application with React and MongoDB that collects training data through built-in sensor APIs.
    - ► The model achieves 94% accuracy and an F1 score of 88% on 7 users, and can also identify phones used by the same user.
    - ► Write a report on the work, detailing the thoughts and reflexions on the subject, the experiments considered and carried out, and the conclusions regarding the scientific issues and uncertainties developed.
    """ 

# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Professional Experiences")
# --------------- HELPER FUNCTIONS -----------------------

def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)

def work_experience_section(PIC,ROLE,COMPANY,PERIOD,WORK_DESCRIPTION):
    st.write('\n')
    
    st.image(PIC,width=120)
    st.write(f"**{ROLE} | {COMPANY}**")
    st.write(f"{PERIOD}")
    st.write(WORK_DESCRIPTION, unsafe_allow_html=True)
    

# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ AQSONE SECTION ---------
work_experience_section(AQSONE_PIC,COMMUN_ROLE,AQSONE_COMPANY,AQSONE_PERIOD,AQSONE_DESCRIPTION)

images = [Image.open(image) for image in example_paths]
cols = st.columns(len(images))
for col,image in zip(cols,images):
    with col:
        st.image(image,width=600)
st.write('----')

# ------ ASTEK SECTION ---------
work_experience_section(ASTEK_PIC,COMMUN_ROLE,ASTEK_COMPANY,ASTEK_PERIOD,ASTEK_DESCRIPTION)
st.write('----')