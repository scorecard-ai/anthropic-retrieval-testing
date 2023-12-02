import os
import anthropic
import claude_retriever
from claude_retriever.searcher.searchtools.wikipedia import WikipediaSearchTool


ANTHROPIC_SEARCH_MODEL = "claude-2"


def generate_completion(
    query: str, n_search_results_to_use: int = 1, max_searches_to_try: int = 1
):
    wikipedia_search_tool = WikipediaSearchTool()

    client = claude_retriever.ClientWithRetrieval(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        verbose=True,
        search_tool=wikipedia_search_tool,
    )

    response, context, prompt = client.completion_with_retrieval(
        query=query,
        model=ANTHROPIC_SEARCH_MODEL,
        n_search_results_to_use=n_search_results_to_use,
        max_searches_to_try=max_searches_to_try,
        max_tokens_to_sample=1000,
    )

    return response, str(context)[:1000], prompt


if __name__ == "__main__":
    queries = [
        "Who won the 2024 presidential election in the US?",
        "Who won the 2023 NBA Finals?",
        "Which team lost the 2023 NBA Finals?",
        "How many games were there in the 2023 NBA Finals?",
        "How much total funding has Anthropic raised?",
    ]
    for query in queries:
        print("QUERY:", query)
        response, context, prompt = generate_completion(query, 3, 5)
        print("RESPONSE:", response, "\n\n\n")
