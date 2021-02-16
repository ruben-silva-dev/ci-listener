import re


def compute_tccn(merge_requests):
    for merge_request in merge_requests:
        changes = merge_request.changes()

        test_added_lines = 0
        test_removed_lines = 0
        for change in changes['changes']:
            if re.search('test', change['new_path'], re.IGNORECASE):
                test_added_lines += len(re.findall("\n\\+", change['diff']))
                test_removed_lines += len(re.findall("\n-", change['diff']))

        print(test_added_lines, test_removed_lines)
