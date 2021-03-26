from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_cirt(gl_pipelines):
    gl_pipelines.sort(key=pipeline_sort)

    start_datetime = datetime.strptime(gl_pipelines[0].created_at, datetime_format)
    end_datetime = datetime.strptime(gl_pipelines[len(gl_pipelines) - 1].created_at, datetime_format)

    return (end_datetime - start_datetime).total_seconds()


def pipeline_sort(pipeline):
    return pipeline.created_at
