import boto3
import json

def SqsRead():
    recibos = []
    answerlist = []
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team1',
    )
    for message in response["Messages"]:
        recibos.append(message['ReceiptHandle'])
        data = json.loads(message['Body'])
        answerlist.append(data)
        print(data)
    for answer in answerlist:
        mensaje = json.dumps(answer)
        print(mensaje)
        #respuesta = sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_response1', MessageBody = mensaje)
    #for r in recibos:
        #response = sqs.delete_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team1', ReceiptHandle = r)

SqsRead()

#print(h[0]['orden']
#for i in range(len(h)):
#    print(h[i]['orden'][0]['quantity'])
#    print(h[i]['orden'][1]['quantity'])

