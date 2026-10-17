# example_module.py

def main_logic():
    print("This is the main logic of the module.")

print(f"__name__ in example_module.py is: {__name__}")

if __name__ == "__main__":
    # This code block will only run when example_module.py is executed directly
    print("example_module.py is being run directly.")
    main_logic()
else:
    # This code block will run when example_module.py is imported
    print("example_module.py is being imported.")