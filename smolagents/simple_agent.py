import sys

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(),
    additional_authorized_imports=["time", "datetime", "pandas"]
    )


if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = input("Enter a search query: ")


agent.run(query)