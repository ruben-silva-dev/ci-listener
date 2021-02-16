import re
from datetime import datetime

bot_codacy = "codacy-bot|Codacy"
datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


def created_at_key(note):
    return note.created_at


def compute_frt(merge_requests):
    for merge_request in merge_requests:
        notes = []
        for note in merge_request.notes.list():
            test_bot = re.findall(bot_codacy, note.body)
            if not note.system and not test_bot:
                notes.append(note)

        if notes:
            notes.sort(key=created_at_key)
            start_datetime = datetime.strptime(merge_request.created_at, datetime_format)
            end_datetime = datetime.strptime(notes[0].created_at, datetime_format)
            print(end_datetime - start_datetime)
