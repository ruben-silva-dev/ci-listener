import pandas as pd

csv_columns = ["added_files", "total_changes", "deleted_files", "modified_files", "build_correction_intervals",
               "total_builds", "success_builds", "failed_builds", "ci_latency", "closure_time", "code_review_time",
               "commits_number", "first_response_time", "total_jobs", "success_jobs", "failed_jobs", "mention_number",
               "merge_time", "participants_number", "source_code_added_lines", "source_code_removed_lines",
               "test_code_added_lines", "test_code_removed_lines", "total_comments", "general_comments",
               "review_comments", "effective_comments"]


def generate_histogram():
    dataset = pd.read_csv("./general.csv")
    dataset[csv_columns].hist(figsize=(15, 15))
