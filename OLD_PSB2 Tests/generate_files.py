import os
import json
import psb2

def load_json(json_file):
    """
    Loads the config.json file and returns the models and programming languages
    
    Args:
        json_file (str): Path to the JSON file.

    Returns:
        tuple: Returns two lists containing the models and programming languages.
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data["models"], data["programming_languages"]


def get_language_names(languages):
    """
    Extracts programming language names from a dictionary.

    Args:
        languages (dict): Dictionary with programming languages as keys.

    Returns:
        list: List of programming language names.
    """
    return list(languages.keys())


def create_model_directories(models):
    """
    Creates directories for each model specified in the models list.

    Args:
        models (list): A list of model names for which directories will be created.

    Returns:
        list: A list of paths to the created model directories.
    """
    if not os.path.exists("./models"):
            os.makedirs("./models")
    else:
        print(f"The models directory already exists")
    
    model_paths = []

    for model in models:
        model_path = os.path.join(os.getcwd(), "models", model)
        model_paths.append(model_path)
        if not os.path.exists(model_path):
            os.makedirs(model_path)
        else:
            print(f"This model directory already exists: {model_path}")

    return model_paths


def create_language_directories(model_paths, languages):
    """
    Creates directories for each programming language under each model directory.

    Args:
        model_paths (list): Paths to model directories.
        languages (dict): Dictionary containing programming language details.

    Returns:
        list: A list of paths to the created programming language directories.
    """
    language_paths = []
    language_names = get_language_names(languages)

    for model_path in model_paths:
        for language_name in language_names:
            language_path = os.path.join(model_path, language_name)
            language_paths.append(language_path)
            if not os.path.exists(language_path):
                os.makedirs(language_path)
                create_tests_and_results_directories(
                    language_path, languages, language_name)
            else:
                print(f"This directory already exists: {language_path}")

    return language_paths


def create_tests_and_results_directories(language_path, languages, language_name):
    """
    Creates "tests" and "results" directories for a specific programming language.

    Args:
        language_path (str): Path to the programming language directory.
        languages (dict): Dictionary of languages containing file extensions.
        language_name (str): Name of the programming language.
    """
    # create two directories: test, results
    tests_path = os.path.join(language_path, "tests")
    if not os.path.exists(tests_path):
        os.makedirs(tests_path)
        create_tests(tests_path, languages, language_name)
    else:
        print(f"This directory already exists: {tests_path}")

    results_path = os.path.join(language_path, "results")
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    else:
        print(f"This directory already exists: {results_path}")


def create_tests(tests_path, languages, language_name):
    """
    Populates the "tests" directory with empty test files for a programming language.

    Args:
        tests_path (str): Path to the directory where test files will be created.
        languages (dict): Dictionary containing programming language details.
        language_name (str): Name of the programming language to create test files for.
    """
    extension = languages[language_name]["extension"]

    for problem in psb2.PROBLEMS:
        problem_file = f"{problem}.{extension}"
        problem_path = os.path.join(tests_path, problem_file)

        if not os.path.exists(problem_path):
            with open(os.path.join(tests_path, problem_file), 'w') as f:
                pass
        else:
            print(f"This file already exists: {problem_path}")


def main():
    """
    Main function to load configuration and create necessary directories and files.
    """

    models, languages = load_json("config.json")

    model_paths = create_model_directories(models)
    create_language_directories(model_paths, languages)


if __name__ == "__main__":
    main()
