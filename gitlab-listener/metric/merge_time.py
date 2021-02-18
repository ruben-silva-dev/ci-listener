from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_mt(gl_merge_request):
    if not gl_merge_request.merged_at is None:
        start_datetime = datetime.strptime(gl_merge_request.created_at, datetime_format)
        end_datetime = datetime.strptime(gl_merge_request.merged_at, datetime_format)
        return (end_datetime - start_datetime).total_seconds()
