from agents import Agent, Runner, function_tool
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

@function_tool
def get_order_status(
    costumer_id: str | None,
    order_id: str,
    channel: str | None
) -> str:
    
    fake_db = {
        "ORD_001": {"status": "Em trânsito", "delivery_date": "2023-10-15"},
        "ORD_002": {"status": "Entregue", "delivery_date": "2023-06-15"},
        "ORD_003": {"status": "Saiu para entrega", "delivery_date": "2023-10-19"},
        "ORD_004": {"status": "Necessário realizar pagamento de taxas", "delivery_date": "2023-03-13"},
        "ORD_005": {"status": "Preso na alfândega", "delivery_date": "2023-12-16"},
    }

    order = fake_db.get(order_id)

    if not order:
        return f"Pedido {order_id} não encontrado."
    
    return (
        f"Status do pedido {order_id}: {order['status']}. "
        f"Data de entrega: {order['delivery_date']}."
        f"Canal de atendimento: {channel if channel else 'Não especificado'}."
        f"Cliente: {costumer_id if costumer_id else 'Não especificado'}."
    )

agent = Agent(
    name="OrderStatusAgent",
    instructions="Você é um assistente que fornece informações sobre o status de pedidos. Use a função get_order_status para obter o status do pedido com base no ID do pedido fornecido. Forneça respostas claras e detalhadas.",
    model="gpt-4.1-mini",
    tools=[get_order_status]
)

result = Runner.run_sync(agent, "Qual é o status do pedido ORD_003 no canal de atendimento online?")

print(result.final_output)