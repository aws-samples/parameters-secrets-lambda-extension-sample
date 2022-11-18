## parameters-secrets-lambda-extension-sample

This project contains source code and supporting files for deploying resources described in following blog: 
[Using the AWS Parameter and Secrets Lambda extension to cache parameters and secrets](https://aws.amazon.com/blogs/compute/using-the-aws-parameter-and-secrets-lambda-extension-to-cache-parameters-and-secrets/)

- sample-code - Code for the sample Lambda function.
- template.yaml - A template that defines the AWS resources used in the example.

## Deployment instructions

```
git clone https://github.com/aws-samples/parameters-secrets-lambda-extension-sample.git
sam build 
sam deploy --guided
```

The deploy command will package and deploy your application to AWS, with a series of prompts as seen below:

```
Setting default arguments for 'sam deploy'

================================

Stack Name [sam-app]: parameter-secrets-extension-blog-stack
AWS Region [us-east-1]: <ENTER YOUR CHOICE OF REGION>
Parameter pVpcCIDR [172.31.0.0/16]: 
Parameter pPublicSubnetCIDR [172.31.3.0/24]: 
Parameter pPrivateSubnetACIDR [172.31.2.0/24]: 
Parameter pPrivateSubnetBCIDR [172.31.1.0/24]: 
Parameter pDatabaseName [DemoAppDatabase]: 
Parameter pDatabaseUsername [myadmin]: 
Parameter pDBEngineVersion [5.7]: 
#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
Confirm changes before deploy [y/N]: y
#SAM needs permission to be able to create roles to connect to the resources in your template
Allow SAM CLI IAM role creation [Y/n]: y
#Preserves the state of previously provisioned resources when an operation fails
Disable rollback [y/N]: N
Save arguments to configuration file [Y/n]: y
SAM configuration file [samconfig.toml]: 
SAM configuration environment [default]: 

Looking for resources needed for deployment:
  Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-9cqpewwuywgs
  A different default S3 bucket can be set in samconfig.toml

Saved arguments to config file
Running 'sam deploy' for future deployments will use the parameters saved above.
The above parameters can be changed by modifying samconfig.toml
```
## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

