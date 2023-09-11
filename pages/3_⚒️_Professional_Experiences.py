from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"
AQSONE_PIC_PATH = current_dir / "assets" / "work" / "aqsone" /"aqsone.png"
ASTEK_PIC_PATH = current_dir / "assets" / "work" /  "astek" / "astek.png"
ALEXSYS_PIC_PATH = current_dir / "assets" / "work" /  "alexsys" / "alexsys.png"
DADVISOR_PIC_PATH = current_dir / "assets" / "work" /  "digitaladvisor" / "digitaladvisor.png"
preview_aqsone = [f"""{current_dir}/assets/work/aqsone/{example}""" for example in ['example_1.png','example_2.png']]
preview_astek = [f"""{current_dir}/assets/work/astek/{example}""" for example in ['navigation.png','activity.png','database.png','sensor.png','data.png']]
preview_alexsys = [f"""{current_dir}/assets/work/alexsys/{example}""" for example in ['home.png','auth.png','add_person.png']]

# ------------ CONSTANTS ----------
PAGE_TITLE = "Work Experiences | Et-tali Mouad"
PAGE_ICON = "🏛"

#-------- WORK EXPERIENCE CONTENT----------
COMMUN_ROLE  = "Data Scientist"
AQSONE_PIC  = Image.open(AQSONE_PIC_PATH)
AQSONE_COMPANY = "Aqsone"
AQSONE_PERIOD = "09/2022 - Present"
AQSONE_DESCRIPTION = """
    - ►  <span style="color:#f50057; font-size: 15;">Nexans mission : </span>
        - 💠  Correction of inconsistencies in historical purchasing and supplier data. Enrichment of missing data impacting  <span style="color:#f50057; font-size: 15;">+440 M€</span> in materials thanks to deduplication and ML clustering methods.
    - ►  <span style="color:#f50057; font-size: 15;">Allegro Musique mission : </span>
        - 💠  Participation dans le développement d’une solution ML de recommendation de professeurs de musiques à des élèves cherchant des cours. La solution est développé entierment sur AWS et utilise plusieurs services <span style="color:#19A7CE; font-size: 15;">**( Sagemaker, Lambda, API Gateway, S3, RDS )**</span>
    - ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
    - ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
    - ► Participated in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
    - ► Commercial work : Participated in the <span style="color:#f50057; font-size: 15;">the developement of multiple proofs of concept</span> to demonstrate to prospects and clients for biz dev purposes
    - ► Internal work :
        - 💠 Along 2 other data scientist and an Agile coach, we handle the management of different courses and certifications for the rest of the company.
        - 💠 organization monthly presentations about the state of the art in the fields of data, AI and ML. As well as introduce new tools to our collaborators
    """ 

ASTEK_PIC  = Image.open(ASTEK_PIC_PATH)
ASTEK_COMPANY = "Astek Researche Lab"
ASTEK_PERIOD = "02/2022 - 08/2022"
ASTEK_DESCRIPTION = """
    - ► Implemented a XGBOOST model that utilizes a <span style="color:#f50057; font-size: 15;">user's tactile, orientation, and acceleration phone usage data</span> to determine whether he is the owner of the phone or an impostor.
    - ► Developed an application with <span style="color:#f50057; font-size: 15;">React and MongoDB</span> that collects training data through built-in sensor APIs.
    - ► The model achieves <span style="color:#f50057; font-size: 15;">94% accuracy and an F1 score of 88% on 7 users</span>, and can also identify phones used by the same user.
    - ► Write a report on the work, detailing the thoughts and reflexions on the subject, the experiments considered and carried out, and the conclusions regarding the scientific issues and uncertainties developed.
    - ► The app I developped allowed the user to create his own expirements by specifying which sensors are used, the types of activities such reading/ walking/ comparing images. And for activities with data you can add text or images. Finally it was deployed on heorku and Atlas Cloud (MongoDB) as a database.
    """ 

