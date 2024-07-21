from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct


class AwsProjectsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        hello_world_function = _lambda.Function(
            self,
            "HelloWorldFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,  # Choose any supported Node.js runtime
            # Points to the lambda directory
            code=_lambda.Code.from_asset("lambda"),
            handler="hello.handler",  # Points to the 'hello' file in the lambda directory
        )

        api = apigateway.LambdaRestApi(
            self,
            "HelloWorldApi",
            handler = hello_world_function,
            proxy = False,
        )
        
        # Define the '/hello' resource with a GET method
        hello_resource = api.root.add_resource("hello")
        hello_resource.add_method("GET")
        