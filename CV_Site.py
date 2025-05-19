import streamlit as st
import base64
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Carol Andrea Murcia Romero",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for luxury styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# At the top of your sidebar
with st.sidebar:
    st.markdown("""
    <style>
        div[role="radiogroup"] > label {
            padding: 10px 15px;
            margin: 5px 0;
            border-radius: 4px;
            transition: all 0.3s;
        }
        div[role="radiogroup"] > label:hover {
            background: #f5f5f5;
        }
        div[role="radiogroup"] > label[data-baseweb="radio"] {
            background: #FFFFFF;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    selected = st.radio(
        "MENU",
        ["Profile", "Experience", "Education", "Portfolio", "Skills", "Contact"],
        label_visibility="visible"
    )

# Header section
def header():
    col1, col2 = st.columns([2, 3])
    with col1:
        # Profile picture - replace with your image
        st.image("profile.jpg", width=200)
    with col2:
        st.markdown("<h1 style='font-size: 48px; margin-bottom: 0;'>CAROL ANDREA</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 36px; margin-top: 0; color: #7a7a7a;'>MURCIA ROMERO</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px;'>Data Scientist | Supply Chain Professional</p>", unsafe_allow_html=True)

# Profile page
if selected == "Profile":
    header()
    # Video section
    st.markdown("---")
    
    # Placeholder for video - replace with your actual video
    video_file = open('intro2.mp4', 'rb')
    video_bytes = video_file.read()
    with st.container():
        col1, col2, col3 = st.columns([1,1,1])  # Centered column
        with col2:
            st.video(video_bytes)

    st.markdown("---")

    st.markdown("""
    <h3>ABOUT ME</h3>
    <p>
    Highly motivated Marketing and Logistics professional currently enhancing analytical capabilities 
    through a Master's in Big Data Analytics for Business. Proven team player, detail oriented with 
    a creative and critical approach to complex challenges.
    </p>
    """, unsafe_allow_html=True) 

    st.markdown("""
    <h3>KEY STRENGTHS</h3>
    <ul>
        <li>Data Analysis & Visualization</li>
        <li>Supply Chain Optimization</li>
        <li>Cross-functional Collaboration</li>
        <li>Process Improvement</li>
        <li>Bilingual Communication</li>
    </ul>
    """, unsafe_allow_html=True)

# Experience page
elif selected == "Experience":
    header()
    st.markdown("---")
    
    st.markdown("""
    <h2 style='text-align: center; margin-bottom: 40px;'>PROFESSIONAL EXPERIENCE</h2>
    """, unsafe_allow_html=True)
    
    # Experience 1
    with st.expander("Demand Planning and Sourcing Analyst | Blush-Bar, Colombia | 2021-2024", expanded=False):
        st.markdown("""
        <ul>
            <li>Developed demand forecasting models for 7 cosmetic brands helping 60% of them rank among the company's top 10</li>
            <li>Worked with teams across departments to develop and document new processes, improving overall organization and efficiency</li>
            <li>Implemented a weekly data visualization system for the marketing team, supporting strategic decision making and monitoring KPIs</li>
        </ul>
        """, unsafe_allow_html=True)
    
    # Experience 2
    with st.expander("Logistics Coordinator | Nutresa, Colombia | 2019-2021"):
        st.markdown("""
        <ul>
            <li>Developed data analytics to track inventory performance and optimize storage, improving accuracy to 95%</li>
            <li>Reduced inventory and delivery prep time by 50% through process optimization</li>
        </ul>
        """, unsafe_allow_html=True)
    
    # Experience 3
    with st.expander("Logistics Analyst | Nutresa, Colombia | 2018-2019"):
        st.markdown("""
        <ul>
            <li>Designed and launched a model to optimize raw material distribution in northern Colombia</li>
            <li>Used available data to address resource limitations, successfully implementing the model company-wide</li>
        </ul>
        """, unsafe_allow_html=True)

# Education page
elif selected == "Education":
    header()
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <h3>Master in Big Data Analytics for Business</h3>
        <p>Iéseg School of Management, France | 2024-Present</p>
        <ul>
            <li>Main courses: Forecasting, Predictive Analysis, Big Data Tools, NLP, Deep Learning, Statistical ML, Visualization Tools, Recommendation Tools</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h3>International Marketing and Logistics Manager</h3>
        <p>Sabana University, Colombia | 2015-2020</p>
        <ul>
            <li>"Ser Pilo Paga" and "Talentos Excepcionales (TExc)" scholarship programs</li>
            <li>Main courses: Financial project evaluation, International marketing, strategic marketing, Planning, sourcing, distribution and International Logistics</li>
        </ul>
        """, unsafe_allow_html=True)

# Portfolio page
elif selected == "Portfolio":
    header()
    st.markdown("---")
    
    st.markdown("<h2 style='text-align: center;'>PORTFOLIO</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='border: 1px solid #e0e0e0; padding: 20px; margin-bottom: 20px; border-radius: 5px;'>
            <h4>Cash Flow Analysis</h4>
            <p>Built a dashboard to track customer payment cycles and key KPIs for a logistics company using Python and Tableau</p>
            <p>Forecast the company cash flow for a time horizon of 3 years using Arima and ETS models</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='border: 1px solid #e0e0e0; padding: 20px; margin-bottom: 20px; border-radius: 5px;'>
            <h4>Predictive Modeling</h4>
            <p>Predicted the review score of orders from an e-commerce company preparing historical data and implementing a machine learning model using Spark</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='border: 1px solid #e0e0e0; padding: 20px; margin-bottom: 20px; border-radius: 5px;'>
            <h4>Sales Results Dashboard</h4>
            <p>Created a dashboard showcasing sales results before and after a marketing campaign, highlighting key insights for marketing and brand managers, using Tableau</p>
        </div>
        """, unsafe_allow_html=True)

# Skills page
elif selected == "Skills":
    header()
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <h3>TECHNICAL SKILLS</h3>
        <ul>
            <li>Python, SQL, Spark, SAS</li>
            <li>Tableau, Power BI</li>
            <li>Excel, Word, PowerPoint</li>
            <li>SAP, Siesa</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h3>SOFT SKILLS</h3>
        <ul>
            <li>Adaptability & Problem Solving</li>
            <li>Teamwork & Communication</li>
            <li>Critical Thinking</li>
            <li>Attention to Detail</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <h3>LANGUAGES</h3>
        <ul>
            <li>Spanish (Native)</li>
            <li>English (C2 - Advanced)</li>
            <li>French (C1 - Fluent)</li>
        </ul>
        """, unsafe_allow_html=True)

# Contact page
elif selected == "Contact":
    header()
    st.markdown("---")
    
    st.markdown("<h2 style='text-align: center;'>GET IN TOUCH</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <h3>CONTACT INFORMATION</h3>
            <p><i class='fas fa-phone'></i> +33 7 44 88 00 48</p>
            <p><i class='fas fa-envelope'></i> krolaromero@hotmail.com</p>
            <p><i class='fab fa-linkedin'></i> linkedin.com/in/carolandreamr</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/krolaromero@hotmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        
        # Local CSS for form styling
        st.markdown("""
        <style>
            input[type=text], input[type=email], textarea {
                width: 100%;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                margin-top: 6px;
                margin-bottom: 16px;
                resize: vertical;
                font-family: inherit;
            }
            button[type=submit] {
                background-color: #000000;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
                font-family: inherit;
            }
            button[type=submit]:hover {
                background-color: #333333;
            }
        </style>
        """, unsafe_allow_html=True)