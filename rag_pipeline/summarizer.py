from langchain.llms import OpenAI

class Summarizer:
    def __init__(self, api_key):
        self.llm = OpenAI(api_key=api_key)

    def summarize(self, text):
        prompt = f"Summarize the following financial news:\n\n{text}"
        return self.llm(prompt)
