from collections import Counter

import numpy as np
import pandas as pd

cr_metrics = ["added_files", "total_changes", "deleted_files", "modified_files", "closure_time", "comment_time",
              "reviews_number", "first_response_time", "mention_number", "review_time", "participants_number",
              "source_code_added_lines", "source_code_removed_lines", "test_code_added_lines",
              "test_code_removed_lines", "total_comments", "general_comments", "review_comments", "effective_comments"]
ci_metrics = ["ci_result", "build_correction_intervals", "total_builds", "success_builds", "failed_builds",
              "ci_latency", "total_jobs", "success_jobs", "failed_jobs"]


def detect_outliers(df, n, features):
    outlier_indices = []
    for col in features:
        df.sort_values(by=[col], inplace=True, ascending=False)

        q1 = np.percentile(df[col], 25)
        q3 = np.percentile(df[col], 75)
        iqr = q3 - q1
        outlier_step = 1.5 * iqr
        outlier_list_col = df[(df[col] < q1 - outlier_step) | (df[col] > q3 + outlier_step)].index
        outlier_indices.extend(outlier_list_col)

    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items()
                             )
    return multiple_outliers


def outliers_removal(path_input, path_output):
    df = pd.read_csv(path_input)

    drop_cr_outliers = detect_outliers(df, 1, cr_metrics)
    cr_df = pd.concat([df, df.loc[drop_cr_outliers].copy()]).drop_duplicates(keep=False)

    drop_ci_outliers = detect_outliers(df, 1, ci_metrics)
    ci_df = pd.concat([df, df.loc[drop_ci_outliers].copy()]).drop_duplicates(keep=False)

    no_outliers_df = pd.concat([cr_df, ci_df]).drop_duplicates(keep=False)
    no_outliers_df.to_csv(path_output, index=False)


def run_tukey_test(projects):
    for project in projects:
        path_input = project + "_base.csv"
        path_output = project + "_without_outliers.csv"
        outliers_removal(path_input, path_output)

    outliers_removal("general_base.csv", "general_without_outliers.csv")
