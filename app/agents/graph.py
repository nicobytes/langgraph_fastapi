from app.agents.simple import agent
from langchain_core.messages import HumanMessage

class LangGraphAgent:
    async def get_response(self, message: str):
        config = {
            "configurable": {"thread_id": '123'},
        }
        human_message = HumanMessage(content=message)
        return agent.invoke({"messages": [human_message]}, config)
