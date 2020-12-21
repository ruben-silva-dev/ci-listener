from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_bci(merge_requests):
    for merge_request in merge_requests:
        pipelines = merge_request.pipelines()
        pipelines.sort(key=pipeline_sort)

        start_pipeline = {}
        for pipeline in pipelines:
            if pipeline['status'] == 'failed' and start_pipeline == {}:
                start_pipeline = pipeline
            elif pipeline['status'] == 'success' and start_pipeline != {}:
                start_datetime = datetime.strptime(start_pipeline['created_at'], datetime_format)
                end_datetime = datetime.strptime(pipeline['created_at'], datetime_format)

                start_pipeline = {}
                print(end_datetime - start_datetime)


def pipeline_sort(pipeline):
    return pipeline['created_at']
