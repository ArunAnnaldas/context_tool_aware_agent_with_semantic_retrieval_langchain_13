from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from memory.vector_store import create_vector_memory
from tools.calculator import calculator_tool
from langchain_community.callbacks.manager import get_openai_callback

llm = ChatOpenAI(temperature=0)

tools = [calculator_tool]

conversation_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    memory=conversation_memory,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)

vector_memory = create_vector_memory()
retriever = vector_memory.as_retriever()

def run_agent():
    queries = [
        "What is 20% of 180?",
        "Add 30 to that.",
        "Remind me what the original query was.",
    ]

    for q in queries:
        print(f"\n🗣️ User: {q}")
        with get_openai_callback() as cb:
            response = agent.run(q)
            print(f"🤖 Agent: {response}")
            print(f"📊 Token Usage: {cb.total_tokens} tokens")

        # Semantic retrieval
        print("\n🔎 Relevant documents from vector memory:")
        docs = retriever.get_relevant_documents(q)
        for doc in docs:
            print("•", doc.page_content)

if __name__ == "__main__":
    run_agent()