from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_rt(gl_merge_request):
    if gl_merge_request.state == 'merged':
        start_datetime = datetime.strptime(gl_merge_request.created_at, datetime_format)
        end_datetime = datetime.strptime(gl_merge_request.updated_at, datetime_format)
        return (end_datetime - start_datetime).total_seconds()

    return 0
