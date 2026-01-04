# app.py
from medical_project_1 import routed_qa, route_query, symptom_sub_router, is_emergency
import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Medical RAG Assistant (WHO/CDC)",
    page_icon="🩺",
    layout="centered"
)

# -------------------------------
# Header Section
# -------------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>🩺 Medical RAG Assistant</h1>
    <p style='text-align: center; font-size: 18px;'>
    WHO & CDC Guideline–Based Medical Information System
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    ⚠️ **Disclaimer**  
    This system provides informational guidance based on WHO and CDC documents.  
    It does **NOT** provide medical diagnosis or treatment.  
    For emergencies, consult a healthcare professional immediately.
    """
)

st.divider()

# -------------------------------
# Input Section
# -------------------------------
st.markdown("### 🔍 Ask a Medical Question")

question = st.text_input(
    "",
    placeholder="e.g. High fever with headache and body pain",
    label_visibility="collapsed"
)

# -------------------------------
# Helper: Routing Info
# -------------------------------
def show_routing_info(question: str):
    if is_emergency(question):
        st.error("🚨 **Emergency detected** → Immediate escalation")
        return

    route = route_query(question)
    st.info(f"🔀 **Primary route:** `{route}`")

    if route == "symptom":
        sub = symptom_sub_router(question)
        st.info(f"🧭 **Symptom sub-route:** `{sub}`")

# -------------------------------
# Action Button
# -------------------------------
st.markdown("")  # spacing
run = st.button("🩺 Get Medical Guidance", use_container_width=True)

if run and question.strip():

    with st.spinner("Analyzing using WHO/CDC guidelines..."):
        answer = routed_qa(question)

    # ---------------------------
    # Routing Explanation
    # ---------------------------
    st.markdown("### 🧠 System Decision")
    show_routing_info(question)

    # ---------------------------
    # Answer Output
    # ---------------------------
    st.markdown("### 📘 Guidance Based on WHO/CDC")
    st.success(answer)

elif run:
    st.warning("Please enter a question or symptoms before submitting.")

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>"
    "Built with LangChain Runnables, FAISS, and WHO/CDC documents<br>"
    "Educational & research use only"
    "</p>",
    unsafe_allow_html=True
)
