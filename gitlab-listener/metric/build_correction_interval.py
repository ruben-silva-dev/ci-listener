from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_bci(gl_pipelines):
    intervals = []

    gl_pipelines.sort(key=pipeline_sort)

    start_pipeline = {}
    for pipeline in gl_pipelines:
        if pipeline['status'] == 'failed' and start_pipeline == {}:
            start_pipeline = pipeline
        elif pipeline['status'] == 'success' and start_pipeline != {}:
            start_datetime = datetime.strptime(start_pipeline['created_at'], datetime_format)
            end_datetime = datetime.strptime(pipeline['created_at'], datetime_format)

            start_pipeline = {}
            intervals.append((end_datetime - start_datetime).total_seconds())

    return intervals


def pipeline_sort(pipeline):
    return pipeline['created_at']
