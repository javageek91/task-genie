import boto3 as bo3
import json

bedrock_runtime = bo3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)
prompt = "apple pie"


kwargs = {
 "modelId": "ai21.j2-ultra-v1",
 "contentType": "application/json",
 "accept": "*/*",
 "body": "{\"prompt\":\"Apple\",\"maxTokens\":200}"
}

bedrock_model_response = bedrock_runtime.invoke_model(**kwargs)
#print(json.loads(bedrock_model_response))
bedrock_model_response_body = json.loads(bedrock_model_response.get('body').read())
print("**Sumanth***" + str(bedrock_model_response_body))