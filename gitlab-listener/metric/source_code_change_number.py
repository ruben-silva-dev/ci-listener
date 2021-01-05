import re


def compute_sccn(merge_requests):
    for merge_request in merge_requests:
        changes = merge_request.changes()

        source_added_lines = 0
        source_removed_lines = 0
        for change in changes['changes']:
            if re.search('src', change['new_path'], re.IGNORECASE):
                source_added_lines += len(re.findall("\n\\+", change['diff']))
                source_removed_lines += len(re.findall("\n-", change['diff']))

        print(source_added_lines, source_removed_lines)
