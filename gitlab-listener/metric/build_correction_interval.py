class BuildCorrectionInterval:
    def __init__(self, gitlab):
        self.gitlab = gitlab

    def compute(self, project, start_date, end_date):
        print("Build Correction Interval")