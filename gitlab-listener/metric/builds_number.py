def compute_bn(gl_pipelines):
    success_count = 0
    failed_count = 0
    for pipeline in gl_pipelines:
        if pipeline['status'] == 'success':
            success_count += 1
        elif pipeline['status'] == 'failed':
            failed_count += 1

    return {
        'total_builds': len(gl_pipelines),
        'success_builds': success_count,
        'failed_builds': failed_count
    }
