import subprocess
import os
import platform

def execute_script(script_name):
    """
    Function to execute a script (sh or bat) based on the system's OS.
    """
    try:
        if script_name.endswith('.bat'):
            # Run Windows batch file
            print(f"Executing {script_name} on Windows...")
            subprocess.run(script_name, shell=True, check=True)
        elif script_name.endswith('.sh'):
            # Run Bash script (Linux/Mac)
            print(f"Executing {script_name} on Linux/Mac...")
            subprocess.run(["bash", script_name], check=True)
        else:
            print(f"Unsupported script type: {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {script_name}: {e}")

def execute_main():
    """
    Function to execute the main.py script.
    """
    if not os.path.exists("main.py"):
        print("Error: main.py not found in the current directory.")
        return
    try:
        print("Running main.py...")
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running main.py: {e}")

def main():
    """
    Main function that allows users to choose Setup or Execute main.py.
    """
    while True:
        print("=========================================")
        print("    Auto PenTest Tool Setup Launcher")
        print("=========================================")
        print("1. Setup Environment")
        print("2. Execute PenTest Tool")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # OS Selection and Setup
            print("\nChoose your operating system:")
            print("1. Windows")
            print("2. Linux")
            print("3. macOS")
            os_choice = input("Enter your choice (1/2/3): ")

            if os_choice == '1':
                if platform.system() != "Windows":
                    print("Warning: You selected Windows, but you are not on a Windows OS!")
                script_name = "autorun.bat"
            elif os_choice == '2':
                if platform.system() != "Linux":
                    print("Warning: You selected Linux, but you are not on a Linux OS!")
                script_name = "setup.sh"
            elif os_choice == '3':
                if platform.system() != "Darwin":
                    print("Warning: You selected macOS, but you are not on a macOS system!")
                script_name = "Macsetup.sh"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

            # Check if the script file exists
            if not os.path.exists(script_name):
                print(f"Error: {script_name} not found in the current directory.")
            else:
                execute_script(script_name)
        
        elif choice == '2':
            # Execute main.py
            execute_main()
        
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()