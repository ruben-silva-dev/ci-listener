import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

cr_metrics = ["added_files", "total_changes", "deleted_files", "modified_files", "closure_time", "comment_time",
              "reviews_number", "first_response_time", "mention_number", "review_time", "participants_number",
              "source_code_added_lines", "source_code_removed_lines", "test_code_added_lines",
              "test_code_removed_lines", "total_comments", "general_comments", "review_comments", "effective_comments"]
ci_metrics = ["ci_result", "build_correction_intervals", "total_builds", "success_builds", "failed_builds",
              "ci_latency", "total_jobs", "success_jobs", "failed_jobs"]


def generate_cr_boxplot(dataset):
    plt.subplots_adjust(bottom=.45)

    dataset[cr_metrics].boxplot(rot=80)

    plt.savefig("boxplot_cr.png")


def generate_ci_boxplot(dataset):
    plt.subplots_adjust(bottom=.45)

    dataset[ci_metrics].boxplot(rot=80)

    plt.savefig("boxplot_ci.png")


def generate_histogram(dataset):
    dataset[cr_metrics + ci_metrics].hist(figsize=(21, 28), layout=(7, 4))
    plt.subplots_adjust(bottom=.1)
    plt.savefig("histogram.png")


def generate_correlation(dataset):
    plt.figure(figsize=(28, 30))
    plt.subplots_adjust(left=.19, bottom=.16)

    sns.set(font_scale=2.5)

    sns.heatmap(dataset.corr(method="spearman").loc[cr_metrics, ci_metrics], annot=True, cbar=False, cmap=plt.cm.PuBu)

    plt.savefig("correlation.png")


def calculate_statistical_significance(dataset):
    corr, pvalue = scipy.stats.spearmanr(dataset[ci_metrics + cr_metrics])
    pd.DataFrame(pvalue).to_csv("p_value.csv", header=None, index=None)


if __name__ == '__main__':
    pd_data = pd.read_csv("INPUT_FILE")

    scaler = MinMaxScaler(feature_range=(-1, 1))
    pd_data[cr_metrics + ci_metrics] = scaler.fit_transform(
        pd_data[cr_metrics + ci_metrics])

    # call_method()
