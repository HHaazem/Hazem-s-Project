import subprocess

# List of packages to install
packages_to_install = ["pyinstaller", "qrcode", "Pillow"]

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(["pip", "install", package])
        except Exception as e:
            print(f"Failed to install {package}: {e}")

if __name__ == "__main__":
    print("Installing required packages...")
    install_packages(packages_to_install)
    print("Installation complete.")
