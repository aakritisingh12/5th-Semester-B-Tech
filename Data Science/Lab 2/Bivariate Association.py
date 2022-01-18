import pandas as pd

house_pred_df = pd.read_csv("kc_house_data.csv")
print(house_pred_df.head())


def n_by_n_cov(df):
    def _covariance(x, y):
        x_mean, y_mean = sum(x) / len(x), sum(y) / len(y)
        return sum([(x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)]) / (len(x) - 1)

    columns = df.columns
    covs = dict()
    # column1 = 0
    for column1 in columns:
        covs[column1] = dict()
        for column2 in columns:
            covs[column1][column2] = _covariance(df[column1], df[column2])
    return covs


house_pred_covs = pd.DataFrame(n_by_n_cov(house_pred_df))
print(house_pred_covs)


def n_by_n_corr(df):
    def correlation(x, y):
        x_mean, y_mean = sum(x) / len(x), sum(y) / len(y)
        numerator_summation = sum([(x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y)])
        x_denominator_summation = sum([(x_i - x_mean) ** 2 for x_i in x])
        y_denominator_summation = sum([(y_i - y_mean) ** 2 for y_i in y])
        denominator = (x_denominator_summation * y_denominator_summation) ** 0.5
        return round(numerator_summation / denominator, 7)

    columns = df.columns
    corrs = dict()
    # column1 = 0
    for column1 in columns:
        corrs[column1] = dict()
        for column2 in columns:
            corrs[column1][column2] = correlation(df[column1], df[column2])
    return corrs


house_pred_corr = pd.DataFrame(n_by_n_corr(house_pred_df))
print(house_pred_corr)

customer_behavior_df = pd.read_csv("Customer_Behaviour.csv")
print(customer_behavior_df.head())


def point_biserial_corr(binary_feature, numerical_feature):
    def standard_dev(arr):
        mean = sum(arr) / len(arr)
        summation = sum([(a - mean) ** 2 for a in arr])
        return (summation / len(arr)) ** (1 / 2)

    binary_feature = binary_feature.astype('category').cat.codes  # encoding categorical feature
    if 1 < len(set(binary_feature)) > 2:
        return "BINARY FEATURE IS NOT OF BINARY CATEGORICAL"
    binary_group_split = dict()
    for binary, numerical in zip(binary_feature, numerical_feature):
        if binary not in binary_group_split.keys():
            binary_group_split[binary] = list()
        binary_group_split[binary].append(numerical)
    mean_for_cat_1 = sum(binary_group_split[1]) / len(binary_group_split[1])
    mean_for_cat_0 = sum(binary_group_split[0]) / len(binary_group_split[0])

    numerical_std_dev = standard_dev(numerical_feature)
    proportion_for_cat_1 = len(binary_group_split[1]) / len(binary_feature)
    proportion_for_cat_0 = len(binary_group_split[0]) / len(binary_feature)
    # formula
    category_split_over_deviation = (mean_for_cat_1 - mean_for_cat_0) / numerical_std_dev
    categorical_proportion = (proportion_for_cat_1 * proportion_for_cat_0) ** (1 / 2)
    return category_split_over_deviation * categorical_proportion


point_biserial_corr = point_biserial_corr(customer_behavior_df['Gender'], customer_behavior_df['Salary'])
print("Point Biserial Correlation:", point_biserial_corr)
