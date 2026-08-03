from printusername import print_user_name
import streamlit as sl

# Call the function to print username
# print_user_name()



sl.set_page_config(
    page_title="Chatbot UI",
    page_icon="🧠",
    layout="wide",  
)

# Custom CSS for sidebar styling
sl.markdown("""
    <style>
    div.css-textbarboxtype {
        background-color: #EEEEEE;
        border: 1px solid #DCDCDC;
        padding: 20px 20px 20px 70px;
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
    }
    
    /* Justify text for Purpose section */
    div.css-textbarboxtype:nth-of-type(3) {
        text-align: justify;
        text-justify: inter-word;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar
with sl.sidebar:
    sl.title("About Bot")
    
    # About Section
    sl.markdown("## Description")
    sl.markdown("""
        <div class="css-textbarboxtype">
            An AI-powered chatbot designed to provide answers related to College Name.
        </div>
    """, unsafe_allow_html=True)


sl.title("🎓 College Chatbot")
