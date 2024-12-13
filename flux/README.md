


```
curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.29.5+k3s1 sh -s - --write-kubeconfig-mode 644
```

```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm=3.15.1-1
```


```
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

```
docker run -d -p 5000:5000 --name registry registry:2.7
```

```
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
```

```
kubectl create namespace training
```
