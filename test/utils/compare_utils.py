class DataCompareDBUtils:
    @staticmethod
    def compare_dataframes(df1, df2):
        """
        Compare two pandas dataframes and return True if they are equal, False otherwise.

        :param df1: First dataframe to compare.
        :param df2: Second dataframe to compare.
        :return: True if the dataframes are equal, False otherwise.
        """
        try:
            # Check if the dataframes are equal (element-wise)
            result = df1.equals(df2)
            return result
        except Exception as e:
            print(f"Error while comparing dataframes: {str(e)}")
            return False

    import pandas as pd

    @staticmethod
    def compare_query_results(result_df1, result_df2):
        # Sort both DataFrames to ensure consistent order for comparison
        result_df1 = result_df1.sort_values(by=result_df1.columns.tolist()).reset_index(drop=True)
        result_df2 = result_df2.sort_values(by=result_df2.columns.tolist()).reset_index(drop=True)
        print(result_df1)
        print(result_df2)

        # Check if the DataFrames are equal
        if result_df1.equals(result_df2):
            return "The DataFrames are identical."
        else:
            return "The DataFrames are not identical."

        # # Find rows that are in result_df1 but not in result_df2
        # added_rows = result_df1[~result_df1.isin(result_df2).all(1)]
        #
        # # Find rows that are in result_df2 but not in result_df1
        # removed_rows = result_df2[~result_df2.isin(result_df1).all(1)]
        #
        # # Find rows with different values between result_df1 and result_df2
        # different_rows = result_df1[result_df1.isin(result_df2).all(1) & ~result_df1.equals(result_df2)]
        #
        # return {
        #     "added_rows": added_rows,
        #     "removed_rows": removed_rows,
        #     "different_rows": different_rows
        # }
