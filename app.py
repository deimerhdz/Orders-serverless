#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_projects.aws_projects_stack import AwsProjectsStack


app = cdk.App()
AwsProjectsStack(app, "AwsProjectsStack")

app.synth()
