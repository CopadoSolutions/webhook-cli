import argparse, urllib, json, time, urlparse, sys

parser = argparse.ArgumentParser(description='Copado Webhook API. Command Line Interface.',
	epilog='More information at http://docs.copado.apiary.io and http://docs.copa.do',
	prog='copado')
parser.add_argument('-url', dest='url', required=True, nargs=1,
                   help='Copado Webhook URL.')
args = parser.parse_args()
url = args.url[0]

print "calling %s" % url
response = urllib.urlopen(url)
jsontext = response.read()
print jsontext
data = json.loads(jsontext)
jobId = data["copadoJobId"]
print ">>> copadoJobId is %s" % jobId
isFinished = False
isSuccess = False
data = None
print ""
while not isFinished:
	time.sleep(5)
	parts = urlparse.urlparse(url)
	query = urlparse.parse_qs(parts.query)
	api_key = query['api_key'][0]
	statusUrl = "%s://%s/json/v1/webhook/jobStatus/%s?api_key=%s" % (parts.scheme, parts.netloc, jobId, api_key)
	print "calling %s" % statusUrl
	response = urllib.urlopen(statusUrl)
	jsontext = response.read()
	print ""
	print jsontext
	print ""
	data = json.loads(jsontext)
	isFinished = data["isFinished"]
	print ">>> status: %s" % data["status"]
	print ">>> isFinished is %s" % isFinished
	print ""
isSuccess = data["isSuccess"]
if isSuccess:
	print "FINISHED SUCCESSLFULLY"
else:
	print "FAILURE %s" % data["messages"]
	sys.exit(1)

