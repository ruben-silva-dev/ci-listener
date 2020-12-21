def compute_df(merge_requests):
    for merge_request in merge_requests:
        mr_changes = merge_request.changes()['changes']

        delete_count = 0
        for change in mr_changes:
            if change['deleted_file']:
                delete_count += 1

        print("Deleted files:", delete_count)
