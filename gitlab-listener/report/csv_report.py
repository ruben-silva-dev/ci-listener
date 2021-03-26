import csv

csv_columns = ['id', 'status', 'added_files', 'total_changes', 'deleted_files', 'modified_files', 'ci_run_time',
               'build_correction_intervals', 'total_builds', 'success_builds', 'failed_builds', 'ci_latency',
               'ci_result', 'closure_time', 'code_review_time', 'commits_number', 'first_response_time', 'total_jobs',
               'success_jobs', 'failed_jobs', 'mention_number', 'merge_time', 'participants_number',
               'source_code_added_lines', 'source_code_removed_lines', 'test_code_added_lines',
               'test_code_removed_lines', 'total_comments']


def export_csv(projects):
    for project in projects:
        try:
            with open(project['id'] + ".csv", 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for merge_request in project['merge_requests']:
                    writer.writerow(merge_request)
        except IOError:
            print("I/O error")
