import re


def compute_sccn(gl_changes):
    source_added_lines = 0
    source_removed_lines = 0

    for change in gl_changes['changes']:
        if re.search('src', change['new_path'], re.IGNORECASE):
            source_added_lines += len(re.findall("\n\\+", change['diff']))
            source_removed_lines += len(re.findall("\n-", change['diff']))

    return {
        'source_code_added_lines': source_added_lines,
        'source_code_removed_lines': source_removed_lines
    }
