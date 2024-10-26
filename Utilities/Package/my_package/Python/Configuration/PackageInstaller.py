# coding: utf-8



import tkinter as tk
from tkinter import messagebox
import subprocess

# List of packages with installation names, categories, descriptions, and display names
packages = [
    ('beautifulsoup4', 'Web Scraping', 'BeautifulSoup: Parses HTML and XML', 'BeautifulSoup'),
    ('lxml', 'Web Scraping', 'lxml: Processes XML and HTML', 'lxml'),
    ('html5lib', 'Web Scraping', 'html5lib: Parses HTML', 'html5lib'),
    ('numpy', 'Data Manipulation', 'NumPy: Fundamental package for numerical computation', 'NumPy'),
    ('pandas', 'Data Manipulation', 'Pandas: Data manipulation and analysis tool', 'Pandas'),
    ('matplotlib', 'Data Visualization', 'Matplotlib: Plotting library', 'Matplotlib'),
    ('seaborn', 'Data Visualization', 'Seaborn: Statistical data visualization', 'Seaborn'),
    ('plotly', 'Data Visualization', 'Plotly: Interactive graphing library', 'Plotly'),
    ('bokeh', 'Data Visualization', 'Bokeh: Interactive visualization library', 'Bokeh'),
    ('scikit-learn', 'Machine Learning', 'Scikit-learn: Machine learning library', 'Scikit-learn'),
    ('tensorflow', 'Machine Learning', 'TensorFlow: Open-source platform for machine learning', 'TensorFlow'),
    ('keras', 'Machine Learning', 'Keras: High-level neural networks API', 'Keras'),
    ('pytorch', 'Machine Learning', 'PyTorch: Deep learning framework', 'PyTorch'),
    ('scipy', 'Data Science', 'SciPy: Scientific and technical computing', 'SciPy'),
    ('statsmodels', 'Data Science', 'Statsmodels: Statistical models', 'Statsmodels'),
    ('nltk', 'NLP', 'NLTK: Natural Language Toolkit', 'NLTK'),
    ('spacy', 'NLP', 'Spacy: Industrial-strength NLP library', 'SpaCy'),
    ('sqlalchemy', 'Database', 'SQLAlchemy: SQL toolkit and ORM library', 'SQLAlchemy'),
    ('pymongo', 'Database', 'PyMongo: MongoDB driver', 'PyMongo'),
    ('requests', 'Networking', 'Requests: Simplifies making HTTP requests', 'Requests'),
    ('socket', 'Networking', 'Socket: Provides low-level networking interfaces', 'Socket'),
    ('pillow', 'Utilities', 'Pillow: Image processing library', 'Pillow'),
    ('opencv-python', 'Utilities', 'OpenCV: Computer vision and machine learning library', 'OpenCV'),
    ('django', 'Web Development', 'Django: High-level web framework', 'Django'),
    ('flask', 'Web Development', 'Flask: Lightweight WSGI web application framework', 'Flask'),
    ('scrapy', 'Web Scraping', 'Scrapy: Web crawling framework', 'Scrapy')
]

# Sort packages alphabetically by category and then name
packages.sort(key=lambda x: (x[1], x[0]))

