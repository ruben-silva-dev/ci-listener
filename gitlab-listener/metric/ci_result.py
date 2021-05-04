def compute_cr(gl_pipelines):
    for pipeline in gl_pipelines:
        if pipeline['status'] == 'failed':
            return 1

    return 0
