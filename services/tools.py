from llama_index.core.tools import QueryEngineTool
from utils.all_prints import print_error

def get_tools(engine_dict):
    try:
        query_engine_tools = []
    
        for k, v in engine_dict.items():
            query_engine_tools.append(
                QueryEngineTool.from_defaults(
                    query_engine=v,
                    name=f"{k}_10k",
                    description= (
                        f"Delivers insights and information about {k}'s 2024 financial data.",
                        "You'll provided with a detailed, plain text question to obtain the most relevant and precise responses"
                    )
                )
            )

        return query_engine_tools
    except Exception as e:
        print_error(e, "Error in get_tools function in tools.py")

