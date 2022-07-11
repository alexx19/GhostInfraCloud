from cgitb import handler
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)
from hitcounterLambda.hitcounter import HitCounter

class GhostApigatewayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Definiendo un recurso de lambda
        dummy_lambda = _lambda.Function(
            self, 'Handler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('dummy-lambda'),
            handler='dummy-lambda.handler'
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=dummy_lambda,
        )

        apigw.LambdaRestApi(
            self, 'ghost-apigateway-domain',
            handler=hello_with_counter._handler,
        )