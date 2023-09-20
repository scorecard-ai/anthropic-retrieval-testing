"""
Script that runs an ad hoc test suite for the Wikipedia task.

Testset and results use the Scorecard SDK.
"""

from scorecard import utils as scorecard
from demo import wikipedia_retrieval


def run_all_tests(input_testset_id: int, scoring_config_id: int, model_params: dict):
    # Start a new run and fetch the testcases
    run_id = scorecard.create_run(
        input_testset_id, scoring_config_id, model_params=model_params
    )
    testcases = scorecard.get_testset(input_testset_id)

    if not testcases:
        print("No testcases found. Exiting.")
        return

    for testcase in testcases:
        print(f"Running testcase {testcase['id']}...")
        print(f"User query: {testcase['user_query']}")

        # Call the anthropic retrieval system
        response, context, prompt = wikipedia_retrieval.generate_completion(
            testcase["user_query"]
        )
        # Log the result back to Scorecard for scoring
        scorecard.log_record(
            run_id=run_id,
            testcase_id=testcase["id"],
            model_response=response,
            context=context,
            prompt=prompt,
            model_params=model_params,
        )

    # Mark the run as complete
    scorecard.update_run_status(run_id, "awaiting_scoring")


if __name__ == "__main__":
    INPUT_TESTSET_ID = 126
    SCORING_CONFIG_ID = 1
    MODEL_PARAMS = {
        "model_name": "claude-2",
        "n_search_results_to_use": 1,
        "max_searches_to_try": 3,
        "max_tokens_to_sample": 1000,
        "temperature": 1.0,
    }
    run_all_tests(INPUT_TESTSET_ID, SCORING_CONFIG_ID, MODEL_PARAMS)
