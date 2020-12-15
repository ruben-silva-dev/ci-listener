import gitlab
import os
from metric.build_correction_interval import BuildCorrectionInterval

gl = gitlab.Gitlab(os.environ['GITLAB_URI'], private_token=os.environ['GITLAB_PRIVATE_TOKEN'])
bci = BuildCorrectionInterval(gl)

if __name__ == '__main__':
    print('Gitlab Listener')