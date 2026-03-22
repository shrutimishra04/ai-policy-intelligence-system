def build_prompt(context, query):
    context_text = "\n\n".join(context)

    prompt = f"""
You are an HR Policy Assistant.

Answer ONLY from the context below.
If answer not found, say:
"I could not find this in the policy documents."

Context:
{context_text}

Question:
{query}

Answer:
"""
    return prompt