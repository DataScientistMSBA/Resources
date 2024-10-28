# coding: utf-8



import tkinter as tk
from tkinter import messagebox
import subprocess

# List of packages with installation names, categories, descriptions, and display names
packages = [
    ('beautifulsoup4', 'Web Scraping', 'BeautifulSoup: Parses HTML and XML', 'BeautifulSoup'),
    ('lxml', 'Web Scraping', 'lxml: Processes XML and HTML', 'lxml'),
    ('html5lib', 'Web Scraping', 'html5lib: Parses HTML', 'html5lib'),
    ('scrapy', 'Web Scraping', 'Scrapy: Web crawling framework', 'Scrapy'),
    ('selenium', 'Web Automation', 'Selenium: Web browser automation tool', 'Selenium'),
    ('tqdm', 'Utilities', 'Tqdm: Progress bar library', 'tqdm'),
    ('PyPDF2', 'File Processing', 'PyPDF2: PDF manipulation and extraction', 'PyPDF2'),
    ('boto3', 'Cloud Services', 'Boto3: AWS SDK for Python', 'Boto3'),
    ('awswrangler', 'Cloud Services', 'AWS Data Wrangler: Python library for AWS data', 'AWS Wrangler'),
    ('azure-servicebus', 'Cloud Services', 'Azure Service Bus: Azure messaging service', 'Azure Service Bus'),
    ('simple-salesforce', 'Cloud Services', 'Simple Salesforce: Python wrapper for Salesforce API', 'Simple Salesforce'),
    ('pandas', 'Data Manipulation', 'Pandas: Data manipulation and analysis tool', 'Pandas'),
    ('numpy', 'Data Manipulation', 'NumPy: Fundamental package for numerical computation', 'NumPy'),
    ('pyarrow', 'Data Manipulation', 'PyArrow: Columnar data and in-memory analytics', 'PyArrow'),
    ('pympler', 'Data Manipulation', 'Pympler: Memory profiling for Python applications', 'Pympler'),
    ('fuzzywuzzy', 'Data Matching', 'FuzzyWuzzy: String matching and comparison', 'FuzzyWuzzy'),
    ('recordlinkage', 'Data Matching', 'Record Linkage Toolkit: Link and match records', 'Record Linkage Toolkit'),
    ('strsimpy', 'Data Matching', 'String Similarity Algorithms: Similarity metrics', 'Strsimpy'),
    ('textdistance', 'Data Matching', 'TextDistance: Compute distances between texts', 'TextDistance'),
    ('chart-studio', 'Data Visualization', 'Chart Studio: Create interactive charts', 'Chart Studio'),
    ('matplotlib', 'Data Visualization', 'Matplotlib: Plotting library', 'Matplotlib'),
    ('seaborn', 'Data Visualization', 'Seaborn: Statistical data visualization', 'Seaborn'),
    ('plotly', 'Data Visualization', 'Plotly: Interactive graphing library', 'Plotly'),
    ('bokeh', 'Data Visualization', 'Bokeh: Interactive visualization library', 'Bokeh'),
    ('dash', 'Data Visualization', 'Dash: Interactive web applications for visualization', 'Dash'),
    ('IPython', 'Development', 'IPython: Interactive Python shell', 'IPython'),
    ('virtualenv', 'Development', 'Virtualenv: Tool to create isolated Python environments', 'Virtualenv'),
    ('python3-devel', 'Development', 'Python3 Devel: Essential libraries for development', 'Python3 Devel'),
    ('pip', 'Development', 'Pip: Package installer for Python', 'Pip'),
    ('setuptools', 'Development', 'Setuptools: Library for Python packaging', 'Setuptools'),
    ('pytest', 'Development', 'Pytest: Testing framework for Python', 'pytest'),
    ('s3fs', 'File Systems', 'S3FS: File system for Amazon S3', 'S3FS'),
    ('fsspec', 'File Systems', 'FSSpec: Filesystem specification for data handling', 'FSSpec'),
    ('paramiko', 'File Systems', 'Paramiko: SSH2 protocol for remote server management', 'Paramiko'),
    ('pysftp', 'File Systems', 'PySFTP: Simple SFTP interface', 'PySFTP'),
    ('openpyxl', 'File Handling', 'Openpyxl: Read/write Excel files', 'Openpyxl'),
    ('pillow', 'Image Processing', 'Pillow: Image processing library', 'Pillow'),
    ('opencv-python', 'Image Processing', 'OpenCV: Computer vision and machine learning library', 'OpenCV'),
    ('country_converter', 'Localization', 'Country Converter: ISO 3166 data conversions', 'Country Converter'),
    ('phonenumbers', 'Localization', 'Phonenumbers: Parse, format, and validate phone numbers', 'Phonenumbers'),
    ('uszipcode', 'Localization', 'US Zipcode: Get U.S. zipcode data', 'US Zipcode'),
    ('pyzipcode', 'Localization', 'Pyzipcode: Search U.S. zipcode database', 'Pyzipcode'),
    ('us', 'Localization', 'US: US state and territory metadata', 'US'),
    ('sqlalchemy', 'Database', 'SQLAlchemy: SQL toolkit and ORM library', 'SQLAlchemy'),
    ('pymongo', 'Database', 'PyMongo: MongoDB driver', 'PyMongo'),
    ('trino', 'Database', 'Trino: Distributed SQL query engine', 'Trino'),
    ('pyathena', 'Database', 'PyAthena: Athena client for AWS', 'PyAthena'),
    ('presto-python-client', 'Database', 'Presto: Python client for Presto', 'Presto Client'),
    ('requests', 'Networking', 'Requests: Simplifies making HTTP requests', 'Requests'),
    ('socket', 'Networking', 'Socket: Provides low-level networking interfaces', 'Socket'),
    ('websocket-client', 'Networking', 'WebSocket Client: WebSocket API for Python', 'WebSocket Client'),
    ('requests_oauthlib', 'Networking', 'Requests-OAuthlib: OAuth for HTTP requests', 'Requests OAuthlib'),
    ('scipy', 'Data Science', 'SciPy: Scientific and technical computing', 'SciPy'),
    ('statsmodels', 'Data Science', 'Statsmodels: Statistical models', 'Statsmodels'),
    ('xgboost', 'Machine Learning', 'XGBoost: Gradient boosting library', 'XGBoost'),
    ('lightgbm', 'Machine Learning', 'LightGBM: Fast gradient boosting library', 'LightGBM'),
    ('scikit-learn', 'Machine Learning', 'Scikit-learn: Machine learning library', 'Scikit-learn'),
    ('tensorflow', 'Machine Learning', 'TensorFlow: Open-source platform for machine learning', 'TensorFlow'),
    ('keras', 'Machine Learning', 'Keras: High-level neural networks API', 'Keras'),
    ('shap', 'Machine Learning', 'SHAP: Interpret ML model predictions', 'SHAP'),
    ('pytorch', 'Machine Learning', 'PyTorch: Deep learning framework', 'PyTorch')
]

