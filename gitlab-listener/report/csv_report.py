import csv

csv_columns = ['id', 'status', 'added_files', 'total_changes', 'deleted_files', 'modified_files',
               'build_correction_intervals', 'total_builds', 'success_builds', 'failed_builds', 'ci_latency',
               'ci_result', 'closure_time', 'comment_time', 'reviews_number', 'first_response_time', 'total_jobs',
               'success_jobs', 'failed_jobs', 'mention_number', 'review_time', 'participants_number',
               'source_code_added_lines', 'source_code_removed_lines', 'test_code_added_lines',
               'test_code_removed_lines', 'total_comments', 'general_comments', 'review_comments', 'effective_comments']


def export_individual_csv(projects):
    for project in projects:
        try:
            with open(project['id'] + "_base.csv", 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for merge_request in project['merge_requests']:
                    writer.writerow(merge_request)
        except IOError:
            print("I/O error")


def export_general_csv(projects):
    try:
        with open("general_base.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for project in projects:
                for merge_request in project['merge_requests']:
                    writer.writerow(merge_request)
    except IOError:
        print("I/O error")
