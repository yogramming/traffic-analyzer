# 🚀 Traffic Analyzer CI/CD + GitOps Project

## 📌 Overview

This project demonstrates a **production-style CI/CD pipeline** using:

- Python (Flask) → application
- Docker → containerization
- Jenkins → CI (build + push)
- GitHub → source + configuration repos
- Kubernetes → deployment platform
- ArgoCD → CD (GitOps)

The application is a **Traffic Analyzer API** that tracks incoming requests and exposes metrics.

---

## 🧠 Architecture

Developer (Git Push)
↓
GitHub (App Repo)
↓
Jenkins (CI Pipeline)
↓
DockerHub (Image Registry)
↓
GitHub (K8s Repo)
↓
ArgoCD (GitOps CD)
↓
Kubernetes Cluster
↓
Running Application

---

## 🧩 Project Structure

### 🔹 App Repository (`traffic-analyzer`)

traffic-analyzer/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile

---

### 🔹 Kubernetes Repository (`traffic-analyzer-k8s`)

traffic-analyzer-k8s/
├── deployment.yml
├── service.yml

---

## ⚙️ Application Details

### 🔹 Features

- Tracks:
  - Total requests
  - Endpoint hits
  - IP addresses

### 🔹 Endpoints

- `/` → Health check
- `/stats` → JSON analytics
- `/metrics` → Prometheus-compatible metrics

---

## 🐳 Docker

### Build locally

```bash
docker build -t traffic-analyzer .
docker run -p 5000:5000 traffic-analyzer
⚙️ Jenkins Pipeline
Stages
Build Image
Push Image to DockerHub
Update Kubernetes Repo
CI Flow
git push →
Jenkins builds image →
pushes to DockerHub →
updates K8s repo →
ArgoCD deploys
🔐 Jenkins Credentials
ID	Purpose
dockerhub-creds	Push Docker images
github-creds	Update K8s repo
☸️ Kubernetes Deployment
Deployment with 2 replicas
Uses versioned Docker images
Service exposed via NodePort
🔄 ArgoCD (GitOps)
Responsibilities
Watches traffic-analyzer-k8s repo
Applies changes automatically
Keeps cluster in sync with Git
Sync Policy
Automatic Sync ✅
Prune ✅
Self Heal ✅
🔁 End-to-End CI/CD Flow
Developer pushes code
Jenkins triggers (Poll SCM)
Jenkins:
Builds Docker image
Pushes image
Updates K8s repo
ArgoCD:
Detects repo change
Syncs deployment
Kubernetes:
Performs rolling update
Replaces old pods
🧪 Verification
Check running image
kubectl describe pod | grep Image:

Expected:

yogramming/traffic-analyzer:<latest-tag>
Watch rollout
kubectl get pods -w
⚡ Deployment Strategy
Rolling updates (zero downtime)
Old pods terminate after new pods are ready
🌐 Automation
Jenkins Trigger
Poll SCM (H/2 * * * *)
Checks GitHub every ~2 minutes
⚠️ Common Issues & Fixes
Issue	Cause	Fix
ImagePullBackOff	Image not pushed	Push to DockerHub
Git push fails	Token permissions	Use PAT with write access
ArgoCD not deploying	Auto-sync disabled	Enable auto-sync
Jenkins not triggering	No trigger configured	Enable Poll SCM
📈 Future Improvements
Prometheus + Grafana dashboards
Horizontal Pod Autoscaler (HPA)
Ingress + domain routing
GitHub Webhooks instead of polling
Staging + production environments
🏆 What This Project Demonstrates
Real-world CI/CD pipeline
GitOps workflow
Kubernetes deployment strategies
Docker image lifecycle
Debugging production-like issues
🎯 Key Takeaways
CI (Jenkins) builds artifacts
CD (ArgoCD) deploys from Git
Git is the single source of truth
Kubernetes ensures safe deployments
👨‍💻 Author

Built as a hands-on DevOps learning project focused on real-world workflows.

🚀 Final Note

This is not just a demo — it reflects how modern cloud-native systems are built and deployed in production.
```
