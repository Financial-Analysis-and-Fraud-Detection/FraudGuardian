import pandas as pd

# Load data from the NSFAS and University CSV files
nsfas_data = pd.read_csv('C:/Users/Tau/Desktop/Compare_Data_AI/Nsfas_Data/Nsfas_data.csv')
university_data = pd.read_csv('C:/Users/Tau/Desktop/Compare_Data_AI/University_Data/University_Data.csv')

# Define a function to display data and perform operations
def display_and_operate_data(data, data_name):
    while True:
        print(f"\nOptions for {data_name} data:")
        print("1. View data")
        print("2. Edit data")
        print("3. Delete data by line number")
        print("4. Back to main options")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(data)
        elif choice == '2':
            print("Go edit manually on the CSV File")
            pass
        elif choice == '3':
            try:
                line_number = int(input(f"Enter the line number to delete (1 to {len(data)}): ")) - 1
                if 0 <= line_number < len(data):
                    data = data.drop(index=line_number)
                    print("Data deleted successfully.")
                else:
                    print("Invalid line number.")
            except ValueError:
                print("Invalid input. Please enter a valid line number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Define a function to compare data and perform AI actions
def compare_and_report(nsfas_data, university_data):
    common_applicants = pd.merge(university_data, nsfas_data, on=['Full Name', 'Identity Number'], how='inner')
    uncommon_applicants = pd.concat([university_data, nsfas_data]).drop_duplicates(keep=False)
    
    common_applicants.to_csv('common_applicants.csv', index=False)
    uncommon_applicants.to_csv('uncommon_applicants.csv', index=False)
    
    if len(university_data) > len(nsfas_data):
        print("\nFRAUD DETECTED !!!!!\nUncommon applicants list generated")
    else:
        print("\nNO FRAUD DETECTED\nUncommon applicants list generated")
    
    combined_data = pd.concat([university_data, nsfas_data])
    summary_data = pd.DataFrame({
        'Total Records': [len(combined_data)],
        'Common Data': [len(common_applicants)],
        'Unique Data': [len(uncommon_applicants)],
    })
    summary_data.to_csv('summary_data.csv', index=False)

# Main AI interface
while True:
    print("\nAI Options:")
    print("1. Manage NSFAS data")
    print("2. Manage University data")
    print("3. Compare data and generate report")
    print("4. Exit")

    ai_choice = input("Enter your choice: ")

    if ai_choice == '1':
        display_and_operate_data(nsfas_data, "NSFAS")
    elif ai_choice == '2':
        display_and_operate_data(university_data, "University")
    elif ai_choice == '3':
        compare_and_report(nsfas_data, university_data)
    elif ai_choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Goodbye!")
