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

        results, n = applicable_sections(fir_text)
        
        applicable = [sec for sec in results if sec["applicable"] == "yes"]
        st.session_state["applicable"] = applicable
        st.session_state["show_results"] = True
        
        if st.session_state.get("show_results"):

          applicable = st.session_state.get("applicable", [])

          if not applicable:
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
                       ("No", "Yes"),
                       key="summary_choice")

            if choice == "Yes":

            # Prevent recomputing every rerun
              if "summaries_generated" not in st.session_state:

                with st.spinner("Generating summaries..."):
                    summaries = add_summaries(applicable)

                st.session_state["summaries"] = summaries
                st.session_state["summaries_generated"] = True

              summaries = st.session_state["summaries"]

              st.subheader("Section Summaries")

              for sec in summaries:
                 st.subheader(f"{sec['Act']} - Section {sec['section_id']}")
                 st.write(sec.get("summary", ""))
                 st.divider()
