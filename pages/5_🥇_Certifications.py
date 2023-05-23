from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"
CERTIFICATION_ML_PIC_PATH = current_dir / "assets" / "certifications" / "ml_stanford.png"
# ------------ CONSTANTS ----------
PAGE_TITLE = "Certifications | Et-tali Mouad"
PAGE_ICON = "🏛"

#-------- Certifications CONTENT----------
CERTIFICATION_ML_TITLE = "Machine Learning : Stanford University "
CERTIFICATION_ML_PIC = Image.open(CERTIFICATION_ML_PIC_PATH)
CERTIFICATION_ML_LINK = "https://www.coursera.org/account/accomplishments/verify/K52NAQ2FB8Z7"
CERTIFICATION_ML_DESCRIPTION = """
    - ✔  The Machine Learning Specialization is a foundational online program created in collaboration between DeepLearning.AI and Stanford Online.
    - ✔  This certification teaches the fundamentals of machine learning and how to use these techniques to build real-world AI applications. 

    """ 
# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Certifications")
# --------------- HELPER FUNCTIONS -----------------------

def certification_section(CERTIFICATION_TITLE,CERTIFICATION_LINK,CERTIFICATION_DESCRIPTION,CERTIFICATION_PIC):

    st.subheader(f"[{CERTIFICATION_TITLE}]({CERTIFICATION_LINK})")
    st.write(CERTIFICATION_DESCRIPTION, unsafe_allow_html=True)
    with st.expander("Check Certification"):
        st.image(CERTIFICATION_PIC,width=800)
    st.write('----')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)



certification_section(CERTIFICATION_ML_TITLE,CERTIFICATION_ML_LINK,CERTIFICATION_ML_DESCRIPTION,CERTIFICATION_ML_PIC)