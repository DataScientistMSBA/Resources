# coding: utf-8



def OutdatedPackages():
    """Function to retrieve the list of outdated packages."""
    result = subprocess.run(['pip', 'list', '--outdated', '--format', 'json'], stdout=subprocess.PIPE)
    outdated_packages = json.loads(result.stdout)
    return outdated_packages

def UpdatePackages():
    """Function to update pip and all outdated packages using the list from OutdatedPackages()."""
    # Update pip first
    print("Checking for pip updates...")
    subprocess.run(['pip', 'install', '--upgrade', 'pip'])

    # Get outdated packages
    outdated_packages = OutdatedPackages()

    print("Outdated Packages:")
    for package in outdated_packages:
        print(f"{package['name']} ({package['version']}) -> {package['latest_version']}")

    # Update each outdated package with progress bar
    for package in outdated_packages:
        print(f"Updating {package['name']}...")
        process = subprocess.Popen(['pip', 'install', '--upgrade', package['name']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        for line in process.stdout:
            print(line.decode().strip())

    print("All outdated packages have been updated.")

