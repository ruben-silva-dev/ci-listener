from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_cl(merge_requests):
    for merge_request in merge_requests:
        start_datetime = datetime.strptime(merge_request.created_at, datetime_format)

        pipelines = merge_request.pipelines()
        pipelines.sort(key=pipeline_sort, reverse=True)

        for pipeline in pipelines:
            if pipeline['status'] == 'failed' or pipeline['status'] == 'success':
                end_datetime = datetime.strptime(pipeline['created_at'], datetime_format)
                print(end_datetime - start_datetime)
                break


def pipeline_sort(pipeline):
    return pipeline['created_at']