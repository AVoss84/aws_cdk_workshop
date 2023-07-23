from constructs import Construct      # abstract cloud component
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,     # note that lambda is a builtin function, we won't overide it
    aws_apigateway as apigw,   # API Gateway which proxies all requests to an AWS Lambda function
)

from .hitcounter import HitCounter


class CdkWorkshopStack(Stack):
    # Constructs are always created in the scope of another construct and must always have an identifier which must be unique within the scope it’s created. 
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:     #scope in which this consgtructb is created; construct id
        super().__init__(scope, id, **kwargs)

        # Define an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,         # Our function uses the Python 3.7 runtime
            code=_lambda.Code.from_asset('lambda'),     # handler code is loaded from our lambda directory
            handler='hello.handler',          #  name of the handler function is hello.handler (“hello” is the name of the file and “handler” is the function name)
        )
        
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        # Define an API endpoint and associate it with our Lambda function.
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter._handler,
        )


