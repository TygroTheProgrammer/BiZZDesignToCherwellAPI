# 🔄 BiZZDesign to Cherwell Field Sync

This project is a **Python-based tool** that automatically syncs important application data from a platform called **BiZZDesign** into another platform called **Cherwell**. It connects to both systems via their APIs (a way for software to talk to each other), extracts specific information, and updates it in the target system.

---

## 📌 What This Project Does

- ✅ Logs into BiZZDesign and Cherwell using secure credentials
- 🔍 Retrieves details from a specific BiZZDesign application (like name, recovery time, inputs, etc.)
- ✏️ Updates a matching application entry in Cherwell with the latest data

---

## 🧠 Who Is This For?

This is for IT teams, enterprise architects, or developers who:

- Need to keep system documentation up to date
- Want to reduce manual data entry between tools
- Are using **Cherwell** for configuration management and **BiZZDesign** for architecture modeling

Even if you're **not familiar with Python or APIs**, this README will help guide you through setup and usage!

---

## 🧰 Requirements

Before running this project, make sure you have:

1. **Python 3.7 or later** installed on your computer  
2. **Git** (optional, for cloning the project)  
3. A basic understanding of the command line (or terminal)

---

## 📦 Installation Steps

### 1. Clone or Download the Repository

```bash
git clone https://github.com/yourusername/bizzdesign-cherwell-sync.git
cd bizzdesign-cherwell-sync
```

Or just Download ZIP and unzip it.

## 2. Set Up Your Python Environment
Install required libraries using pip:

```bash
pip install -r requirements.txt
```
If you don’t have pip, follow this guide.

---

## 🔐 Configuration
This project uses a .env file to store sensitive information (like usernames and passwords) safely.

Create a file named .env in the project folder and add the following details:

```ini
# Cherwell Credentials
C_BASE_URL=https://your-cherwell-instance.com
C_USERNAME=yourCherwellUsername
C_PASSWORD=yourCherwellPassword
C_AUTH_URL=https://your-cherwell-instance.com/token
C_CLIENT_ID=yourCherwellClientID
C_BUSINESS_OBJ_ID=ConfigApplications

# BiZZDesign Credentials
B_BASE_URL=https://your-bizzdesign-instance.com
B_AUTH_URL=https://your-bizzdesign-instance.com/oauth/token
B_CLIENT_ID=yourBizzDesignClientID
B_CLIENT_SECRET=yourBizzDesignClientSecret
```
⚠️ Important: Never share your .env file or push it to GitHub!

---

## 🚀 How to Run the Script
From the terminal, run:

```bash
python api.py
```
This will:
- Log into both platforms
- Extract data from BiZZDesign
- Update that data in Cherwell

You’ll see no visible output unless there's an error — but everything is happening behind the scenes!

## 🧪 What’s Actually Happening?
1. Authentication
The script uses secure tokens to log into both BiZZDesign and Cherwell — like a login session.

2. Data Extraction (from BiZZDesign)
The script looks for a specific application and grabs:
- Application name
- Recovery Time Objective (RTO)
- Major inputs and outputs
- Licensing impact
- Operating system info
3. Data Upload (to Cherwell)
It then updates a matching app in Cherwell with the latest info.

---

## 🤔 FAQs
Q: I don’t know Python. Can I still use this?
Absolutely! Once installed, just follow the instructions to run python sync.py.

Q: Can I change what data is transferred?
Yes. Just modify the fields in the data dictionary inside the updateFields() function in sync.py.

Q: Is my data secure?
As long as you keep your .env file private and don't upload it to GitHub, your credentials remain safe.
---

## 🛠️ Dependencies
- requests – To send HTTP requests
- jmespath – To extract data from JSON
- python-dotenv – To load credentials from .env file

Install them all via:
```bash
pip install requests jmespath python-dotenv
```

## 📬 Want to Contribute?
Pull requests are welcome! Feel free to suggest improvements or new features.

## 📝 License
This project is open-source under the MIT License.
