#!/usr/bin/env python3

import aws_cdk as cdk

from ghost_apigateway.ghost_apigateway_stack import GhostApigatewayStack


app = cdk.App()
GhostApigatewayStack(app, "ghost-apigateway")

app.synth()
