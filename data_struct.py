import pickle

def save_data(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_data(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

def main():
    # Asking user for a list of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    int_list = [int(item) for item in user_input.split()]


    # Filename to save data
    filename = "data.pkl"

    # Save data to file
    save_data(int_list, filename)

    # Load data from file
    loaded_list = load_data(filename)

    # Display the loaded data
    print("Data loaded from file:", loaded_list)

if __name__ == "__main__":
    main()
