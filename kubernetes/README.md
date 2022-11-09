# Load Generators
## NGINX
 ed-gen-nginx.yml

Run: kubectl apply -f ed-nginx-deployment.yml
Delete: kubectl delete -f ed-nginx-deployment.yml
Logs: kubectl logs -l app=ed-gen-nginx -n ed-gen-nginx -f
