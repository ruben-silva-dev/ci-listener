def compute_cn(merge_requests):
    for merge_request in merge_requests:
        commits = merge_request.commits()
        print(len(commits))