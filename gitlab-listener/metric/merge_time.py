from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_mt(merge_requests):
    for merge_request in merge_requests:
        if not merge_request.merged_at is None:
            start_datetime = datetime.strptime(merge_request.created_at, datetime_format)
            end_datetime = datetime.strptime(merge_request.merged_at, datetime_format)
            print(end_datetime - start_datetime)
