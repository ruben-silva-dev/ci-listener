import gitlab
import os
from metric.build_correction_interval import BuildCorrectionInterval
from metric.ci_latency import CiLatency
from metric.ci_result import CiResult
from metric.closure_time import ClosureTime
from metric.effective_comments import EffectiveComments
from metric.first_response_time import FirstResponseTime
from metric.general_comments import GeneralComments
from metric.merge_time import MergeTime
from metric.number_builds import NumberBuilds
from metric.number_code_test_changed import NumberCodeTestChanged
from metric.number_commits import NumberCommits
from metric.number_jobs import NumberJobs
from metric.number_mentions import NumberMentions
from metric.number_participants import NumberParticipants
from metric.review_code_time import ReviewCodeTime
from metric.review_comments import ReviewComments
from metric.src_churn import SrcChurn
from metric.total_comments import TotalComments

gl = gitlab.Gitlab(os.environ['GITLAB_URI'], private_token=os.environ['GITLAB_PRIVATE_TOKEN'])
bci = BuildCorrectionInterval(gl)
cl = CiLatency(gl)
cr = CiResult(gl)
ct = ClosureTime(gl)
ec = EffectiveComments(gl)
gc = GeneralComments(gl)
mt = MergeTime(gl)
nb = NumberBuilds(gl)
nct = NumberCodeTestChanged(gl)
nc = NumberCommits(gl)
nj = NumberJobs(gl)
nm = NumberMentions(gl)
np = NumberParticipants(gl)
rtc = ReviewCodeTime(gl)
rc = ReviewComments(gl)
sc = SrcChurn(gl)
tfr = FirstResponseTime(gl)
tc = TotalComments(gl)

if __name__ == '__main__':
    print('Gitlab Listener')