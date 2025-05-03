from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Shubham_Agrawal_Data_Scientist.pdf"
profile_pic = current_dir / "assets" / "DSC_1510.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shubham Agrawal"
PAGE_ICON = ":wave:"
NAME = "Shubham Agrawal"
DESCRIPTION = """
Data professional with 3 years of QlikView experience, upskilled in SQL, Python, Deep Learning and Machine Learning, seeking to transition into a Data Scientist role to leverage analytical capabilities for impactful insights.
"""
EMAIL = "13shubhi@gmail.com"

PROJECTS = {
    "📊 Credit Card Default Prediction:": {
        "link": "https://www.kaggle.com/code/shubhi13/credit-card-default-prediction#Compare-the-Model",
        "description": "Performed EDA, hypothesis testing, and feature engineering on credit card usage data to build a default prediction model. Compared Logistic Regression, Random Forest, and XGBoost using cross-validation and hyperparameter tuning. Achieved best results with XGBoost: ROC AUC Score 0.78 and Accuracy 82%, highlighting key drivers of default risk."
    },
    "📈 Sentiment Analysis": {
        "link": "https://www.kaggle.com/code/shubhi13/sentiment-analysis-nlp-bow-td-idf-word2vec?scriptVersionId=216155492",
        "description": "Built an NLP pipeline applying data cleaning, tokenization, BoW, TF-IDF, and Word2Vec vectorization techniques. Trained and compared Feedforward Neural Networks across different vectorization for sentiment classification. Achieved 86% accuracy and 0.93 AUC score using Word2Vec embeddings, outperforming other techniques."
    },
    "📉 Mumbai’s Temperature Prediction and Forecasting:": {
        "link": "https://www.kaggle.com/code/shubhi13/predicting-mumbai-temperature-regression-analysis#Compare-the-Model",
        "description": "Built deep learning models (RNN, LSTM, Bi-LSTM, GRU) to forecast Mumbai's temperature using historical weather data. Engineered lag features, scaled data, and optimized hyperparameters to improve model accuracy. GRU model achieved the best performance with an RMSE of 1.46, providing highly accurate temperature forecasts."
    },
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD ASSETS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    st.image(profile_pic, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- CONNECT WITH ME ---
st.write("\n")
st.write("\n")
st.markdown("### Connect with Me")

contact_cols = st.columns(4)
st.write("\n")

# Phone
contact_cols[0].markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center;'>
        <img src="https://cdn-icons-png.flaticon.com/512/724/724664.png" width="20" style="margin-right: 8px;" />
        <span>+91 8447172967</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Email
contact_cols[1].markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center;'>
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" width="20" style="margin-left: 80px; margin-right: 8px;" />
        <span>13shubhi@gmail.com</span>
    </div>
    """,
    unsafe_allow_html=True
)

# LinkedIn
contact_cols[2].markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center;'>
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" style="margin-left: 72px; margin-right: 8px;" />
        <a href="https://www.linkedin.com/in/shubham-agrawal-374b94108" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)

# GitHub
contact_cols[3].markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center;'>
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="18" style="margin-right: 6px;" />
        <a href="https://github.com/13shubhi" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown("<h3>Experience & Qualifications</h3><hr>", unsafe_allow_html=True)

st.write(
    """
- 3+ years of experience developing KPI dashboards for margin optimization and commercial performance analysis
- Solid foundation in statistics, hypothesis testing, and exploratory data analysis (EDA) for data-driven insights
- Strong knowledge of Python, SQL, and Machine Learning techniques with real-world application in modeling and automation  
- Applied deep learning (RNN, LSTM, GRU) and NLP models for forecasting and sentiment analysis with high accuracy  
- Demonstrated strength in cross-functional collaboration, leading training sessions, acting as an individual contributor, and managing stakeholder expectations across global teams  
"""
)

# --- TECHNICAL SKILLS ---
st.write("\n")
st.markdown("<h3>Technical Skills</h3><hr>", unsafe_allow_html=True)

st.markdown(
    """
- **Programming Languages & Libraries:** Python (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow), SQL  
- **Machine Learning & Deep Learning:** Supervised Learning, Unsupervised Learning, Feature Engineering, Model Validation, Neural Networks, RNN, LSTM, GRU  
- **Natural Language Processing (NLP):** Text Preprocessing, Bag of Words (BoW), TF-IDF, Word2Vec  
- **Data Analytics & Visualization:** QlikView, QlikSense, Google Spreadsheet, Matplotlib, Seaborn  
- **Statistics & Data Analysis:** Descriptive Statistics, Hypothesis Testing, EDA  
- **Relevant Coursework:** SQL (Namaste SQL – Ankit Bansal), Deep Learning & NLP (Krish Naik, CampusX)  
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.markdown("<h3>Work History</h3><hr>", unsafe_allow_html=True)

# Holcim
st.markdown(
    """
    <div style='display: flex; justify-content: space-between; align-items: center;'>
        <div style='display: flex; align-items: center;'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a2/LogoHolcim2021.svg" width="100" style="margin-right: 10px;" />
            <strong>| Business Intelligence Developer</strong>
        </div>
        <div>03/2022 - Present</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
- Designed interactive dashboards in QlikView and Qlik Sense, consolidating KPIs for real-time analysis  
- Developed advanced visualizations to track performance and enable insight generation  
- Collaborated with data engineering to maintain Global Pricing Tool for EMEA, APAC, LATAM  
- Automated KPI reporting, reducing manual hours by ~30%  
- Led training sessions and supported cross-functional teams for smooth adoption  
"""
)

# HCL
logo_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAwAB/NYtHT8AAAAASUVORK5CYII="

st.markdown(
    f"""
    <div style='display: flex; justify-content: space-between; align-items: center;'>
        <div style='display: flex; align-items: center;'>
            <img src="data:image/png;base64,{logo_base64}" width="100" style="margin-right: 10px;" />
            <strong>| Intern</strong>
        </div>
        <div>12/2020 - 01/2021</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
- Analyzed survey data related to employment, income, and migration  
- Created Excel dashboard and conducted Univariate analysis on demographics  
"""
)

# --- PROJECTS ---
st.write("\n")
st.markdown("<h3>Projects</h3><hr>", unsafe_allow_html=True)

for project, details in PROJECTS.items():
    st.markdown(f"**{project}**")
    st.markdown(f"[View Project]({details['link']})")
    st.write(f"**Description:** {details['description']}")