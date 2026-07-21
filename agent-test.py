import os 
from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name="TestAgent",
    instructions="Você é um tutor que explica sobre Http e Https, e como eles funcionam. Você deve fornecer explicações detalhadas e exemplos práticos para ajudar os alunos a entenderem os conceitos. Seja claro, conciso e use uma linguagem acessível.",
    model="gpt-4.1-mini"
)

result = Runner.run_sync(agent, "Explique a diferença entre Http e Https e como eles funcionam.")
print(result.final_output)