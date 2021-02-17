def compute_af(changes):
    add_count = 0

    for change in changes['changes']:
        if change['new_file']:
            add_count += 1

    return add_count
