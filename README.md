# ⚡ Energy Trading using Blockchain and AI

This project is a decentralized web application that enables users to **buy, sell, and trade renewable energy (solar or other sources) directly with each other or through the grid**.  
It combines **Blockchain for secure transactions, AI for forecasting and dynamic pricing, and MERN stack for the web platform**.

---

## 🌟 Features
- Peer-to-peer **energy trading** within the grid
- **Blockchain integration** for secure and transparent transactions
- **AI-powered forecasting** using Prophet and LSTM to predict future energy demand
- **Dynamic pricing** model that adjusts prices based on predicted demand
- MERN stack-based **web dashboard** for trading and monitoring
- Uses **real-world weather & solar panel datasets** (via SAM software) for predictions

---

## 🛠 Tech Stack
### Web Development
- **MongoDB, Express.js, React.js, Node.js (MERN Stack)**

### Blockchain
- Smart contracts + **Selenium** (integration testing and automation)

### Artificial Intelligence
- **Prophet** for energy demand forecasting
- **LSTM (Long Short-Term Memory)** models for time-series prediction
- Dataset sourced from **SAM (System Advisor Model)** for solar/wind/weather data

---

## 🚀 How It Works
1. Users register and connect their energy accounts.
2. Energy usage and generation are tracked via datasets & predictions.
3. AI models forecast energy requirements for upcoming hours/days.
4. Based on supply-demand, the system **dynamically adjusts energy trading prices**.
5. Users can:
   - Sell surplus energy to other users
   - Sell to the grid for extra income
   - Buy energy when demand is high

---

## 📂 Project Structure

---

## ⚡ Setup Instructions
### Prerequisites
- Node.js & npm
- MongoDB
- Python (for AI models)
- Solidity + Ganache/Truffle (for blockchain simulation)

### Steps
1. Clone the repo  
   ```bash
   git clone https://github.com/MannShah312/Energy-Trading-using-Blockchain-and-AI.git
   cd Energy-Trading-using-Blockchain-and-AI
   ```

2. Install dependencies for backend & frontend
    ```bash
    cd server && npm install
    cd ../client && npm install
    ```

3. Run AI models
    ```bash
    cd ai-models
    python train_lstm.py
    python forecast_prophet.py
    ```

4. Start development servers
     ```bash
     # Backend
    cd server
    npm start
    
    # Frontend
    cd client
    npm start
    ```
📊 Demo
-------

👉 [GitHub Repo](https://github.com/MannShah312/Energy-Trading-using-Blockchain-and-AI)\

* * * * *

🤝 Contributing
---------------

Pull requests are welcome! Please fork the repo and submit a PR.

* * * * *

📜 License
----------

This project is licensed under the MIT License.

* * * * *

👨‍💻 Author
------------

**Mann Shah**
