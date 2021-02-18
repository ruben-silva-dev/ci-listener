import re

bot_codacy = "codacy-bot|Codacy"


def compute_tc(gl_notes):
    notes = []

    for note in gl_notes:
        test_bot = re.findall(bot_codacy, note.body)
        if not note.system and not test_bot:
            notes.append(note)

    return len(notes)
