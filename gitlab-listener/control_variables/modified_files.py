def compute_mf(changes):
    modified_count = 0

    for change in changes['changes']:
        if ~change['new_file'] and ~change['deleted_file']:
            modified_count += 1

    return modified_count
