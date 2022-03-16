from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
import aws_cdk as cdk
from aws_cdk.pipelines import Codepipeline, CodePipelineSource, ShellStep
from constructs import Construct

class MyPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(
            self, "MyPipeline",

            synth=ShellStep("Synth",
            input = CodePipelineSource.git_hub("chandoo1986/demos", "main"),
                commands = ["npm install -g aws-cdk", 
                    "python -m pip install -r requirements.txt",
                    "cdk synth"]
        )