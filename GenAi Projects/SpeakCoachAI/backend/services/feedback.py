from services.llm_service import generate_response

def evaluate_response(user_response: str, category: str):
    prompt = f"Evaluate the following {category} response:\n{user_response}"
    return generate_response(prompt, "speech coach")

def evaluate_presentation(content: str):
    prompt = f"Provide structured feedback on the following presentation:\n{content}"
    return generate_response(prompt, "presentation evaluator")
