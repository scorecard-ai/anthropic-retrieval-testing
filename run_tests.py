import os
from scorecard.client import Scorecard


def query_model(prompt: str) -> str:
    """
    FIXME: Replace this placeholder function with a call to your model
    """
    return f"Placeholder LLM response, got prompt: {prompt}"


def main(testset_id: int, scoring_config_id: int):
    """
    Run and score all testcases in a given testset
    """
    client = Scorecard(api_key=SCORECARD_API_KEY)
    client.run_tests(
      input_testset_id=testset_id,
      scoring_config_id=scoring_config_id,
      model_invocation=query_model,
    )


if __name__ == "__main__":
    TESTSET_ID = int(os.environ["TESTSET_ID"])
    SCORING_CONFIG_ID = int(os.environ["SCORING_CONFIG_ID"])
    SCORECARD_API_KEY = os.environ["SCORECARD_API_KEY"]
    main(TESTSET_ID, SCORING_CONFIG_ID)
