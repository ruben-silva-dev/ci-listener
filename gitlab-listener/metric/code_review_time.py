import re
from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'
bot_codacy = "codacy-bot|Codacy"


def compute_crt(gl_notes):
    notes = []

    for note in gl_notes:
        test_bot = re.findall(bot_codacy, note.body)
        if not note.system and not test_bot:
            notes.append(note)

    if notes:
        notes.sort(key=pipeline_sort)

        start_datetime = datetime.strptime(notes[0].created_at, datetime_format)
        end_datetime = datetime.strptime(notes[len(notes) - 1].created_at, datetime_format)

        return (end_datetime - start_datetime).total_seconds()


def pipeline_sort(note):
    return note.created_at
