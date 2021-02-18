import re


def compute_tccn(gl_changes):
    test_added_lines = 0
    test_removed_lines = 0

    for change in gl_changes['changes']:
        if re.search('test', change['new_path'], re.IGNORECASE):
            test_added_lines += len(re.findall("\n\\+", change['diff']))
            test_removed_lines += len(re.findall("\n-", change['diff']))

    return {
        'test_code_added_lines': test_added_lines,
        'test_code_removed_lines': test_removed_lines
    }
