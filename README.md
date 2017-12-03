# awscli-on-lambda
sample AWS Lambda package for running [AWS Command Line Interface](https://aws.amazon.com/cli/?nc1=f_ls)

# Usage

1. modify `main.py` as you like
1. update package `zip -r9 lambda.zip main.py`
1. deploy package and choose runtime "Python 2.7"

# Warning

If the execution environment of AWS Lambda changes, this package may not work.
(For example, this package assumes that `/usr/bin/python` exists.)

This package created on Amazon Linux(`amzn-ami-hvm-2017.03.1.20170812-x86_64-gp2`).

# reference

For the creation procedure, refer to the following.
https://alestic.com/2016/11/aws-lambda-awscli/
