# Prompt-generation

🚀 **A data-driven, highly modular desktop application for managing and generating AI prompts.**

Built with Python and PyQt6, this tool features a responsive UI and a modern dark-mode design. It strictly follows the **Separation of Concerns (SoC)** architecture, completely decoupling the core parsing engine, UI rendering, and configuration data.

It provides an intuitive way to manage, randomly sample, and fine-tune AI drawing prompts for tools such as **Stable Diffusion**, **Midjourney**, and more.

---

# ✨ Features

## 📂 Data-Driven Dynamic UI

No hardcoding required. Simply edit the JSON configuration files, and the system will automatically parse and generate a multi-level UI tree.

## 🌊 Responsive Flow Layout

A custom flow layout algorithm ensures tag buttons automatically wrap based on window width, adapting perfectly to any screen size.

## ⚙️ Seamless Weight Adjustment

Click the gear icon (`⚙`) next to any tag to open a frameless floating weight control panel.

Supports:

* Manual keyboard input
* Precise decimal adjustments
* Real-time formatting

Example:

```text
(tag:1.2)
```

## 🎲 Smart Randomized Sampling

Supports both:

* Module-level randomization
* Global random generation

The algorithm is category-aware and avoids logical conflicts between mutually exclusive tags.

Example:

* ✅ "sunrise"
* ❌ "sunrise" + "midnight" simultaneously

## 🌐 Dual-Column Output

The bottom panel displays:

| Left Column             | Right Column         |
| ----------------------- | -------------------- |
| Native Language Preview | Clean English Prompt |

This makes reviewing and copying prompts much easier.

## 🎨 Modern Dark Theme

Deeply customized QSS cyber-style dark theme optimized for long-term usage.

---

# 🛠️ Installation

Make sure you have **Python 3.8+** installed.

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Prompt-generation.git
cd Prompt-generation
```

## 2. Install Dependencies

This project is lightweight and only requires PyQt6.

```bash
pip install PyQt6
```

## 3. Run the Application

```bash
python main.py
```

---

# 🚀 How to Use

## 1. Select Tags

Browse categories and click the tags you want to use.

Selected tags will be highlighted in blue.

---

## 2. Adjust Weights

Click the small `⚙` icon attached to a tag to open the weight adjustment popup.

You can:

* Enter custom values (e.g. `1.2`, `0.8`)
* Use arrow controls
* Automatically format prompt syntax

Example:

```text
(tag:1.2)
```

---

## 3. Randomize Tags

### Module Random

Click:

```text
🎲 随机抽取
```

to randomly sample tags only within the current module.

### Global Random

Click:

```text
🎲 全局一键随机
```

to sample across all expanded modules.

> Collapsed modules are ignored.

---

## 4. Generate Prompt

Click:

```text
🚀 生成提示词
```

The final prompt will instantly appear in the bottom panel.

Copy the English output and paste it into your AI image generator.

---

# 🏗️ Project Structure

```text
Prompt-generation/
├── main.py
│
├── ui/
│   ├── main_window.py
│   ├── flow_layout.py
│   └── components.py
│
├── core/
│   └── parser.py
│
├── data/
│   └── example_landscape.json
│
└── assets/
    └── styles.qss
```

## Structure Overview

| File / Folder       | Description                  |
| ------------------- | ---------------------------- |
| `main.py`           | Application entry point      |
| `ui/`               | UI rendering modules         |
| `flow_layout.py`    | Responsive wrapping layout   |
| `components.py`     | Reusable UI widgets          |
| `core/parser.py`    | Dynamic JSON parser          |
| `data/`             | User prompt libraries        |
| `assets/styles.qss` | Global dark theme stylesheet |

---

# ⚖️ License

This project is licensed under the:

## CC BY-NC 4.0

**Creative Commons Attribution-NonCommercial 4.0 International**

Please see the `LICENSE` file for full legal details.

---

## ✅ You Are Free To

* Share the project
* Copy the code
* Modify the source
* Use for personal or educational purposes
* Create non-commercial derivatives

---

## ❌ You May NOT

* Sell this software
* Bundle it into commercial products
* Use it for enterprise monetization
* Redistribute modified versions commercially

---

## 📝 Attribution Required

You must:

* Give proper credit to the original author
* Include a link to this repository
* Clearly indicate modifications if changes were made

---

# ⚠️ Disclaimer

## "As Is" Basis

This open-source software is provided **"as is"**, without warranty of any kind, express or implied.

The author is not responsible for:

* Stability issues
* Data loss
* Compatibility problems
* Unexpected behavior

---

## Content Responsibility

This tool only assists with prompt generation and management.

Users are solely responsible for:

* Generated prompts
* AI-generated content
* Copyright compliance
* Ethical usage
* Legal responsibility

---

## Legal Compliance

Users must comply with all applicable local laws and regulations.

The author assumes no liability for disputes or damages resulting from misuse of this software.
