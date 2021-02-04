def compute_nc(merge_requests):
    for merge_request in merge_requests:
        commits = merge_request.commits()
        count = 0
        for commit in commits:
            count = count + 1
        print(count)