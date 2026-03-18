import nltk
import streamlit as st
from applicable_sections import applicable_sections
from summaries import add_summaries
nltk.download('punkt_tab')
nltk.download('punkt')
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

st.title("FIR Legal Section Analyzer")

st.subheader("Enter FIR Details")

# Structured input fields
date = st.text_input("Date of Incident")
place = st.text_input("Place of Incident")
accused = st.text_input("Accused Name(s)")
victim = st.text_input("Victim Name(s)")
description = st.text_area("Incident Description", height=200)

# Combine into FIR text
fir_text = f"""
Date: {date}
Place: {place}
Accused: {accused}
Victim: {victim}
Description: {description}
"""

if st.button("Analyze FIR"):

    if description.strip() == "":
        st.warning("Please enter incident description.")
    else:

        results = applicable_sections(fir_text)
        st.write(len(applicable_sections))
        applicable = [sec for sec in results if sec["applicable"] == "yes"]

        if applicable == []:
            st.info("No applicable sections found.")

        else:
            st.subheader("Applicable Sections")

            for sec in applicable:
                st.subheader(f"{sec['Act']} - Section {sec['section_id']}")
                st.write("Reason:", sec["reason"])
                st.divider()

            # Ask user for summaries
            st.subheader("Need section summaries?")

            choice = st.radio(
                "If you want, I can give you summaries of each section:",
                ("No", "Yes")
            )

            if choice == "Yes":

                with st.spinner("Generating summaries..."):
                    applicable = add_summaries(applicable)

                st.subheader("Section Summaries")

                for sec in applicable:
                    st.subheader(f"{sec['Act']} - Section {sec['section_id']}")
                    st.write(sec.get("summary", ""))
                    st.divider()
