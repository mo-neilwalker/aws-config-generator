# AWS Config Generator

Python helper script to create an AWS config from a list of AWS accounts

## Instructions

1. Copy all the accounts listed within the AWS Access Portal, leaving any formatting as is.
2. Add the copied text to a file named ./input/aws_accounts.txt
3. Run the script, inputting any infor when prompted.
4. Move the the config file from ./output/config to ~/.aws/config

## Limitations

Config file becomes very verbose with many accounts, especially when you have multiple levels of access.

