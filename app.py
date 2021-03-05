#!/usr/bin/env python3

from aws_cdk import core

from test_cdk.test_cdk_stack import TestCdkStack


app = core.App()
TestCdkStack(app, "test-cdk")

app.synth()
