# awscli-on-lambda
sample AWS Lambda package for running [AWS Command Line Interface](https://aws.amazon.com/cli/?nc1=f_ls)

# Usage

1. modify `main.py` as you like
1. update package `zip -r9 lambda.zip main.py`
1. deploy package and choose runtime "Python 2.7", set Handler "main.handle"

# Warning

If the execution environment of AWS Lambda changes, this package may not work.
(For example, this package assumes that `/usr/bin/python` exists.)

This package created on Amazon Linux(`amzn-ami-hvm-2017.03.1.20170812-x86_64-gp2`).

# Reference

For the creation commands, refer to the following.
https://alestic.com/2016/11/aws-lambda-awscli/

on Amazon Linux, you'll need following 2 steps.

* install libyaml-devel for PyYAML

```
sudo yum install libyaml-devel
```

* put `lib64` library into package

```
(cd $virtualenv/lib64/python2.7/site-packages; zip -r9 $zipfile .)
```
