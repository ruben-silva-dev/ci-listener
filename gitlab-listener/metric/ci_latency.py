from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_cl(gl_merge_request, gl_pipelines):
    start_datetime = datetime.strptime(gl_merge_request.created_at, datetime_format)

    gl_pipelines.sort(key=pipeline_sort, reverse=True)

    for pipeline in gl_pipelines:
        if pipeline['status'] == 'failed' or pipeline['status'] == 'success':
            end_datetime = datetime.strptime(pipeline['created_at'], datetime_format)
            return (end_datetime - start_datetime).total_seconds()


def pipeline_sort(pipeline):
    return pipeline['created_at']
