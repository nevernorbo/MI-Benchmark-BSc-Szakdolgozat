import psb2


def create_data():
    """
    Generate data for all problems in the PSB2 dataset if it doesn't exist.
    """
    for problem in psb2.PROBLEMS:
        (train_data, test_data) = psb2.fetch_examples("./listsdata", problem, 200, 2000, format="lists")
      
        
def main():
    create_data()


if __name__ == "__main__":
    main()