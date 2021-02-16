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
    for project_id in project_ids:
        project = gl.projects.get(project_id)
        merge_requests = project.mergerequests.list(all=True)

        compute_af(merge_requests)
        compute_cf(merge_requests)
        compute_df(merge_requests)
        compute_mf(merge_requests)

        compute_bci(merge_requests)
        compute_bn(merge_requests)
        compute_cl(merge_requests)
        compute_cr(merge_requests)
        compute_crt(merge_requests)
        compute_cn(merge_requests)
        compute_frt(merge_requests)
        compute_jn(project, merge_requests)
        compute_mn(merge_requests)
        compute_mt(merge_requests)
        compute_pn(merge_requests)
        compute_sccn(merge_requests)
        compute_tccn(merge_requests)
        compute_tc(merge_requests)
