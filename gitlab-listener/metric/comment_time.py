import re
from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'
bot = "codacy-bot|Codacy|SonarQube analysis"


def compute_cmt(gl_merge_request, gl_notes):
    notes = []

    for note in gl_notes:
        test_bot = re.findall(bot, note.body)
        if not note.system and not test_bot:
            notes.append(note)

    if notes:
        notes.sort(key=note_sort, reverse=True)

        start_datetime = datetime.strptime(gl_merge_request.created_at, datetime_format)
        end_datetime = datetime.strptime(notes[0].created_at, datetime_format)

        return (end_datetime - start_datetime).total_seconds()

    return 0


def note_sort(note):
    return note.created_at
