# Deployment

Helm chart are defined to deploy application in Kubernetes cluster

# Install K3s

```bash
  curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.29.5+k3s1 sh -s - --write-kubeconfig-mode 644
  export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

# Install Helm

```bash
  curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
  sudo apt-get install apt-transport-https --yes
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
  sudo apt-get update
  sudo apt-get install helm=3.15.1-1
```

# Compilation

Compile all containers with `docker compose build` in `login`, `api` and `training` directories. 

# Registry

Run a local registry :

```bash
  docker run -d -p 5000:5000 --name registry registry:2.7
```

Send all containers in registry :

```bash
  docker tag login-login-api:latest localhost:5000/login-login-api:latest
  docker push localhost:5000/login-login-api:latest
  docker tag training-init-model-api:latest localhost:5000/training-init-model-api:latest
  docker push localhost:5000/training-init-model-api:latest
  docker tag training-import-model:latest localhost:5000/training-import-model:latest
  docker push localhost:5000/training-import-model:latest
  docker tag training-make-dataset:latest localhost:5000/training-make-dataset:latest
  docker push localhost:5000/training-make-dataset:latest
  docker tag training-training:latest localhost:5000/training-training:latest
  docker push localhost:5000/training-training:latest
  docker tag api-prediction-api:latest localhost:5000/api-prediction-api:latest
  docker push localhost:5000/api-prediction-api:latest
```

# Deploy

Create namespaces :

```bash
  kubectl create namespace login
  kubectl create namespace training
  kubectl create namespace api
  kubectl create namespace monitoring
```

Deploy containers with kubectl :

```bash
  kubectl apply -f monitoring
  kubectl apply -f login
  kubectl apply -f training
  kubectl apply -f api
```

# URL

All IPs can be retrieve by :

```bash
  kubectl get service --namespace=monitoring
  kubectl get service --namespace=login
  kubectl get service --namespace=training
  kubectl get service --namespace=api
```

# Configuration

Go to LakeFS URL and create `accidents` repository (URL and credentials are defined in helm chart file).

Go to Graphana and create dashboards for Postgresql.

- Connections > Data sources
- Add new Datasource
- Postgresql
- Add Prometheus server URL
- Dashboards > New > New dashboard
- Import dashboard
  - Copy 9628 id + load
  - Select prometheus in DS_PROMETHEUS
  - Import
