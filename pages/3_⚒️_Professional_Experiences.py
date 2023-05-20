from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# ------------ CONSTANTS ----------
PAGE_TITLE = "Work Experiences | Et-tali Mouad"
PAGE_ICON = "🏛"
NAME = "Et-tali Mouad"
DESCRIPTION = """
My Academic Journey was always influenced by my love for maths and coding Starting from my Mathematical sciences Baccalaureate down to my latest experience 
"""

# --------------------------------------

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="centered")


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"

st.title("Professional Experiences")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)

# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------