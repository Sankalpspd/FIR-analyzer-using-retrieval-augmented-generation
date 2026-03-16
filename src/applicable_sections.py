import json
import pandas as pd
from retrieve_sections import retrieve_sections
from exceptions import sec_exceptions
from prompt import build_prompt
from querry import query_llm
def applicable_sections(fir_text):
 offence_df = pd.read_excel("data/offence_sections_df.excel")
 retrieved_ids_offence = retrieve_sections(fir_text)
 sections = []

 for id in retrieved_ids_offence:

    row = offence_df.loc[offence_df["vector_id"] == id].iloc[0]

    section_title = row["section_title"]
    section_text = row["section_text"]
    section_number = row["section_number"]
    act = row["Act"]

    short_section = section_text[:1500]
    short_fir = fir_text

    # get exceptions for the act
    exceptions = sec_exceptions(act)
    exceptions = exceptions[:2500]

    prompt = build_prompt(short_fir, short_section, exceptions)

    response = query_llm(prompt)

    # Default values
    applicable = "no"
    reason = ""

    try:
        data = json.loads(response)
        applicable = data.get("applicable", "no").lower()
        reason = data.get("reason", "")
    except Exception:
        reason = "Invalid JSON response from model."

    sections.append({
        "section_title": section_title,
        "section_id": id,
        "applicable": applicable,
        "reason": reason,
        "Act": act
    })
    return sections, len(retrieved_ids_offence)
