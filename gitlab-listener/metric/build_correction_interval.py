class BuildCorrectionInterval:
    def __init__(self, gitlab):
        self.gitlab = gitlab

    def compute(self, project_id, start_date, end_date):
        print("Build Correction Interval")