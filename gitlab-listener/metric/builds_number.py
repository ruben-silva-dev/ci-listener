def compute_bn(merge_requests):
    for merge_request in merge_requests:
        pipelines = merge_request.pipelines()

        success_count = 0
        failed_count = 0
        for pipeline in pipelines:
            if pipeline['status'] == 'success':
                success_count += 1
            elif pipeline['status'] == 'failed':
                failed_count += 1

        print("Total:", len(pipelines))
        print("Success:", success_count)
        print("Failed:", failed_count)
