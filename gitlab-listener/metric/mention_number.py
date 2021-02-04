import re

exclusoes = ['@GetMapping', '@github.com', '@PreAuthorize', '@Secured', '@Inject', '@Inject.', '@OneToMany',
             '@AutenticationPrincipal', '@Query', '@Query.', '@click', '@ModelAttribute']


def compute_mn(merge_requests):
    for merge_request in merge_requests:
        notes = merge_request.notes.list()
        ocorrencias = []
        for note in notes:
            if note.system is False:
                for ocorrencia in re.findall("@[\\w.-]+", note.body):
                    if ocorrencia not in exclusoes:
                        ocorrencias.append(ocorrencia)

        print(len(ocorrencias))
