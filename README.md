# Traffic Analyzer CI/CD + GitOps Project

## Overview

This project demonstrates a production-style CI/CD pipeline using:

- Python (Flask) — application
- Docker — containerization
- Jenkins — CI (build and push)
- GitHub — source and configuration repositories
- Kubernetes — deployment platform
- ArgoCD — CD (GitOps)

The application is a Traffic Analyzer API that tracks incoming requests and exposes metrics.

---

## Architecture

```
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
```

---

## Project Structure

### App Repository (traffic-analyzer)

```
traffic-analyzer/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
```

### Kubernetes Repository (traffic-analyzer-k8s)

```
traffic-analyzer-k8s/
├── deployment.yml
├── service.yml
```

---

## Application Details

### Features

- Tracks total requests
- Tracks endpoint hits
- Tracks IP addresses

### Endpoints

- `/` — Health check
- `/stats` — JSON analytics
- `/metrics` — Prometheus-compatible metrics

---

## Docker

### Build locally

```bash
docker build -t traffic-analyzer .
docker run -p 5000:5000 traffic-analyzer
```

---

## Jenkins Pipeline

### Stages

- Build Image
- Push Image to DockerHub
- Update Kubernetes Repository

### CI Flow

```
git push → Jenkins builds image → pushes to DockerHub → updates K8s repo → ArgoCD deploys
```

---

## Jenkins Credentials

| ID              | Purpose                      |
| --------------- | ---------------------------- |
| dockerhub-creds | Push Docker images           |
| github-creds    | Update Kubernetes repository |

---

## Kubernetes Deployment

- Deployment with 2 replicas
- Uses versioned Docker images
- Service exposed via NodePort

---

## ArgoCD (GitOps)

### Responsibilities

- Watches the `traffic-analyzer-k8s` repository
- Applies changes automatically
- Keeps the cluster in sync with Git

### Sync Policy

- Automatic sync enabled
- Prune enabled
- Self-heal enabled

---

## End-to-End CI/CD Flow

1. Developer pushes code
2. Jenkins triggers (Poll SCM)
3. Jenkins builds and pushes the Docker image
4. Jenkins updates the Kubernetes repository
5. ArgoCD detects changes
6. ArgoCD syncs the deployment
7. Kubernetes performs a rolling update

---

## Verification

### Check running image

```bash
kubectl describe pod | grep Image:
```

Expected:

```
yogramming/traffic-analyzer:<latest-tag>
```

### Watch rollout

```bash
kubectl get pods -w
```

---

## Deployment Strategy

- Rolling updates (zero downtime)
- Old pods terminate after new pods are ready

---

## Automation

- Jenkins uses Poll SCM (`H/2 * * * *`)
- Checks GitHub every ~2 minutes

---

## Common Issues and Fixes

| Issue                  | Cause                 | Fix                       |
| ---------------------- | --------------------- | ------------------------- |
| ImagePullBackOff       | Image not pushed      | Push image to DockerHub   |
| Git push fails         | Token permissions     | Use PAT with write access |
| ArgoCD not deploying   | Auto-sync disabled    | Enable auto-sync          |
| Jenkins not triggering | No trigger configured | Enable Poll SCM           |

---

## Future Improvements

- Add Prometheus and Grafana dashboards
- Add Horizontal Pod Autoscaler (HPA)
- Add Ingress and domain routing
- Replace polling with GitHub webhooks
- Add staging and production environments

---

## What This Project Demonstrates

- Real-world CI/CD pipeline
- GitOps workflow
- Kubernetes deployment strategies
- Docker image lifecycle
- Debugging real-world DevOps issues

---

## Key Takeaways

- CI (Jenkins) builds artifacts
- CD (ArgoCD) deploys from Git
- Git is the single source of truth
- Kubernetes ensures safe deployments

---

## Author

Built as a hands-on DevOps learning project focused on real-world workflows.

---

## Final Note

This project reflects how modern cloud-native systems are built and deployed in production environments.
