def compute_mf(merge_requests):
    for merge_request in merge_requests:
        mr_changes = merge_request.changes()['changes']

        modified_count = 0
        for change in mr_changes:
            if ~change['new_file'] and ~change['deleted_file']:
                modified_count += 1

        print("Modified files:", modified_count)
