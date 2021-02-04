import re

bot_codacy = "codacy-bot|Codacy"


def compute_tc(merge_requests):
    for merge_request in merge_requests:
        notes = []

        for note in merge_request.notes.list():
            test_bot = re.findall(bot_codacy, note.body)
            if not note.system and not test_bot:
                notes.append(note)

        print("Comentários Totais: ", len(notes))
