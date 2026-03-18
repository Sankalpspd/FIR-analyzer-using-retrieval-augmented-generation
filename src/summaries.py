from summary_prompt import build_summary_prompt
from querry import query_gemini
def add_summaries(applicable_sections):

    for sec in applicable_sections:

        section_text = sec["section_text"]

        prompt = build_summary_prompt(section_text)  # truncate

        response = query_gemini(prompt)
        summary = response

        sec["summary"] = summary

    return applicable_sections
