import boto3
import json



def SqsRead():
    recibos = []
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team1',
        MaxNumberOfMessages = 3
    )
    if response != None:
         for message in response["Messages"]:
            recibos.append(json.loads(message["Body"]))
    return recibos



def SqsDel(Lista):
    sqs = boto3.resource('sqs')
    for r in Lista:
        response=sqs.delete_message(QueueURL='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team1',ReceiptHandle=r)

rec = SqsRead()
#print(h[0]['orden']
#for i in range(len(h)):
#    print(h[i]['orden'][0]['quantity'])
#    print(h[i]['orden'][1]['quantity'])


def SqsWrite(mensaje):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName= 'cc406_response1')
    response = queue.send_message(MessageBody=mensaje)
