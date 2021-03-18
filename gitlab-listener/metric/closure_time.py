from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def compute_ct(gl_merge_requests):
        if not gl_merge_request.updated_at is None:
            start_datetime = datetime.strptime(gl_merge_request.created_at, datetime_format)
            end_datetime = datetime.strptime(gl_merge_request.updated_at, datetime_format)
            return (end_datetime - start_datetime).total_seconds()
