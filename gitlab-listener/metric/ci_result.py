def compute_cr(merge_requests):
    for merge_request in merge_requests:
        pipelines = merge_request.pipelines()

        for pipeline in pipelines:
            if pipeline['status'] == 'failed':
                print("True")
                break
