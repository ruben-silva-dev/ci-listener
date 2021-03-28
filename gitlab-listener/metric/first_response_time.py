import re
from datetime import datetime

bot = "codacy-bot|Codacy|SonarQube analysis"
datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def created_at_key(note):
    return note.created_at


def compute_frt(gl_merge_request, gl_notes):
    notes = []
    for note in gl_notes:
        test_bot = re.findall(bot, note.body)
        if not note.system and not test_bot:
            notes.append(note)

    if notes:
        notes.sort(key=created_at_key)
        start_datetime = datetime.strptime(gl_merge_request.created_at, datetime_format)
        end_datetime = datetime.strptime(notes[0].created_at, datetime_format)
        return (end_datetime - start_datetime).total_seconds()
