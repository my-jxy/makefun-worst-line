import os

# The chosen pickup line, designed to be amusingly bad and AI-like.
LINE = "Warning: All other romantic interests have been deprecated in favor of your superior interface. Consider this an upgrade notification."

def main():
    if not (1 <= len(LINE) <= 140):
        raise ValueError(f"Pickup line must be between 1 and 140 characters. Current length: {len(LINE)}")

    output_dir = "/output"
    output_file_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True) # Ensure output directory exists

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
