def compute_cf(merge_requests):
    for merge_request in merge_requests:
        print(merge_request.changes()['changes_count'])
