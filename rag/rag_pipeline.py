from retriever import retrieve
from generator import generate_answer

def ask_question(query):
    query = query + " employee policy HR rules leave benefits"
    retrieved_chunks = retrieve(query)

    if not retrieved_chunks:
        return "I could not find this in the policy documents."

    # Convert list of chunks → single context string
    context = "\n".join(retrieved_chunks)

    answer = generate_answer(context, query)

    return answer


if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        answer = ask_question(query)
        print("\nAnswer:\n", answer)