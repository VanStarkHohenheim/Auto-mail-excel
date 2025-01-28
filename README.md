# 📧 Automatic Email Sender with iCloud

Script Python pour envoyer des emails personnalisés avec pièces jointes à partir d'un fichier Excel, utilisant un compte iCloud comme expéditeur.

## 📋 Fonctionnalités
- Envoi d'emails en masse depuis iCloud
- Gestion de pièces jointes
- Personnalisation du message
- Suivi d'envoi dans la console

## ⚙️ Prérequis
1. [Python 3.10+](https://www.python.org/downloads/)
2. Compte iCloud actif
3. Fichier Excel structuré avec une colonne d'emails

## 🚀 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/votreuser/email-sender.git
```

### 2. Installer les dépendances
```bash
pip install pandas openpyxl
```

### 🔧 Configuration

#### 1. Préparation du fichier Excel
Structure minimale :  

| Nom       | Email             |
|-----------|-------------------|
| John Doe  | john@example.com  |

Sauvegarder le fichier en `.xlsx`.

#### 2. Configuration du script
Créer un fichier `.env` :

```env
ICLOUD_EMAIL="votre@icloud.com"
ICLOUD_APP_PASSWORD="xxxx-xxxx-xxxx-xxxx"
EXCEL_PATH="chemin/vers/fichier.xlsx"
ATTACHMENT_PATH="chemin/vers/piece_jointe.pdf"
```

### 3. Générer un mot de passe d'application Apple
- Aller sur [appleid.apple.com](https://appleid.apple.com)  
- Section **"Sécurité"** → **"Générer un mot de passe..."**  
- Utiliser ce mot de passe dans le fichier `.env`.

---

### 🖥️ Utilisation

### Lancer l'envoi des emails
```bash
python main.py
```

### ⚠️ Sécurité
- Ne jamais commiter le fichier `.env`.
- Utiliser toujours des mots de passe d'application.
- Vérifier les permissions du fichier Excel.

---

### 🐛 Dépannage courant

#### Erreur d'authentification 535
```text
Solution :
- Régénérer le mot de passe d'application
- Vérifier l'activation SMTP sur iCloud
- Tester avec le script test_connection.py
```

*### 🐛 Fichier Excel non trouvé
- **Utiliser des chemins absolus**  
- **Vérifier les permissions du fichier**  
- ***Format attendu : `.xlsx` (pas `.xls` ou `.csv`)***

---

### 📄 Structure du projet
```bash
email-sender/
├── data/
│   └── contacts.xlsx    # Fichier des destinataires
├── attachments/
│   └── document.pdf     # Pièces jointes
├── .env                 # Configuration sensible
├── main.py              # Script principal
└── README.md
```

### 📌 Limitations
- **Limite iCloud** : ~100 emails/jour  
- **Taille max des pièces jointes** : 20MB  
- **Délai recommandé entre les envois** : 5 secondes
