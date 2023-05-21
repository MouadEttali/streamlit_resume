from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# ------------ CONSTANTS ----------
PAGE_TITLE = "Academia | Et-tali Mouad"
PAGE_ICON = "🏛"
NAME = "Et-tali Mouad"
DESCRIPTION = """
My Academic Journey was always influenced by my love for maths and coding Starting from my Mathematical sciences Baccalaureate down to my latest experience 
"""

# ---------- PARIS_CITE------------------
PARIS_CITE_ICON = "📜"
PARIS_CITE_TITLE = "**Master 2 Machine learning for Data Science | Université Paris-Descartes**"
PARIS_CITE_PERIOD = "09/2021 - 09/2022"
PARIS_CITE_DESCRIPTION = """
- ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
- ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
- ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
""" 
# --------------------------------------

# ---------- ESI ------------------
ESI_ICON = "🧑🏻‍💻"
ESI_TITLE = "**Engineering Diploma in Data science and knowledge management | Université des Sciences de L'information**"
ESI_PERIOD = "09/2017 - 09/2020"
ESI_DESCRIPTION = """
- ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
- ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
- ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
""" 
# --------------------------------------

# ---------- PREP ------------------
PREP_ICON = "🚀"
PREP_TITLE = "**Preparatory classes for grand university (Maths/Physics) | Prep School AL-KHANSAA**"
PREP_PERIOD = "09/2015 - 09/2017"
PREP_DESCRIPTION = """
- ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
- ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
- ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
""" 
# --------------------------------------

# ---------- BAC ------------------
BAC_ICON = "🎒"
BAC_TITLE = "**Scientific Baccalaureate Mathematical Sciences | Groupe Scholaire Ouhoud**"
BAC_PERIOD = "06/2015"
BAC_DESCRIPTION = """
- ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
- ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
- ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
""" 
# --------------------------------------

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="centered")


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent

css_file = current_dir / "styles" / "main.css"

uni_pic = Image.open(current_dir / "assets" / "academic" / "uni.jpg")

esi_pic = Image.open(current_dir / "assets" / "academic" / "esi.jpg")

paris_pic = Image.open(current_dir / "assets" / "academic" / "paris.jpg")

bac_pic = Image.open(current_dir / "assets" / "academic" / "bac.jpg")


st.title("Academic Background")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)

def create_background_section(ICON, BACKGROUND_TITLE,BACKGROUND_PERIOD,BACKGROUND_DESCRIPTION):
    st.write('\n')
    st.write(ICON, BACKGROUND_TITLE)
    st.write(BACKGROUND_PERIOD)
    st.write(BACKGROUND_DESCRIPTION, unsafe_allow_html=True)
    
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------
cols = st.columns(2, gap='small')

with cols[0]:
    st.image(uni_pic)


with cols[1]:
    st.title(NAME)
    st.write(DESCRIPTION)


# --------- BACKGROUND ---------
V_SPACE(1)
st.subheader("My Journey 🚩")
st.write('---')

# st.write('\n')
# st.write("📜", "**Master 2 Machine learning for Data Science | Université Paris-Descartes**")
# st.write("09/2021 - 09/2022")
# st.write(
#     """
# - ► Collaborated on the creation of a <span style="color:#f50057; font-size: 15;">Digital costing</span>  solution that predicts cost of clothing items using Image and description, based on Convolutional Neural Networks and Transformers.
# - ► Development of a <span style="color:#f50057; font-size: 15;">360° Procurement</span> solution using Python, AWS MySQL and Google Data Studio with interactive dashboards including Forecasts, Spend Analysis, Supplier audit, CO2 emissions and more.
# - ► Participation in the creation of a <span style="color:#f50057; font-size: 15;">Succession Planning</span> solution that uses Machine Learning for optimal successor choice, using d3js for visualizations.
# - ► Commercial work : Participation in the <span style="color:#f50057; font-size: 15;">the developement of multiple proofs of concept</span> to demonstrate to prospects and clients for biz dev purposes
# - ► Internal work : Along 2 other data scientist and an Agile coach, we handle the management of different courses and certifications for the rest of the company.
# - ► Internal work : organization monthly presentations about the state of the art in the fields of data, AI and ML. As well as introduce new tools to our collaborators
# """ , unsafe_allow_html=True
# )

create_background_section(PARIS_CITE_ICON,PARIS_CITE_TITLE,PARIS_CITE_PERIOD,PARIS_CITE_DESCRIPTION)
st.image(paris_pic, caption="Getting ready for Internships and Job Hunting")
st.write('----')

create_background_section(ESI_ICON,ESI_TITLE,ESI_PERIOD,ESI_DESCRIPTION)
st.image(esi_pic, caption="Building connections in Engineering University (I had already finished my turn)")
st.write('----')

create_background_section(PREP_ICON,PREP_TITLE,PREP_PERIOD,PREP_DESCRIPTION)
st.write("""***PS: no picture for prep school period on purpose (if you know you know)*** 🙃""",unsafe_allow_html=True)
st.write('----')

create_background_section(BAC_ICON,BAC_TITLE,BAC_PERIOD,BAC_DESCRIPTION)
cols = st.columns(3,gap="small")
with cols[1]:
    st.image(bac_pic,caption="Blurry graduation because 2015 Android",width=280)
st.write('----')