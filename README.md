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
