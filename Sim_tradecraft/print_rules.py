import os


def read_rules_file():
    """
    Read rules from the rules.txt file in the templates folder
    and print them to the console
    """
    try:
        # Construct the file path
        file_path = os.path.join('templates', 'rules.txt')

        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return

        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Print header
        print("=" * 80)
        print("TRADE CRAFT - STOCK EXCHANGE SIMULATOR RULES")
        print("=" * 80)
        print()

        # Split content into lines and process
        lines = content.strip().split('\n')

        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line:  # Only print non-empty lines
                if i == 1:
                    # First line is the header
                    print(f"📋 {line}")
                    print("-" * 80)
                elif "Educational Purpose Only" in line:
                    # Disclaimer
                    print()
                    print("⚠️  IMPORTANT:")
                    print(f"   {line}")
                else:
                    # Regular rules
                    print(f"\n{i - 1}. {line}")

        print()
        print("=" * 80)

    except FileNotFoundError:
        print(f"Error: Could not find the file at {file_path}")
    except PermissionError:
        print(f"Error: Permission denied to read {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def read_rules_simple():
    """
    Simple version - just read and print line by line
    """
    try:
        file_path = os.path.join('templates', 'rules.txt')

        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())

    except Exception as e:
        print(f"Error: {str(e)}")


def read_rules_formatted():
    """
    Formatted version with better structure
    """
    try:
        file_path = os.path.join('templates', 'rules.txt')

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]

        # Print with formatting
        print("\n" + "🎯 " * 20)
        print("         TRADE CRAFT - GAME RULES")
        print("🎯 " * 20 + "\n")

        for idx, rule in enumerate(lines, 1):
            if idx == 1:
                print(f"📌 {rule}\n")
            elif "Educational" in rule:
                print(f"\n⚠️  {rule}\n")
            else:
                print(f"✓ Rule {idx - 1}: {rule}\n")

        print("🎯 " * 20 + "\n")

    except Exception as e:
        print(f"Error: {str(e)}")


# Main execution
if __name__ == "__main__":
    print("Choose output format:")
    print("1. Formatted with headers")
    print("2. Simple output")
    print("3. Formatted with emojis")

    choice = input("\nEnter choice (1-3) or press Enter for option 1: ").strip()

    if choice == "2":
        read_rules_simple()
    elif choice == "3":
        read_rules_formatted()
    else:
        read_rules_file()