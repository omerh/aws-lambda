import sys
import boto3
import datetime
import os

s3 = boto3.resource('s3')

def lambda_handler(event, context):
	s3bucket = event['Records'][0]['s3']['bucket']['name']
	s3object = event['Records'][0]['s3']['object']['key']
	s3file = os.path.basename(s3object)
	newparentdirectory = os.path.dirname(s3object).split('/')[1]
	print s3bucket
	print s3object
	object = s3.Object(s3bucket,s3object)
	yearfolderpath = 'dt=' + object.last_modified.strftime("%Y-%m-%d")
	hourfolderpath = 'hh=' + object.last_modified.strftime("%H")
	s3objectkeypath = 'processed' + '/' + newparentdirectory + '/' + yearfolderpath + "/" + hourfolderpath + "/" + s3file
	print "File " + s3object + ", on bucket " + s3bucket + " will be moved to " + s3objectkeypath
	s3.Object(s3bucket,s3objectkeypath).copy_from(CopySource=s3bucket + '/' + s3object)
	#s3.Object(s3bucket, s3object).delete()
