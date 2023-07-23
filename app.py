#!/usr/bin/env python3
from pathlib import Path
import aws_cdk as cdk
from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


app = cdk.App()
CdkWorkshopStack(app, "cdk-workshop")

app.synth()   # produce AWS CloudFormation template for each stack defined in your application.

#aws_path = Path.home() / ".aws"

#import os
#from dotenv import load_dotenv

#load_dotenv(Path.cwd() / "cdk_workshop/.env")

#aws_access_key_id = os.getenv('aws_access_key_id')
#aws_access_key_id