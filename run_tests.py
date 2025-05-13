import os
import re
from typing import Any

from scorecard_ai import Scorecard
from scorecard_ai.lib import run_and_evaluate


def run_system(system_input: dict[str, Any]) -> dict:
    """
    FIXME: Replace this placeholder function with a call to your model
    """
    return {
        "response": f"Placeholder LLM response, got input: {system_input}",
    }


def main(
    *, scorecard_api_key: str, project_id: str, testset_id: str, metric_ids: list[str]
) -> None:
    """
    Run and score all Testcases in a given Testset
    """
    client = Scorecard(api_key=scorecard_api_key)

    run = run_and_evaluate(
        client=client,
        project_id=project_id,
        testset_id=testset_id,
        metric_ids=metric_ids,
        system=run_system,
    )

    print(run["url"])


if __name__ == "__main__":
    main(
        scorecard_api_key=os.environ["SCORECARD_API_KEY"],
        project_id=os.environ["PROJECT_ID"],
        testset_id=os.environ["TESTSET_ID"],
        metric_ids=re.findall(r"\b\d+\b", os.environ["METRIC_IDS"]),
    )
