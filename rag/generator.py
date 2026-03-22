import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(context, query):
    """
    Generate answer using LLM based on retrieved context
    """

    if not context:
        return "I could not find this in the policy documents."

    prompt = f"""
You are an HR policy assistant.

Instructions:
- Answer ONLY using the provided context.
- Do NOT make up information.
- If answer is not clearly present, say:
  "I could not find this in the policy documents."

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise HR policy assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Error in LLM generation:", str(e))
        return "Error generating answer. Please try again."