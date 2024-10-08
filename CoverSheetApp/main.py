import subprocess
import tkinter as tk
from tkinter import messagebox
import json
import shutil
import os

# Global variable to store user input
project_info = {}


# Function to handle form submission
def submit_form():
    global project_info
    project_info = {
        "[project-name]": project_name_entry.get(),
        "[bid-type]": bid_type_entry.get(),
        "[location]": location_entry.get(),
        "[contract-number]": contract_number_entry.get(),
        "[cwsrf-number]": cwsrf_number_entry.get()
    }

    # Save the project_info to a JSON file so it can be passed to cover-generator.py
    with open("project_info.json", "w") as f:
        json.dump(project_info, f)

    messagebox.showinfo("Information Submitted", "Project information has been submitted successfully.")
    root.destroy()  # Close the form window


# Function to delete the contents of a directory
def clear_directory(directory):
    """Delete all files in the given directory."""
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


# Function to check the 'pdfs' directory and ask the user if they want to delete existing files
def check_pdfs_directory():
    """Check if 'pdfs' directory has files, and ask user if they want to delete them."""
    if os.path.exists('pdfs') and os.listdir('pdfs'):  # If there are files in the 'pdfs' directory
        # Create a Tkinter window to ask the user whether to delete the contents
        answer = messagebox.askyesno("PDFs Directory Not Empty",
                                     "The 'pdfs' directory contains files. Would you like to delete them and proceed?")
        if answer:  # If the user says yes, delete the files
            clear_directory('pdfs')
            messagebox.showinfo("PDFs Directory", "The 'pdfs' directory has been cleared.")
        else:  # If the user says no, terminate the script
            messagebox.showinfo("Process Terminated",
                                "The process has been terminated. Please clear the 'pdfs' directory manually and try again.")
            exit()


# Function to run a script
def run_script(script_name):
    """Run the given script."""
    try:
        print(f"Running {script_name}...")
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")


if __name__ == "__main__":
    # Automatically clear the 'files' directory without asking
    clear_directory('files')

    # Check the 'pdfs' directory and ask the user if they want to clear it
    check_pdfs_directory()

    # Create the Tkinter form for project information input
    root = tk.Tk()
    root.title("Project Information Form")

    # Define labels and text entry fields for each input
    tk.Label(root, text="Project Name:").grid(row=0, column=0)
    project_name_entry = tk.Entry(root, width=40)
    project_name_entry.grid(row=0, column=1)

    tk.Label(root, text="Bid Type:").grid(row=1, column=0)
    bid_type_entry = tk.Entry(root, width=40)
    bid_type_entry.grid(row=1, column=1)

    tk.Label(root, text="Location:").grid(row=2, column=0)
    location_entry = tk.Entry(root, width=40)
    location_entry.grid(row=2, column=1)

    tk.Label(root, text="Contract Number:").grid(row=3, column=0)
    contract_number_entry = tk.Entry(root, width=40)
    contract_number_entry.grid(row=3, column=1)

    tk.Label(root, text="CWSRF Number:").grid(row=4, column=0)
    cwsrf_number_entry = tk.Entry(root, width=40)
    cwsrf_number_entry.grid(row=4, column=1)

    # Submit button to trigger the submission of form data
    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.grid(row=5, column=1)

    # Run the Tkinter main loop to collect user input
    root.mainloop()

    # After collecting inputs, proceed with running the other scripts
    # First, run the cover-generator script
    run_script("cover-generator.py")

    # Then, run the convert-to-pdf script
    run_script("convert-to-pdf.py")