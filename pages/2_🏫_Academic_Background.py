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
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Relevent Courses:**</span> Unsupervised Learning, Deep Learning, Guassian Mixture Models, Recommender Systems.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Motivation for Masters :**</span> Deepening of machine learning theoretical foundations and honing my data science skills.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Difficulties :**</span> Adjusting to the level of knowledge and skill required in internship and job interviews.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**What I learned :**</span> The best way to learn is to enjoy the process of going from 0 to 1 and not be frustrated at 0.5.
""" 
# ---------------------------------

# ---------- ESI ------------------
ESI_ICON = "🧑🏻‍💻"
ESI_TITLE = "**Engineering Diploma in Data science and knowledge management | Université des Sciences de L'information**"
ESI_PERIOD = "09/2017 - 09/2020"
ESI_DESCRIPTION = """
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Relevent Courses:**</span> Information Theory, Statistics, Algorithmic, Data science, Machine Learning, Python, Java, SQL.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Difficulties :**</span> Engineering diplomas are very time demanding even more than prep school, <span style="color:#f50057; font-size: 15;">**time management**</span> is key when it comes to attending 8 hours of courses then prepare 3-4 projects simulteanously.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**What I learned :**</span> I learned that I chose a path in life where I need to be <span style="color:#f50057; font-size: 15;">**very organized**</span> , and that realisation is important in of itself.
""" 
# --------------------------------------

# ---------- PREP ------------------
PREP_ICON = "🚀"
PREP_TITLE = "**Preparatory classes for grand university (Maths/Physics) | Prep School AL-KHANSAA**"
PREP_PERIOD = "09/2015 - 09/2017"
PREP_DESCRIPTION = """
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Relevent Courses:**</span> Mathematics (Linear Algebra, Probabilities, Calculus), Physics, Algorithmic, Phylosophy.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Motivation for Prep School :**</span> At this point in life, I didn't know exactly what I wanted to do in life but I knew that prep school was the hardest thing to do after highschool so I chose the hard way.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Difficulties :**</span> Adjusting to the level of deep understanding of mathematical concepts especially in calculus for maths and quantum physics in physics
- 🔸 <span style="color:#19A7CE; font-size: 15;">**What I learned :**</span> I learned that every person has their own pace and talents, some people understand things faster than others. The important thing is to be compassionate and treat people with kindess.
""" 
# --------------------------------------

# ---------- BAC ------------------
BAC_ICON = "🎒"
BAC_TITLE = "**Scientific Baccalaureate Mathematical Sciences | Groupe Scholaire Ouhoud**"
BAC_PERIOD = "06/2015"
BAC_DESCRIPTION = """
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Relevent Courses:**</span> Mathematics, Physics, Phylosophy.
- 🔸 <span style="color:#19A7CE; font-size: 15;">**Difficulties :**</span> The pressure from society to do good in that particular exam, and the expectations of parents and teachers who viewed us as "exellent students who are definitively headed to prep school"
- 🔸 <span style="color:#19A7CE; font-size: 15;">**What I learned :**</span> All things must come to an end. 
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
st.subheader("My Journey 🚩")
st.write('---')

create_background_section(PARIS_CITE_ICON,PARIS_CITE_TITLE,PARIS_CITE_PERIOD,PARIS_CITE_DESCRIPTION)
V_SPACE(1)
st.image(paris_pic,width=900, caption="Getting ready for Internships and Job Hunting")
st.write('----')

create_background_section(ESI_ICON,ESI_TITLE,ESI_PERIOD,ESI_DESCRIPTION)
st.image(esi_pic, caption="Building connections in Engineering University (I had already finished my turn)")
st.write('----')

create_background_section(PREP_ICON,PREP_TITLE,PREP_PERIOD,PREP_DESCRIPTION)
st.write("""<span style="color:#19A7CE; font-size: 15;">***PS: no picture for prep school period on purpose (if you know you know)*** </span>🙃""",unsafe_allow_html=True)
st.write('----')

create_background_section(BAC_ICON,BAC_TITLE,BAC_PERIOD,BAC_DESCRIPTION)
cols = st.columns(3,gap="small")
with cols[1]:
    st.image(bac_pic,caption="Blurry graduation because 2015 Android",width=280)
st.write('----')