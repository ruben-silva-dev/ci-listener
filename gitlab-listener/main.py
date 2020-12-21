import gitlab
import os
from metric.build_correction_interval import BuildCorrectionInterval

gl = gitlab.Gitlab.from_config('global', ['.python-gitlab.cfg'])
project_ids = list(os.environ['PROJECTS'].split(","))

bci = BuildCorrectionInterval(gl)

if __name__ == '__main__':
    for project_id in project_ids:
        project = gl.projects.get(project_id)

        bci.compute(project)
