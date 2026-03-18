def build_prompt(fir_text, section_text, exceptions):
    prompt = f"""
You are a legal AI assistant. Your task is to analyze the FIR, Legal section,
and any part of the general exceptions to determine whether the legal section is applicable to the FIR or not, subject to the exceptions.

FIR:
{fir_text}

Legal Section:
{section_text}

General Exceptions:
{exceptions}

Instructions:
1. Use ONLY the information provided in the FIR, the legal section, and the exceptions.
2. Identify key facts from the FIR.
3. Identify the legal elements required by the section.
4. Check whether the facts in the FIR satisfy those elements.
5. If a section applies, but some part of the general exceptions apply to the section and the fir, return "applicable": no.
6. If a section applies, and no part of the general exceptions apply to the section and the fir, return "applicable": yes.
7. Do NOT repeat the prompt, the FIR, the section, or any other text.
8. Only use the information provided in the FIR, section, and exceptions.
9. Follow this exact format exactly.

Output format:
"applicable": yes OR "applicable": no
"reason": "<short explanation>" (can be empty if not applicable)
"""
    return prompt.strip()
