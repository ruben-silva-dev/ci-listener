def compute_np(merge_requests):
    for merge_request in merge_requests:
        participants = merge_request.participants()
        print(len(participants))
