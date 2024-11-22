# AWS Config Generator

Python helper script to create an AWS config from a list of AWS accounts

## Instructions

1. Copy all the accounts listed within the AWS Access Portal, leaving any formatting as is.
2. Add the copied text to a file named ./input/aws_accounts.txt
3. Run the script, inputting any information when prompted.
4. Move the the config file from ./output/config to ~/.aws/config

## Limitations
- Config file becomes very verbose with many accounts, especially when you have multiple levels of access.
- default Level of access not always valid (SupportAccess is not available on for example MOSRS)
- default region is not always correct

## Possible Issues
- ./input/aws_accounts.txt must follow a specific format for the regex to be satisfied, at the time of writing the regex is correct, however as amazon frequently updated aws, it may need to be updated.