ALEXSYS_PIC  = Image.open(ALEXSYS_PIC_PATH)
ALEXSYS_COMPANY = "ALEXSYS SOLUTIONS"
ALEXSYS_PERIOD = "12/2020 - 08/2020"
ALEXSYS_DESCRIPTION = """
    - ► <span style="color:#f50057; font-size: 15;">Mission ONCF (Office National des Chemins de Fer du Maroc) :</span>
      - 💠 Implemented a classification and optical character recognition (OCR) model using YOLOv4 on scans of legal documents in Arabic. The developed system reduces the processing time of each document to the detection time, allowing the batch detection of 1000 documents in 5 minutes (3.33 documents per second).
    - ► <span style="color:#f50057; font-size: 15;">Mission TotalEnergies :</span>
      - 💠 Development of a license plate detection and reading application for natural gas distribution trucks. This system has reduced the time it takes for trucks to enter the gas distribution center by an average of 2 minutes and 53 seconds.
    """ 

DADVISOR_PIC  = Image.open(DADVISOR_PIC_PATH)
DADVISOR_COMPANY = "DigitalAdvisor"
DADVISOR_PERIOD = "01/2020 - 08/2020"
DADVISOR_DESCRIPTION = """
    - ► Implemented a multiclass classification model to predict  <span style="color:#f50057; font-size: 15;">**the types of failures of industrial machines**</span> 86% Accuracy 79% F1 score.
    - ► Implemented a regression model to predict <span style="color:#f50057; font-size: 15;">**the Remaining Useful Time of industrial machines**</span>  using the algorithms: XGBoost, Random Forest and Support Vector Machine.
    - ► Participated in the development of a real time monitoring application for industrial machines using Flask.
    """ 
# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Professional Experiences")
# --------------- HELPER FUNCTIONS -----------------------

def work_experience_section(PIC,ROLE,COMPANY,PERIOD,WORK_DESCRIPTION):

    st.image(PIC,width=150)
    st.write(f"**{ROLE} | {COMPANY}**")
    st.write(f"{PERIOD}")
    st.write(WORK_DESCRIPTION, unsafe_allow_html=True)
    

# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ AQSONE SECTION ---------
work_experience_section(AQSONE_PIC,COMMUN_ROLE,AQSONE_COMPANY,AQSONE_PERIOD,AQSONE_DESCRIPTION)
with st.expander("**Preview of deliverables :** "):
    images = [Image.open(image) for image in preview_aqsone]
    cols = st.columns(len(images))
    for col,image in zip(cols,images):
        with col:
            st.image(image,width=600)
st.write('----')

# ------ ASTEK SECTION ---------
work_experience_section(ASTEK_PIC,COMMUN_ROLE,ASTEK_COMPANY,ASTEK_PERIOD,ASTEK_DESCRIPTION)
images = [Image.open(image) for image in preview_astek]
image_captions = ['Navigation between pages' , 'Adding an activity to the experiment','MongoDB Cloud Database' ,'Adding a sensor to the experiment','Adding data and time limit to an activity']
with st.expander("**Preview of deliverables :** "):
    cols = st.columns(3,gap="large")
    for i,image in enumerate(images):
        with cols[i%3]:
            st.image(image,caption=image_captions[i],width=400)
st.write('----')

#------ Alexsys Solutions SECTION
work_experience_section(ALEXSYS_PIC,COMMUN_ROLE,ALEXSYS_COMPANY,ALEXSYS_PERIOD,ALEXSYS_DESCRIPTION)
with st.expander("**Preview of deliverables :** "):
    images = [Image.open(image) for image in preview_alexsys]
    cols = st.columns(len(images))
    for col,image in zip(cols,images):
        with col:
            st.image(image,width=400)
st.write('----')
#------ Digital Advisor SECTION
work_experience_section(DADVISOR_PIC,COMMUN_ROLE,DADVISOR_COMPANY,DADVISOR_PERIOD,DADVISOR_DESCRIPTION)


st.write('----')