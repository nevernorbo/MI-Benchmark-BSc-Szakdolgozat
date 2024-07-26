import os
import importlib.util
import time
import csv
import psb2
import math

def load_function_from_file(filepath, function_name):
    """
    Loads a function from a given python file.

    Args:
        filepath (str): Path to the python file containing the function.
        function_name (str): Name of the function to load.

    Returns:
        function: The loaded function from the specified file.
    """
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


def is_approximately_equal(a, b, rel_tol=1e-9):
    """
    Compares two numbers or lists of numbers and determines if they are approximately equal (with a relative tolerance for floats).

    Args:
        a, b (float or list of floats): Numbers to compare.
        rel_tol (float): Relative tolerance for comparison, defaults to 1e-9.

    Returns:
        bool: True if numbers are approximately equal within the given tolerance, otherwise False.
    """
    if isinstance(*a, float) and isinstance(*b, float):
        return math.isclose(*a, *b, rel_tol=rel_tol)
    else:
        return a == b


def get_directories_in_folder(folder):
    """
    Retrieves a list of directory paths inside a given folder.

    Args:
        folder (str): Path to the folder from which to list directories.

    Returns:
        list: A list of paths to directories within the given folder.
    """
    return [os.path.join(folder, d) for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


def benchmark_function(function, data, data_type, writer):
    """
    Benchmarks a function by executing it with the psb2 test suite data and logs the results in a CSV format.

    Args:
        function (function): The function to benchmark.
        data (list of tuples): List of tuples, each containing inputs and the expected output.
        data_type (str): Type of data being processed ('train' or 'test').
        writer (csv.writer): CSV writer object to log the results.
    """
    for inputs, expected_output in data:
        start_time = time.perf_counter_ns()

        try:
            result = function(*inputs)
        except:
            result = None
            
        execution_time = time.perf_counter_ns() - start_time

        is_correct = is_approximately_equal([result], expected_output)
        writer.writerow([data_type, inputs, expected_output, [result], is_correct, round(execution_time, 6)])


def run_model_benchmarks(model_dir):
    """
    Runs benchmarks for all problems in a specified model directory and records the results.

    Args:
        model_dir (str): Directory path for a specific model where benchmarks are to be run.
    """
    tests_directory = os.path.join(model_dir, 'python/tests')
    
    # Results directory in which to store the results
    results_directory = os.path.join(model_dir, 'python/results_edge')
    os.makedirs(results_directory, exist_ok=True)

    for problem in psb2.PROBLEMS:
        function_path = os.path.join(tests_directory, problem + '.py')
        function_name = problem.replace('-', '_')
        function = load_function_from_file(function_path, function_name)

        results_path = os.path.join(results_directory, problem + '_results.csv')
        
        with open(results_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Dataset type', 'Input', 'Expected Output', 'Function Result', 'Is Correct', 'Execution Time (ns)'])

            (train_data, test_data) = psb2.fetch_examples('./datasets', problem, 200, 2000, format="lists")
            
            benchmark_function(function, train_data, "train", csv_writer)
            benchmark_function(function, test_data, "test", csv_writer)


def main():
    """
    Main function to run benchmarks on all models found in the models directory.
    """
    for model_directory in get_directories_in_folder('./models'):
        run_model_benchmarks(model_directory)


if __name__ == '__main__':
    main()
