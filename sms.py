import boto3
sns = boto3.client('sns')
number = '+56992229813'
sns.publish(PhoneNumber = number, Message='Error en procedimiento' )
