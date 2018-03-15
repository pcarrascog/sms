import sys
import boto3
sns = boto3.client('sns')
number = sys.argv[1]   #'+56992229813'
#sns.publish(PhoneNumber = number, Message='Error en procedimiento' )
print number