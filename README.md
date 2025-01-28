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
git clone https://github.com/VanStarkHohenheim/email-sender.git
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
Configuration de la variable CONFIG dans `main.py` :

```python
CONFIG = {
    "EXCEL_PATH": "path/to/excel_file.xlsx",
    "EMAIL_COLUMN": "Email",
    "SMTP_SERVER": "smtp.mail.me.com",
    "SMTP_PORT": 587,
    "SENDER_EMAIL": "your_email@icloud.com",
    "APP_PASSWORD": "your_app_specific_password",
    "ATTACHMENT_PATH": "path/to/attachment.pdf",
    "EMAIL_SUBJECT": "Candidature professionnelle",
    "THROTTLE_DELAY": 5  # Secondes entre les envois
}
```

### 3. Générer un mot de passe d'application Apple
- Aller sur [appleid.apple.com](https://appleid.apple.com)  
- Section **"Sécurité"** → **"Générer un mot de passe..."**  
- Utiliser ce mot de passe dans le CONFIG `main.py`.

---

### 🖥️ Utilisation

### Lancer l'envoi des emails
```bash
python main.py
```

### ⚠️ Sécurité
- Ne jamais commiter le fichier modifier `main.py`.
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
├── main.py              # Script principal
└── README.md
```

### 📌 Limitations
- **Limite iCloud** : ~100 emails/jour  
- **Taille max des pièces jointes** : 20MB  
- **Délai recommandé entre les envois** : 5 secondes
