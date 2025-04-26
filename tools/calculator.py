from langchain.tools import tool

@tool("calculator_tool", return_direct=True)
def calculator_tool(expression: str) -> str:
    """Evaluate math expressions like '25% of 180' or '30 + 20'."""
    try:
        expression = expression.lower().replace("of", "*").replace("%", "/100")
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"