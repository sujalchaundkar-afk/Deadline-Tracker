import streamlit as st
import google.generativeai as genai
from PIL import Image
from prompts import SYSTEM_PROMPT
from action_tool import send_email

st.set_page_config(page_title="Deadline Tracker", page_icon="⏰", layout="centered")

st.title("⏰ Deadline Tracker")
st.caption("Upload a syllabus, timetable, or assignment sheet to extract deadlines and send alerts.")

# Initialize Gemini Client
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("Please configure `GEMINI_API_KEY` in `.streamlit/secrets.toml`.")

# Sidebar for action target setup
st.sidebar.header("Notification Setup")
action_channel = st.sidebar.radio("Send Alerts Via:", ["Gmail (SMTP)"])

recipient_info = ""
if action_channel == "Gmail (SMTP)":
    recipient_info = st.sidebar.text_input("Recipient Email Address", placeholder="user@example.com")


# Image Upload
uploaded_file = st.file_uploader("Upload Image (Syllabus / Timetable / Assignment)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Document", use_container_width=True)

    if st.button("Extract Deadlines"):
        with st.spinner("Analyzing image with Gemini Vision..."):
            try:
                model = genai.GenerativeModel("gemini-3.6-flash")
                response = model.generate_content([SYSTEM_PROMPT, image])
                st.session_state["extracted_deadlines"] = response.text
            except Exception as e:
                st.error(f"Error processing image: {e}")

# Display extracted output
if "extracted_deadlines" in st.session_state:
    st.subheader("📋 Detected Deadlines & Digest")
    st.markdown(st.session_state["extracted_deadlines"])

    st.divider()
    if st.button(f"Send Alert via {action_channel}"):
        if not recipient_info:
            st.warning("Please enter recipient details in the sidebar first.")
        else:
            with st.spinner("Dispatching alert..."):
                success = False
                if action_channel == "Gmail (SMTP)":
                    success = send_email(
                        to_address=recipient_info,
                        subject="📅 Upcoming Deadline Digest",
                        body=st.session_state["extracted_deadlines"]
                    )
                else:
                    success = send_telegram(
                        chat_id=recipient_info,
                        text=st.session_state["extracted_deadlines"]
                    )
                
                if success:
                    st.success("Deadline digest successfully sent!")