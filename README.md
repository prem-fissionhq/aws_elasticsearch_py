The `elasticsearch_iam_api_auth.py` file helps us to connect to AWS elasticsearch cluster using IAM users credentials.
This is also comes into use when Kibana is getting authenticated using AWS Cognito service and in this case Elasticsearch is by default considered as to be authenticate via IAM user credentials.

--

Issue#1:
```
elasticsearch.exceptions.AuthorizationException: AuthorizationException(403, 'security_exception', 'no permissions for [indices:data/read/search]
and User [name=arn:aws:iam::12345698765432:user/pkasha, backend_roles=[], requestedTenant=null]')

elasticsearch.exceptions.AuthorizationException: AuthorizationException(403, 'security_exception', 'no permissions for [cluster:monitor/main] 
and User [name=arn:aws:iam::12345698765432:user/pkasha, backend_roles=[], requestedTenant=null]')

```
If you run into above errors, it means that respective IAM user is not added as authenticated user in ES roles. 
so please follow below process to add this IAM user into authenticated user via Kibana dashboard. 

## How to Fix

The reason that you couldn’t see the “summary” is due to the IAM user doesn’t have permissions to access the “_cluster/health” endpoint. An easy fix is to log into the Kibana interface, go to “Security” -> “Roles” -> “all_access” -> “Mapped users”, then add your IAM user ARN, for example, mine is (arn:aws:iam::xxxxxx:user/txu) to internal user mapping:

Reference link: https://tonylixu.medium.com/aws-elasticsearch-no-permissions-for-cluster-monitor-health-19c9630454f5

