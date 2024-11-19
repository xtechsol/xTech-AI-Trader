# xTech AI Trader

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

`xTech` is an AI-powered tool designed to assist cryptocurrency traders by identifying new cryptocurrencies through analysis, executing trades via integration with `pump.fun` and managing transactions through the Phantom wallet on the Solana blockchain. It also tweets about its trading activities.

## Features

- **LLM Analysis:** Uses a Large Language Model to analyze market trends, news, and social sentiment.
- **Twitter Integration:** Automatically posts about tokens being purchased or analyzed.
- **Web3 Integration:** Connects to Phantom wallet for seamless trading on the Solana network.
- **Pump.Fun Integration:** Interacts with the `pump.fun` platform for discovering and potentially launching new meme coins.

## Getting Started

### Prerequisites

- Python 3.8+
- Solana Phantom wallet setup

### Installation

git clone [git@github.com:yourusername/xTech-AI-Trader.git](https://github.com/xtechsol/xTech-AI-Trader/edit/main/README.md)
cd xTech-AI-Trader

xTech-AI-Trader/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── xtech/
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── twitter_integration.py
│   │   ├── web3_integration.py
│   │   └── pump_fun.py
│   └── main.py
├── data/
│   └── sample_tweets.json
└── tests/
    ├── __init__.py
    └── test_xtech.py