# Sort packages alphabetically by category and then name
packages.sort(key=lambda x: (x[1], x[0]))

def PackageInstaller():
    max_description_length = max(len(f"{desc}") for _, _, desc, _ in packages)
    width_in_pixels = max_description_length * 9 * 2 + 300  # Ensures sufficient width for all content

    def install_packages():
        selected_packages = [(pkg[0], pkg[3]) for pkg, var in zip(packages, package_vars) if var.get()]
        total_packages = len(selected_packages)
        failed_packages = []
        already_installed = []

        if not selected_packages:
            messagebox.showwarning("No Selection", "No packages selected")
            return

        progress_window = tk.Toplevel(root)
        progress_window.title("Installation Progress")
        progress_window.geometry("400x100")
        progress_window.configure(bg="#F3F4F6")
        progress_label = tk.Label(progress_window, text="", font=("Segoe UI", 10), bg="#F3F4F6")
        progress_label.pack(padx=10, pady=10)

        for i, (install_name, display_name) in enumerate(selected_packages, start=1):
            progress_label.config(text=f"({i}/{total_packages}) Installing {display_name}...")
            progress_window.update()

            try:
                result = subprocess.run(['pip', 'install', install_name], capture_output=True, text=True)
                if "Requirement already satisfied" in result.stdout:
                    already_installed.append(display_name)
                    progress_label.config(text=f"({i}/{total_packages}) {display_name} is already installed")
                else:
                    progress_label.config(text=f"({i}/{total_packages}) Installing {display_name}...")
            except subprocess.CalledProcessError:
                failed_packages.append(display_name)

            progress_window.update()

        progress_window.destroy()

        if failed_packages:
            messagebox.showerror(
                "Installation Complete",
                f"The following packages failed to install:\n" + "\n".join(failed_packages)
            )
        elif already_installed:
            messagebox.showinfo(
                "Installation Complete",
                f"All selected packages installed successfully!\n\n"
                f"The following packages were already installed:\n" + ", ".join(already_installed)
            )
        else:
            messagebox.showinfo("Installation Complete", "All selected packages installed successfully!")

        root.destroy()

    def toggle_install_button(*args):
        selected = any(var.get() for var in package_vars)
        install_button.config(state=tk.NORMAL if selected else tk.DISABLED)

    def toggle_all_packages():
        is_selected = select_all_var.get()
        for var in package_vars:
            var.set(is_selected)
        for cat_var in category_vars.values():
            cat_var.set(is_selected)
        toggle_install_button()

    def toggle_category(category):
        is_selected = category_vars[category].get()
        for idx, (_, cat, _, _) in enumerate(packages):
            if cat == category:
                package_vars[idx].set(is_selected)
        toggle_install_button()

    def on_mouse_scroll(event):
        if event.num == 5 or event.delta == -120:
            canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            canvas.yview_scroll(-1, "units")

    root = tk.Tk()
    root.title("Package Installer")
    root.geometry(f"{width_in_pixels}x600")
    root.configure(bg="#F3F4F6")

    font_style = ("Segoe UI", 10)
    header_font_style = ("Segoe UI", 11, "bold")

    header_frame = tk.Frame(root, bg="#F3F4F6")
    header_frame.pack(side="top", fill="x", pady=10, padx=10)

    select_all_var = tk.IntVar()
    select_all_checkbutton = tk.Checkbutton(
        header_frame, text="Select All", variable=select_all_var, command=toggle_all_packages,
        font=header_font_style, bg="#F3F4F6", activebackground="#F3F4F6"
    )
    install_button = tk.Button(
        header_frame, text="Install", state=tk.DISABLED, command=install_packages, font=header_font_style,
        bg="#0078D4", fg="white", activebackground="#005A9E", activeforeground="white", relief="flat"
    )
    install_button.pack(side="right")
    select_all_checkbutton.pack(side="right", padx=5)

    canvas = tk.Canvas(root, width=width_in_pixels, bg="#F3F4F6", bd=0, highlightthickness=0)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#F3F4F6")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.bind_all("<MouseWheel>", on_mouse_scroll)
    canvas.bind_all("<Button-4>", on_mouse_scroll)
    canvas.bind_all("<Button-5>", on_mouse_scroll)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    package_vars = [tk.IntVar() for _ in packages]
    category_vars = {}

    current_category = None
    row = 0
    column = 0

    for i, (install_name, category, description, display_name) in enumerate(packages):
        # New category handling
        if category != current_category:
            # Reset the row to start directly under the category name in the left column
            if column == 1:  # If we were in the right column, move to a new row
                row += 1
            column = 0  # Start each new category in the left column

            # Create the category title
            category_vars[category] = tk.IntVar()
            cat_checkbutton = tk.Checkbutton(
                scrollable_frame, text=category, variable=category_vars[category],
                font=("Segoe UI", 12, "bold"), bg="#F3F4F6", pady=5,
                command=lambda cat=category: toggle_category(cat)
            )
            cat_checkbutton.grid(row=row, column=0, columnspan=2, sticky='w', padx=10)
            current_category = category
            row += 1  # Move to the next row to start adding packages

        # Create package entry
        package_frame = tk.Frame(scrollable_frame, bg="#F3F4F6")
        package_frame.grid(row=row, column=column * 2, sticky='w', padx=30, pady=2)

        # Add checkbox first
        checkbutton = tk.Checkbutton(
            package_frame, variable=package_vars[i],
            command=toggle_install_button, bg="#F3F4F6", activebackground="#F3F4F6"
        )
        checkbutton.pack(side="left")

        # Bold package name
        package_name_label = tk.Label(
            package_frame, text=display_name + ":", font=("Segoe UI", 10, "bold"),
            bg="#F3F4F6"
        )
        package_name_label.pack(side="left")

        # Description in regular font
        package_description_label = tk.Label(
            package_frame, text=" " + description, font=("Segoe UI", 10),
            bg="#F3F4F6"
        )
        package_description_label.pack(side="left")

        # Alternate columns within each category
        if column == 0:
            column = 1  # Move to the right column
        else:
            column = 0  # Reset to left column and move to a new row
            row += 1

    root.mainloop()




# PackageInstaller()

