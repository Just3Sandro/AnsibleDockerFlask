# AnsibleDockerProject (Déploiement sur GNS3)

## 📌 Objectif
Ce projet a été conçu pour expérimenter le **déploiement automatisé** d’une infrastructure **dans un environnement simulé sous GNS3**.

Il permet de mettre en place :
- Une **API Flask** déployée dans un conteneur Docker
- Une **base de données PostgreSQL** séparée
- Un **système de monitoring (Prometheus & Grafana)**
- Une **gestion centralisée avec Ansible** pour automatiser l’installation et la configuration

💡 **Pourquoi GNS3 ?**  
Le but est de reproduire un **environnement réseau réaliste**, où chaque service tourne sur une **machine distincte** (Web, DB, Monitoring).  
Cela permet de mieux comprendre comment **les services communiquent entre eux sur un réseau réel**.

## 🚀 Technologies utilisées
- **Docker & Docker Compose** → Gestion et orchestration des conteneurs
- **Flask (Python)** → API Web
- **PostgreSQL** → Base de données
- **Prometheus & Grafana** → Monitoring des services
- **Ansible** → Automatisation de l'installation
- **GNS3** → Simulation du réseau et des machines

## 📦 Installation

### 1️⃣ **Cloner le projet**
Sur la VM Bastion :
```sh
git clone https://github.com/ton-user/AnsibleDockerProject.git
cd AnsibleDockerProject
