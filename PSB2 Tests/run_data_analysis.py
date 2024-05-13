import pandas as pd
import os


def convert_to_utf8_and_read(filepath, columns):
    """
    Try reading a CSV file with UTF-8 encoding, convert to UTF-8 if there is an error.

    Args:
        filepath (str): Path to the CSV file.
        columns (list of str): Columns to load from the CSV.

    Returns:
        DataFrame: Loaded DataFrame with the specified columns.
    """
    try:
        # Try to read the file with UTF-8 encoding
        return pd.read_csv(filepath, usecols=columns, encoding='utf-8')
    except UnicodeDecodeError:
        # If there's an encoding error, read with a fallback encoding and convert to utf-8
        encoding = 'latin1'  # fallback to latin1
        df = pd.read_csv(filepath, encoding=encoding)
        # Create a temporary filepath, write to it, then read from it
        temp_filepath = filepath + '_temp.csv'
        df.to_csv(temp_filepath, index=False, encoding='utf-8')
        
        print(f"Encoding error converting to UTF-8. Created temporary file: {temp_filepath}")
        
        return pd.read_csv(temp_filepath, usecols=columns, encoding='utf-8')


def load_and_merge_data(result_dir, results_folders, required_columns):
    """
    Load and merge CSV data from multiple result folders based on problem name.

    Args:
        result_dir (str): The base directory containing results folders.
        results_folders (list of str): Folder names containing the CSV files.
        required_columns (list of str): Columns to load from the CSV.

    Returns:
        dict: A dictionary where the keys are the problem names and the values are merged DataFrames.
    """
    problem_data = {}
    for folder in results_folders:
        folder_path = os.path.join(result_dir, folder)
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                filepath = os.path.join(folder_path, filename)

                try:
                    df = convert_to_utf8_and_read(filepath, required_columns)
                except Exception as e:
                    print(f"Failed to process {filename}: {e}")
                    continue

                problem_name = filename.split('_')[0]
                if problem_name not in problem_data:
                    problem_data[problem_name] = []
                problem_data[problem_name].append(df)

    # Merge the data by problem name
    for problem in problem_data:
        problem_data[problem] = pd.concat(problem_data[problem], ignore_index=True)

    return problem_data


def compute_statistics(problem_data, model_name):
    """
    Compute statistics for each problem.

    Args:
        problem_data (dict): A dictionary with problem names as keys and merged DataFrames as values.

    Returns:
        DataFrame: A DataFrame containing the statistics for each problem.
    """
    statistics = []
    for problem_name, df in problem_data.items():
        train_data = df[df['Dataset type'] == 'train']
        test_data = df[df['Dataset type'] == 'test']
        correct_train = train_data[train_data['Is Correct'] == True]
        correct_test = test_data[test_data['Is Correct'] == True]
        runtime_errors = df[df['Function Result'] == "[None]"]

        stat_dict = {
            'Model': model_name,
            'Problem': problem_name,
            'All cases': len(train_data) + len(test_data),
            'Correct cases': len(correct_train) + len(correct_test),
            'All edge cases': len(train_data),
            'Correct edge cases': len(correct_train),
            'Correct edge case percentage': 100 * len(correct_train) / len(train_data) if len(train_data) > 0 else 0,
            'All random cases': len(test_data),
            'Correct random cases': len(correct_test),
            'Correct random case percentage': 100 * len(correct_test) / len(test_data) if len(test_data) > 0 else 0,
            'Runtime errors': len(runtime_errors),
            'Average execution time': df['Execution Time (ns)'].mean(),
            'Median execution time': df['Execution Time (ns)'].median(),
            'Max execution time': df['Execution Time (ns)'].max(),
            'Min execution time': df['Execution Time (ns)'].min(),
            'Notes': ''
        }
        statistics.append(stat_dict)

    return pd.DataFrame(statistics)


def save_statistics(statistics_df, output_file):
    """
    Save the statistics DataFrame to a CSV file within a designated 'statistics' folder.

    Args:
        statistics_df (DataFrame): DataFrame containing the statistics.
        output_file (str): Filename for the output CSV.
    """
    statistics_path = "statistics"

    if not os.path.exists(statistics_path):
        os.makedirs(statistics_path)

    full_path = os.path.join(statistics_path, output_file)
    statistics_df.to_csv(full_path, index=False)
    print(f"Statistics saved to {full_path}")



def get_directories_in_folder(folder):
    return [os.path.join(folder, d) for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


def cleanup_temp_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('_temp.csv'):
            print("Removed temporary csv file: ", os.path.join(directory, filename))
            os.remove(os.path.join(directory, filename))


def main():
    """
    Main function to run data analysis on all the results inside a model directory.
    """
    results_folders = ['results_1', 'results_2', 'results_3', 'results_4', 'results_5', 'results_edge']
    required_columns = ['Dataset type', 'Is Correct', 'Function Result', 'Execution Time (ns)']

    for model_directory in get_directories_in_folder('./models'):
        results_path = os.path.join(model_directory, 'python')
        # Load and merge the data
        problem_data = load_and_merge_data(results_path, results_folders, required_columns)

        # Compute the statistics
        model_name = model_directory.split(os.sep)[1]
        stats_df = compute_statistics(problem_data, model_name)
        print("Computed statistics for ", model_name)

        # Save the statistics to a CSV file
        save_statistics(stats_df, f'{model_directory.split(os.sep)[1]}_statistics.csv')

        # Remove the temporary files that were created in case there were encoding errors
        for result_folder in results_folders:
            result_folder_path = os.path.join(results_path, result_folder)
            cleanup_temp_files(result_folder_path)


if __name__ == '__main__':
    main()
