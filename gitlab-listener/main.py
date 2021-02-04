import os

import gitlab

from control_variables.add_files import compute_af
from control_variables.changing_files import compute_cf
from control_variables.delete_files import compute_df
from control_variables.modified_files import compute_mf
from metric.build_correction_interval import compute_bci
from metric.builds_number import compute_bn
from metric.ci_latency import CiLatency
from metric.ci_result import compute_cr
from metric.closure_time import ClosureTime
from metric.commits_number import compute_cn
from metric.effective_comments import EffectiveComments
from metric.first_response_time import FirstResponseTime
from metric.general_comments import GeneralComments
from metric.jobs_number import compute_jn
from metric.mention_number import compute_mn
from metric.merge_time import MergeTime
from metric.number_participants import NumberParticipants
from metric.review_code_time import ReviewCodeTime
from metric.review_comments import ReviewComments
from metric.source_code_change_number import compute_sccn
from metric.test_code_change_number import compute_tccn

gl = gitlab.Gitlab.from_config('global', ['.python-gitlab.cfg'])
project_ids = list(os.environ['PROJECTS'].split(","))

cl = CiLatency(gl)
ct = ClosureTime(gl)
ec = EffectiveComments(gl)
gc = GeneralComments(gl)
mt = MergeTime(gl)
np = NumberParticipants(gl)
rtc = ReviewCodeTime(gl)
rc = ReviewComments(gl)
tfr = FirstResponseTime(gl)

if __name__ == '__main__':
    for project_id in project_ids:
        project = gl.projects.get(project_id)
        merge_requests = project.mergerequests.list(all=True)

        compute_bci(merge_requests)
        compute_bn(merge_requests)
        compute_cr(merge_requests)
        compute_cn(merge_requests)
        compute_jn(project, merge_requests)
        compute_mn(merge_requests)
        compute_sccn(merge_requests)
        compute_tccn(merge_requests)

        compute_af(merge_requests)
        compute_df(merge_requests)
        compute_cf(merge_requests)
        compute_mf(merge_requests)
