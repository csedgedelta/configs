# Load Generators
## NGINX
 ed-gen-nginx.yml

* Run: kubectl apply -f ed-nginx-deployment.yml
* Delete: kubectl delete -f ed-nginx-deployment.yml
* Logs: kubectl logs -l app=ed-gen-nginx -n ed-gen-nginx -f
* Scale: kubectl scale --replicas=0 deployment/ed-gen-nginx -n ed-gen-nginx
  * Default: kubectl scale --replicas=2 deployment/ed-gen-nginx -n ed-gen-nginx

## NGINX Long
 ed-gen-long.yml

* Run: kubectl apply -f ed-nginx-long.yml
* Delete: kubectl delete -f ed-nginx-long.yml
* Logs: kubectl logs -l app=ed-gen-long -n ed-gen-long -f
* Scale: kubectl scale --replicas=0 deployment/ed-gen-long -n ed-gen-long
  * Default: kubectl scale --replicas=2 deployment/ed-gen-long -n ed-gen-long
