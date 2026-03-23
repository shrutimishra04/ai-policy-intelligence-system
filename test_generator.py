from rag.generator import generate_answer

# dummy context (simulate retrieved chunk)
context = """
Employees are entitled to 7 days of casual leave (SCL) in a calendar year.
"""

query = "how many leaves do i get in a year?"

answer = generate_answer(context, query)

print("Answer:")
print(answer)