import os
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

agent1 = Agent(
    name="Planner",
    instructions="Você é um planejador de tarefas. Sua função é organizar e priorizar as tarefas fornecidas pelo usuário, criando um plano de ação claro e eficiente.",
)

agent2 = Agent(
    name="Developer",
    instructions="Você é um desenvolvedor de software. Sua função é implementar as tarefas planejadas pelo agente planejador, escrevendo código funcional e eficiente.",
)

agent3 = Agent(
    name="Reviewer",
    instructions="Você é um revisor de código. Sua função é revisar o código implementado pelo agente desenvolvedor, garantindo que ele esteja correto, eficiente e siga as melhores práticas de programação. E se for necessário, sugerir melhorias ou correções.",
)

def run_multiagent(input_text):
    plan = Runner.run_sync(agent1, input_text).final_output

    implementation = Runner.run_sync(
        agent2, 
        f"Plano de ação: {plan}"
    ).final_output

    review = Runner.run_sync(
        agent3,
        f"Solução implementada: {implementation}"
    ).final_output

    return review

result = run_multiagent("Crie uma automação para resumir emails importantes todo dia")
print(result)