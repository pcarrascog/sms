import sys
import boto3
sns = boto3.client('sns')
numero = sys.argv[1] 
mensaje = sys.argv[2]
sns.publish(PhoneNumber=numero, Message=mensaje)