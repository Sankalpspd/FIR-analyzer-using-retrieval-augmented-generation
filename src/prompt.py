def build_prompt(fir_text, section_text, exceptions):
    prompt = f"""
You are a legal AI assistant. Analyze the FIR, the legal section, and the general exceptions to determine whether the legal section applies to the FIR.

FIR:
{fir_text}

Legal Section:
{section_text}

General Exceptions:
{exceptions}

Instructions:
1. Use ONLY the information provided in the FIR, the legal section, and the exceptions.
2. Identify the key facts in the FIR.
3. Identify the legal elements required by the section.
4. Determine whether the FIR facts satisfy those elements.
5. If the section's elements are satisfied AND the situation falls under a general exception, return "applicable": "no".
6. If the section's elements are satisfied AND no general exception applies, return "applicable": "yes".
7. If the FIR facts do not satisfy the section's elements, return "applicable": "no".
8. Do not repeat the FIR, the section text, or the prompt.

Return ONLY valid JSON in this exact format:

{{
  "applicable": "yes" or "no",
  "reason": "short explanation"
}}
"""
    return prompt.strip()
