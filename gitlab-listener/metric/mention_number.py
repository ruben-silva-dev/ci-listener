import re

exclusoes = ['@GetMapping', '@github.com', '@PreAuthorize', '@Secured', '@Inject', '@Inject.', '@OneToMany',
             '@AutenticationPrincipal', '@Query', '@Query.', '@click', '@ModelAttribute']


def compute_mn(gl_notes):
    ocorrencias = []

    for note in gl_notes:
        if note.system is False:
            for ocorrencia in re.findall("@[\\w.-]+", note.body):
                if ocorrencia not in exclusoes:
                    ocorrencias.append(ocorrencia)

    return len(ocorrencias)
