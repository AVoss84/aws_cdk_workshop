import json

#Write lambda function in Python
#AWS Lambda handler code: http response
#used by API Gateway
def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        #'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
        'body': 'Good Afternoon, CDK! You have hit {}\n'.format(event['path'])
    }
