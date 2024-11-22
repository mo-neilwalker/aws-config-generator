import os
import re

# Define the input file and output config file paths
input_file = "./input/aws_accounts.txt"
output_file = os.path.expanduser("./output/config")

# Define the SSO start URL, region, registration scopes and role name
sso_session_name = input("Enter the SSO Session Name: ").strip()
sso_start_url = input("Enter the SSO Start URL: ").strip()
sso_region = input("Enter the SSO Region [eu-west-2]: ").strip() or "eu-west-2"
sso_registration_scopes = (
    input("Enter the SSO Registration Scopes [sso:account:access]: ").strip()
    or "sso:account:access"
)
sso_role_name = (
    input("Enter the SSO Role Name: [SupportAccess] ").strip() or "SupportAccess"
)

# Define the default AWS region and AWS CLI output format
aws_region = input("Enter a default AWS region [eu-west-2]: ").strip() or "eu-west-2"
aws_cli_output_format = (
    input("Enter a default AWS CLI output format [json]: ").strip() or "json"
)

# Regular expression to match the account details
pattern = re.compile(r"(.+?)\n\n(\d+)\s*\|\s*(.+)(?:\n|$)")

# Read the input file
with open(input_file, "r") as f:
    content = f.read()

# Open the output file for writing
with open(output_file, "w") as f:
    # Write the default SSO session block
    f.write(f"[sso-session {sso_session_name}]\n")
    f.write(f"sso_start_url = {sso_start_url}\n")
    f.write(f"sso_region = {sso_region}\n")
    f.write(f"sso_registration_scopes = {sso_registration_scopes}\n\n")

    # Find all matches in the content
    matches = pattern.findall(content)
    for match in matches:
        _, account_number, account_email = match
        account_name = account_email.split("@")[0].removeprefix("aws-")
        f.write(f"[profile {account_name}]\n")
        f.write(f"sso_session = {sso_session_name}\n")
        f.write(f"sso_account_id = {account_number}\n")
        f.write(f"sso_role_name = {sso_role_name}\n")
        f.write(f"output = {aws_cli_output_format}\n")
        f.write(f"region = {aws_region}\n\n")

print(f"Config file created at {output_file}")
