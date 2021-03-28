import re

bot = "codacy-bot|Codacy|SonarQube analysis"


def compute_comments(gl_notes):
    total_comments = 0
    general_comments = 0
    review_comments = 0
    effective_comments = 0

    for note in gl_notes:
        test_bot = re.findall(bot, note.body)

        if not note.system and not test_bot:
            total_comments += 1

            if note.type == 'DiscussionNote' or note.type is None:
                general_comments += 1

            elif note.type == 'DiffNote':
                review_comments += 1

                if note.resolved:
                    effective_comments += 1

    return {
        'total_comments': total_comments,
        'general_comments': general_comments,
        'review_comments': review_comments,
        'effective_comments': effective_comments
    }
