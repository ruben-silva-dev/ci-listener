def compute_jn(gl_project, gl_pipelines):
    success_jobs_count = 0
    failed_jobs_count = 0

    for pipeline in gl_pipelines:
        pipeline = gl_project.pipelines.get(pipeline['id'])
        jobs = pipeline.jobs.list()

        for job in jobs:
            if job.status == 'success':
                success_jobs_count += 1
            elif job.status == 'failed':
                failed_jobs_count += 1

    return {
        'success_jobs': success_jobs_count,
        'failed_jobs': failed_jobs_count
    }
