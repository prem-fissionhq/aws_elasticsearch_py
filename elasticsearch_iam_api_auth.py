from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

host = '' # For example, my-test-domain.us-east-1.es.amazonaws.com
region = '' # e.g. us-west-1
service = 'es'
credentials = {
    'access_key': 'AKIA***********',
    'secret_key': '**************'
}

awsauth = AWS4Auth(credentials['access_key'], credentials['secret_key'], region, service)
print(awsauth)
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

info = es.info() # information about the cluster
cluster_healthy = es.ping() # provides info about cluster is running or not

print(info)

print("\n\ncluster status: ", cluster_healthy)
