# coding: utf-8



import tkinter as tk
from tkinter import messagebox
import subprocess

# List of packages
packages = sorted(['beautifulsoup4', 'lxml', 'html5lib'])

def package_installer():
    def install_packages():
        selected_packages = [pkg for pkg, var in zip(packages, variables) if var.get()]
        if selected_packages:
            for package in selected_packages:
                subprocess.run(['pip', 'install', package])
            messagebox.showinfo("Installation", f"Installed: {', '.join(selected_packages)}")
            root.destroy()  # Close the window after installation
        else:
            messagebox.showwarning("No Selection", "No packages selected")

    def toggle_install_button(*args):
        selected = any(var.get() for var in variables)
        install_button.config(state=tk.NORMAL if selected else tk.DISABLED)

    # Create the main window
    root = tk.Tk()
    root.title("Package Installer")

    # Create a frame to hold the checkbuttons
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create a list to hold IntVar objects
    variables = [tk.IntVar() for _ in packages]

    # Create toggle buttons for each package
    for i, package in enumerate(packages):
        row, col = divmod(i, 5)
        checkbutton = tk.Checkbutton(frame, text=package, variable=variables[i], command=toggle_install_button)
        checkbutton.grid(row=row, column=col, sticky='w')

    # Create the install button and disable it initially
    install_button = tk.Button(root, text="Install", state=tk.DISABLED, command=install_packages)
    install_button.pack(pady=10)

    # Start the application
    root.mainloop()

# Call the function whenever needed
package_installer()

