import os
import re

def main():
    # # Warning
    input("Warning: config.txt may need further modification, this is particularly the case for the default region and sso_role_name for the profiles, which may not be valid in all cases.\n")

    # # Define the input file and output config file paths
    input_file = "./input/aws_accounts.txt"
    output_file = os.path.expanduser("./output/config.txt")

    # # Default values
    default_sso_region = "eu-west-2"
    default_registration_scopes = "sso:account:access"
    default_sso_role_name = "SupportAccess"
    default_aws_region = "eu-west-2"
    default_cli_output_format = "json"

    # # Define the SSO start URL, region, registration scopes and role name
    sso_session_name = input("Enter the SSO Session Name: ")
    sso_start_url = input("Enter the SSO Start URL: ")
    sso_region = input(f"Enter the SSO Region [{default_sso_region}]: ") or default_sso_region
    sso_registration_scopes = input(f"Enter the SSO Registration Scopes [{default_registration_scopes}]: ") or default_registration_scopes
    sso_role_name = input(f"Enter the SSO Role Name: [{default_sso_role_name}] ") or default_sso_role_name

    # # Define the default AWS region and AWS CLI output format
    aws_region = input(f"Enter a default AWS region [{default_aws_region}]: ") or default_aws_region
    aws_cli_output_format = input(f"Enter a default AWS CLI output format [{default_cli_output_format}]: ") or default_cli_output_format


    # # Regular expression to match the account details
    # # regex required changing, as it featured a additional \n after the first line in the pattern
    # pattern = re.compile(r"(.+?)\n\n(\d+)\s*\|\s*(.+)(?:\n|$)")
    pattern = re.compile(r"(.+?)\n(\d+)\s*\|\s*(.+)(?:\n|$)")

    # # Read the input file
    with open(input_file, "r") as f:
        content = f.read()

    # # Open the output file for writing
    with open(output_file, "w") as f:
        # # Write the default SSO session block
        f.write(f"[sso-session {sso_session_name}]\n")
        f.write(f"sso_start_url = {sso_start_url}\n")
        f.write(f"sso_region = {sso_region}\n")
        f.write(f"sso_registration_scopes = {sso_registration_scopes}\n\n")

        # # Find all matches in the content
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

main()