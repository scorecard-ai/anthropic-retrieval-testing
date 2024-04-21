"""
Script that runs an automated test suite for your project.

Testset and results use the Scorecard SDK.
"""

import os
import requests
import scorecard

SCORECARD_API_KEY = os.environ["SCORECARD_API_KEY"]

PROMPT_TEMPLATE = """
Human: Please read the following question and answer by choosing A or B.
In your output include A or B and the full text of the answer. {user_query}

Assistant:"""


def query_model(user_query: str):
    # FIXME: Please replace this placeholder function with the
    # necessary code to query your model's API.

    data["prompt"] = PROMPT_TEMPLATE.format(user_query=user_query)

    response = "CALL YOUR API ENDPOINT HERE"
    if response.status_code != 200:
        raise Exception(f"Model API Error: {response.status_code} {response.text}")

    return response.text()


def run_all_tests(input_testset_id: int, scoring_config_id: int):
    run_id = scorecard.create_run(input_testset_id, scoring_config_id, MODEL_PARAMS)
    testcases = scorecard.get_testset(input_testset_id)

    for testcase in testcases:
        print(f"Running testcase {testcase['id']}...")
        print(f"User query: {testcase['user_query']}")

        model_response = query_model(testcase["user_query"])

        scorecard.log_record(
            run_id, testcase["id"], model_response, PROMPT_TEMPLATE, MODEL_PARAMS
        )

    scorecard.update_run_status(run_id)


if __name__ == "__main__":
    INPUT_TESTSET_ID = int(os.environ["INPUT_TESTSET_ID"])
    SCORING_CONFIG_ID = int(os.environ["SCORING_CONFIG_ID"])
    run_all_tests(INPUT_TESTSET_ID, SCORING_CONFIG_ID)