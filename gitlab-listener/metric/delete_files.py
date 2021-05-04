def compute_df(changes):
    delete_count = 0

    for change in changes['changes']:
        if change['deleted_file']:
            delete_count += 1

    return delete_count
