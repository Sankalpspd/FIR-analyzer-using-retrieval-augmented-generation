import json
import pandas as pd
from retrieve_sections import retrieve_sections
from exceptions import sec_exceptions
from prompt import build_prompt
from querry import query_gemini
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

    print(f"Running section {section_number}")

    short_section = section_text[:1000]
    short_fir = paragraph

    # get exceptions for the act
    exceptions = exceptions_dict.get(act, "")
    exceptions = exceptions[:1500]
    prompt = build_prompt(short_fir, short_section, exceptions)

    response = query_gemini(prompt)
    torch.cuda.empty_cache()
    print(f"\n--- Section {section_number} ---")
    print(response)
    print("-"*50)

    lines = response.strip().split("\n")
    last_two = lines[-2:]  # last 2 lines contain the data

    # Extract applicable
    applicable_matches = re.findall(r'"?applicable"?\s*:\s*(yes|no)', response, re.IGNORECASE)
    applicable = applicable_matches[-1].lower() if applicable_matches else "no"

    reason_matches = re.findall(r'"?reason"?\s*:\s*"?(.+?)"?$', response, re.IGNORECASE | re.MULTILINE)
    reason = reason_matches[-1].strip() if reason_matches else ""
    sections.append({
        "section_id": id,
        "applicable": applicable,   # yes/no or true/false
        "reason": reason,
        "Act": act
 return sections, len(retrieved_ids_offence)
