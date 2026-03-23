from retriever import retrieve
from generator import generate_answer

def ask_question(query):
    retrieved_chunks = retrieve(query)

    if not retrieved_chunks:
        return "I could not find this in the policy documents."

    context = "\n".join(retrieved_chunks[:3])

    answer = generate_answer(context, query)

    return answer


if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        answer = ask_question(query)
        print("\nAnswer:\n", answer)