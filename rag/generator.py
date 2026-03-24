import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(context, query):

    if not context or len(context.strip()) == 0:
        return "I could not find this in the policy documents."

    prompt = f"""
You are an HR policy assistant.

Use ONLY the given context to answer.

Rules:
- Be concise and direct.
- Extract the answer from the context.
- Do not explain unnecessarily.
- If partial information is present, still answer using it.
- Answer only from ONE most relevant policy.
- Do not combine multiple policies.
- Only say "I could not find this in the policy documents." if nothing relevant exists.

Context:
{context[:3000]}

Question:
{query}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer strictly from context."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )

        answer = response.choices[0].message.content.strip()

        if len(answer) < 20:
            return "I could not find this in the policy documents."

        return answer

    except Exception as e:
        print("Error in LLM generation:", str(e))
        return "Error generating answer. Please try again."