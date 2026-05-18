# 🪙 Coin Flip Probability Simulator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Project Status">
</p>

---

## 🚀 Overview

The **Coin Flip Probability Simulator** is a lightweight Python tool designed to test the Law of Large Numbers. By simulating thousands (or even millions) of coin flips, it demonstrates how results converge toward a 50-50 distribution.

> "In the long run, we are all dead... but the coin flips will always be 50-50." 🪙

---

## ✨ Features

- 🎯 **High Precision:** Calculates percentages up to two decimal places.
- ⚡ **Lightning Fast:** Simulates thousands of flips in milliseconds.
- 📊 **Insightful Analysis:** Automatically calculates the deviation from the theoretical 50-50 split.
- 💻 **Simple CLI:** User-friendly command-line interface.

---

## 🛠️ Installation

This project uses [uv](https://github.com/astral-sh/uv) for lightning-fast dependency management.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/coin-flips.git
   cd coin-flips
   ```

2. **Install dependencies (if any):**
   ```bash
   uv sync
   ```

---

## 🎮 Usage

Run the simulator directly using `uv`:

```bash
uv run main.py
```

### 📝 Example Output

```text
--- Coin Flip Probability Simulator ---
This program tests the theory that flipping a coin many times results in a 50-50 distribution.

Enter the number of times you want to flip the coin: 1000

Flipping the coin 1000 times...

--- Results ---
Heads: 512 (51.20%)
Tails: 488 (48.80%)
Total: 1000

Difference from 50-50: 1.20%
The results are quite close to the 50-50 theory!
```

---

## 🎨 Visualization

While this is a CLI tool, you can imagine the magic happening:

<p align="center">
  <pre>
     _______
    /       \
   /   HEADS \
  |     🪙    |
   \   TAILS /
    \_______/
  </pre>
  <i>"Flip it until you make it."</i>
</p>

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Made with ❤️ by Gemini CLI
</p>
