import re
from datetime import datetime

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'
bot_codacy = "codacy-bot|Codacy"


def compute_rct(merge_requests):
    for merge_request in merge_requests:
        notes = []

        for note in merge_request.notes.list():
            test_bot = re.findall(bot_codacy, note.body)
            if not note.system and not test_bot:
                notes.append(note)

        if notes:
            notes.sort(key=pipeline_sort)

            start_datetime = datetime.strptime(notes[0].created_at, datetime_format)
            end_datetime = datetime.strptime(notes[len(notes)-1].created_at, datetime_format)

            print(end_datetime - start_datetime)


def pipeline_sort(note):
    return note.created_at
