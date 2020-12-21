def compute_af(merge_requests):
    for merge_request in merge_requests:
        mr_changes = merge_request.changes()['changes']

        add_count = 0
        for change in mr_changes:
            if change['new_file']:
                add_count += 1

        print("Added files:", add_count)
