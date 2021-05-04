import os

import gitlab

from metric.add_files import compute_af
from metric.build_correction_interval import compute_bci
from metric.builds_number import compute_bn
from metric.changing_files import compute_cf
from metric.ci_latency import compute_cl
from metric.ci_result import compute_cr
from metric.closure_time import compute_clt
from metric.comment_time import compute_cmt
from metric.comments import compute_comments
from metric.delete_files import compute_df
from metric.first_response_time import compute_frt
from metric.jobs_number import compute_jn
from metric.mention_number import compute_mn
from metric.modified_files import compute_mf
from metric.participants_number import compute_pn
from metric.review_time import compute_rt
from metric.reviews_number import compute_rn
from metric.source_code_changes_number import compute_sccn
from metric.test_code_changes_number import compute_tccn
from report.csv_report import export_individual_csv, export_general_csv

gl = gitlab.Gitlab.from_config('global', ['.python-gitlab.cfg'])
project_ids = list(os.environ['PROJECTS'].split(","))

if __name__ == '__main__':
    projects = []

    for project_id in project_ids:
        project = {
            'id': project_id,
            'merge_requests': []
        }

        gl_project = gl.projects.get(project_id)

        for gl_merge_request in gl_project.mergerequests.list(all=True):
            gl_pipelines = gl_merge_request.pipelines()

            if gl_merge_request.state != 'opened' and len(gl_pipelines) > 0:
                merge_request = {
                    'id': gl_merge_request.id,
                    'status': gl_merge_request.state
                }

                gl_changes = gl_merge_request.changes()
                gl_notes = gl_merge_request.notes.list()
                gl_commits = gl_merge_request.commits()

                merge_request['added_files'] = compute_af(gl_changes)
                merge_request['build_correction_intervals'] = compute_bci(gl_pipelines)
                merge_request.update(compute_bn(gl_pipelines))
                merge_request['total_changes'] = compute_cf(gl_changes)
                merge_request['ci_latency'] = compute_cl(gl_merge_request, gl_pipelines)
                merge_request['ci_result'] = compute_cr(gl_pipelines)
                merge_request['closure_time'] = compute_clt(gl_merge_request)
                merge_request['comment_time'] = compute_cmt(gl_merge_request, gl_notes)
                merge_request.update(compute_comments(gl_notes))
                merge_request['deleted_files'] = compute_df(gl_changes)
                merge_request['first_response_time'] = compute_frt(gl_merge_request, gl_notes)
                merge_request.update(compute_jn(gl_project, gl_pipelines))
                merge_request['mention_number'] = compute_mn(gl_notes)
                merge_request['modified_files'] = compute_mf(gl_changes)
                merge_request['participants_number'] = compute_pn(gl_merge_request)
                merge_request['review_time'] = compute_rt(gl_merge_request)
                merge_request['reviews_number'] = compute_rn(gl_commits)
                merge_request.update(compute_sccn(gl_changes))
                merge_request.update(compute_tccn(gl_changes))

                project['merge_requests'].append(merge_request)

        projects.append(project)

    export_individual_csv(projects)
    export_general_csv(projects)
