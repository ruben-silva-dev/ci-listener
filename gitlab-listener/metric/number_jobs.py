def compute_jn(project, merge_requests):
    for merge_request in merge_requests:
        pipelines = merge_request.pipelines()

        success_jobs_count = 0
        failed_jobs_count = 0
        for pipeline in pipelines:
            pipeline = project.pipelines.get(pipeline['id'])
            jobs = pipeline.jobs.list()

            for job in jobs:
                if job.status == 'success':
                    success_jobs_count += 1
                elif job.status == 'failed':
                    failed_jobs_count += 1

        print(success_jobs_count, failed_jobs_count)
