import os
import anthropic
import claude_retriever
from claude_retriever.searcher.searchtools.wikipedia import WikipediaSearchTool


ANTHROPIC_SEARCH_MODEL = "claude-2"


def generate_completion(query: str):
    wikipedia_search_tool = WikipediaSearchTool()

    client = claude_retriever.ClientWithRetrieval(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        verbose=True,
        search_tool=wikipedia_search_tool,
    )

    query = "Can you explain what LK-99 is?"

    response, context, prompt = client.completion_with_retrieval(
        query=query,
        model=ANTHROPIC_SEARCH_MODEL,
        n_search_results_to_use=1,
        max_searches_to_try=3,
        max_tokens_to_sample=1000,
    )

    return response, str(context)[:1000], prompt
