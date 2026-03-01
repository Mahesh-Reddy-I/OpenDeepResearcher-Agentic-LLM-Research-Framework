from agents.planner import Planner
from agents.searcher import Searcher
from agents.writer import Writer

MODEL_NAME = "qwen2.5-vl-3b-instruct"
BASE_URL = "http://localhost:1234/v1"

def run_research(query: str):
    planner = Planner(MODEL_NAME, BASE_URL)
    searcher = Searcher()
    writer = Writer(MODEL_NAME, BASE_URL)

    print("Planning research...")
    sub_questions = planner.create_plan(query)

    final_report = ""

    for sq in sub_questions:
        print(f"Researching: {sq}")

        print("Calling searcher...")
        search_data = searcher.search(sq)
        print("Searcher done.")

        print("Calling writer...")
        summary = writer.summarize(sq, search_data)
        print("Writer done.")

        final_report += f"\n## {sq}\n{summary}\n"

    return final_report


if __name__ == "__main__":
    topic = "Impact of AI on healthcare"
    report = run_research(topic)
    print(report)