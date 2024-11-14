# coding: utf-8

# # View All Upgradable Programs



import subprocess

def upgrade_all_packages():
    try:
        # Start the command with Popen
        process = subprocess.Popen(['winget', 'upgrade'],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True)

        # Send 'Y' as input to the command
        stdout, stderr = process.communicate(input='Y\n')

        # Filter the output to include only relevant lines
        output_lines = stdout.splitlines()
        filtered_output = [
            line for line in output_lines 
            if line.strip() and not line.strip().startswith(('-', '\\', '|'))  # Exclude lines with visual characters
        ]

        # Print the filtered output
        for line in filtered_output:
            print(line)

        if stderr:
            print("Errors:", stderr.strip())

    except Exception as e:
        print("An error occurred while upgrading packages:", e)

if __name__ == "__main__":
    upgrade_all_packages()


# # Upgrade All Programs



import subprocess

def upgrade_all():
    try:
        # Run the command
        subprocess.run(["winget", "upgrade", "--all"], check=True)
        print("Upgrade completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    upgrade_all()

