import re


def compute_tc(merge_requests):
    bot_codacy = "codacy-bot|Codacy"
    for merge_request in merge_requests:
        mr_notes = merge_request.notes.list()
        count = 0
        for note in mr_notes:
            test_bot = re.search(bot_codacy, note.body)
            if not note.system and not test_bot:
                count += 1
        print("Comentários Totais: ", count)