def PackageInstaller():
    # Calculate max width for two columns based on longest descriptions
    max_description_length = max(len(f"{desc}") for _, _, desc, _ in packages)
    width_in_pixels = max_description_length * 8 * 2  # Approximate width for two columns

    def install_packages():
        selected_packages = [(pkg[0], pkg[3]) for pkg, var in zip(packages, package_vars) if var.get()]
        total_packages = len(selected_packages)
        failed_packages = []
        already_installed = []

        if not selected_packages:
            messagebox.showwarning("No Selection", "No packages selected")
            return

        # Create a separate progress window
        progress_window = tk.Toplevel(root)
        progress_window.title("Installation Progress")
        progress_label = tk.Label(progress_window, text="", font=("Helvetica", 10))
        progress_label.pack(padx=10, pady=10)

        for i, (install_name, display_name) in enumerate(selected_packages, start=1):
            # Update the progress window with the current package number and name
            progress_label.config(text=f"({i}/{total_packages}) Installing {display_name}...")
            progress_window.update()

            try:
                # Try to install the package, check if it’s already installed
                result = subprocess.run(['pip', 'install', install_name], capture_output=True, text=True)
                if "Requirement already satisfied" in result.stdout:
                    already_installed.append(display_name)
                    progress_label.config(text=f"({i}/{total_packages}) {display_name} is already installed")
                else:
                    progress_label.config(text=f"({i}/{total_packages}) Installing {display_name}...")
            except subprocess.CalledProcessError:
                # If installation fails, add package to the failed list
                failed_packages.append(display_name)

            progress_window.update()

        # Close the progress window after completion
        progress_window.destroy()

        # Display final results
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

        root.destroy()  # Close the main window after installation

    def toggle_install_button(*args):
        selected = any(var.get() for var in package_vars)
        install_button.config(state=tk.NORMAL if selected else tk.DISABLED)

    def toggle_all_packages():
        is_selected = select_all_var.get()
        for var in package_vars:
            var.set(is_selected)
        for cat_var in category_vars.values():
            cat_var.set(is_selected)
        toggle_install_button()  # Ensure the Install button updates based on new selections

    def toggle_category(category):
        is_selected = category_vars[category].get()
        for idx, (_, cat, _, _) in enumerate(packages):
            if cat == category:
                package_vars[idx].set(is_selected)
        toggle_install_button()

    def on_mouse_scroll(event):
        # Scroll the canvas on two-finger gestures or mouse scroll
        if event.num == 5 or event.delta == -120:
            canvas.yview_scroll(1, "units")  # Scroll down
        elif event.num == 4 or event.delta == 120:
            canvas.yview_scroll(-1, "units")  # Scroll up

    # Create the main window with calculated width based on content size
    root = tk.Tk()
    root.title("Package Installer")
    root.geometry(f"{width_in_pixels}x600")

    # Header frame for Select All and Install button, aligned at the top-right
    header_frame = tk.Frame(root)
    header_frame.pack(side="top", fill="x", pady=10, padx=10)

    # Right-align the Select All checkbox and Install button
    select_all_var = tk.IntVar()
    select_all_checkbutton = tk.Checkbutton(
        header_frame, text="Select All", variable=select_all_var, command=toggle_all_packages
    )
    install_button = tk.Button(header_frame, text="Install", state=tk.DISABLED, command=install_packages)

    # Place both items in the top-right corner, with `Select All` left of `Install`
    install_button.pack(side="right")
    select_all_checkbutton.pack(side="right", padx=5)

    # Create a canvas for scrolling
    canvas = tk.Canvas(root, width=width_in_pixels)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Make the frame scrollable
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Bind mouse scroll events for smooth scrolling
    canvas.bind_all("<MouseWheel>", on_mouse_scroll)  # Windows and macOS
    canvas.bind_all("<Button-4>", on_mouse_scroll)    # Linux scroll up
    canvas.bind_all("<Button-5>", on_mouse_scroll)    # Linux scroll down

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Variables for the package and category toggles
    package_vars = [tk.IntVar() for _ in packages]
    category_vars = {}

    # Track current category to organize packages by category
    current_category = None
    row = 0

    # Create toggle buttons for each package organized by category
    for i, (install_name, category, description, display_name) in enumerate(packages):
        if category != current_category:
            # Display category label with checkbox only once per category
            category_vars[category] = tk.IntVar()
            cat_checkbutton = tk.Checkbutton(
                scrollable_frame, text=category, variable=category_vars[category],
                font=('Helvetica', 12, 'bold'), pady=5,
                command=lambda cat=category: toggle_category(cat)
            )
            cat_checkbutton.grid(row=row, column=0, columnspan=2, sticky='w', padx=10)
            current_category = category
            row += 1

        # Place packages in two columns under each category
        col = (i % 2) * 2  # Alternate columns for each item in a row
        checkbutton = tk.Checkbutton(
            scrollable_frame, text=description, variable=package_vars[i], 
            command=toggle_install_button, anchor="w"  # Remove width restriction for dynamic sizing
        )
        checkbutton.grid(row=row, column=col, sticky='w', padx=30, pady=2)
        
        # Move to a new row after filling both columns
        if col == 2:
            row += 1

    # Start the application
    root.mainloop()






