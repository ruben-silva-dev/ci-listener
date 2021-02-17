import os

import gitlab

from control_variables.add_files import compute_af
from control_variables.changing_files import compute_cf
from control_variables.delete_files import compute_df
from control_variables.modified_files import compute_mf
from metric.build_correction_interval import compute_bci
from metric.builds_number import compute_bn
from metric.ci_latency import compute_cl
from metric.ci_result import compute_cr
from metric.closure_time import ClosureTime
from metric.code_review_time import compute_crt
from metric.commits_number import compute_cn
from metric.effective_comments import EffectiveComments
from metric.first_response_time import compute_frt
from metric.general_comments import GeneralComments
from metric.jobs_number import compute_jn
from metric.mention_number import compute_mn
from metric.merge_time import compute_mt
from metric.participants_number import compute_pn
from metric.review_comments import ReviewComments
from metric.source_code_changes_number import compute_sccn
from metric.test_code_changes_number import compute_tccn
from metric.total_comments import compute_tc

gl = gitlab.Gitlab.from_config('global', ['.python-gitlab.cfg'])
project_ids = list(os.environ['PROJECTS'].split(","))

ct = ClosureTime(gl)
ec = EffectiveComments(gl)
gc = GeneralComments(gl)
rc = ReviewComments(gl)

if __name__ == '__main__':
    projects = []

    for project_id in project_ids:
        project = {
            'id': project_id,
            'merge_requests': []
        }

        gl_project = gl.projects.get(project_id)

        for gl_merge_request in gl_project.mergerequests.list(all=True):
            merge_request = {
                'id': gl_merge_request.id
            }

            gl_changes = gl_merge_request.changes()

            merge_request['added_files'] = compute_af(gl_changes)
            merge_request['total_changes'] = compute_cf(gl_changes)
            merge_request['deleted_files'] = compute_df(gl_changes)
            merge_request['modified_files'] = compute_mf(gl_changes)

        # compute_bci(gl_merge_requests)
        # compute_bn(gl_merge_requests)
        # compute_cl(gl_merge_requests)
        # compute_cr(gl_merge_requests)
        # compute_crt(gl_merge_requests)
        # compute_cn(gl_merge_requests)
        # compute_frt(gl_merge_requests)
        # compute_jn(gl_project, gl_merge_requests)
        # compute_mn(gl_merge_requests)
        # compute_mt(gl_merge_requests)
        # compute_pn(gl_merge_requests)
        # compute_sccn(gl_merge_requests)
        # compute_tccn(gl_merge_requests)
        # compute_tc(gl_merge_requests)

            project['merge_requests'].append(merge_request)

        projects.append(project)

    print(projects)
