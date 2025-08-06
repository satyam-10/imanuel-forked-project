import yaml
import os

# Load the YAML file
with open("config-infra-prod.yml", "r") as file:
    config = yaml.safe_load(file)

# Print contents (or set environment variables)
for key, value in config.items():
    print(f"{key}: {value}")  # Optional: just logs
    # Export as environment variable for use in subsequent steps
    with open(os.environ["GITHUB_ENV"], "a") as env_file:
        env_file.write(f"{key}={value}\n")
