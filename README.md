# Prompt-generation 🎨

## Screenshot
<img width="1184" height="815" alt="image" src="https://github.com/user-attachments/assets/58dd6a8d-432f-4e9c-9c2c-f794bc6775df" />
<img width="1146" height="803" alt="image" src="https://github.com/user-attachments/assets/0c20b248-445a-4c0b-a27c-f322af01c143" />



🚀 **A data-driven, highly modular desktop application for managing and generating AI prompts.**

Built with Python and PyQt6, Prompt-generation provides an intuitive and efficient way to manage, randomize, customize, and generate prompts for AI image generation tools such as Stable Diffusion, Midjourney, FLUX, and more.

The project follows a strict **Separation of Concerns (SoC)** architecture, fully decoupling data parsing, UI rendering, configuration management, and business logic for maintainability and extensibility.

---

## 📸 Overview

Prompt-generation is designed for creators who frequently work with AI-generated content and need a powerful prompt management system.

Features include:

* Dynamic JSON-driven prompt libraries
* Smart random prompt generation
* Multi-language support
* Theme switching
* Prompt weight adjustment
* One-click prompt copying
* Inspiration workflow without destroying current selections

---

## ✨ Features

### 📂 Data-Driven Dynamic UI

No hardcoded categories or tags.

Simply edit your JSON library files and the application will automatically generate:

* Module groups
* Subcategories
* Tag buttons
* Dynamic layouts

without any code modifications.

---

### 🌊 Responsive Flow Layout

Custom Flow Layout implementation that automatically wraps tag buttons according to window size.

Benefits:

* Perfect scaling on different resolutions
* Better usability on small screens
* Smooth responsive experience

---

### ⚙️ Advanced Weight Adjustment

Each tag contains an integrated weight editor.

Click the ⚙ button to:

* Adjust weights precisely
* Input decimal values manually
* Modify prompt strength in real time

Example:

```text
(lush forest:1.2)
(masterpiece:1.4)
```

---

### 🎲 Smart Random Generation

Supports two independent randomization modes:

#### Module Random

Randomly select tags within a single category.

#### Global Random

Generate a complete prompt combination from all expanded modules.

The algorithm intelligently avoids conflicting selections whenever possible.

Example:

```text
✓ sunrise
✗ sunrise + midnight
```

---

### 💡 Non-Destructive Inspiration Workflow

Traditional random generation usually destroys your current selection.

Prompt-generation introduces an Inspiration Mode:

1. Click **🎲 Global Random**
2. Generate a temporary prompt draft
3. Review the generated result
4. Click **✨ Apply Inspiration** if satisfied

Your current work remains untouched until explicitly applied.

---

### 🌐 Multi-Language Support

Built-in internationalization (i18n).

Switch languages instantly without restarting:

* 🇺🇸 English
* 🇨🇳 Simplified Chinese
* 🇯🇵 Japanese

All menus, buttons, and interface text update dynamically.

---

### 🎨 Dynamic Theme Engine

Multiple built-in themes are available:

| Theme          | Description                    |
| -------------- | ------------------------------ |
| Dark Cyber     | Modern dark cyberpunk style    |
| Light Minimal  | Clean and lightweight          |
| Dracula Purple | Popular purple developer theme |

Themes can be switched instantly through the menu bar.

---

### 📋 Dual-Column Prompt Output

Generated prompts are displayed in two synchronized columns:

| Column         | Description                      |
| -------------- | -------------------------------- |
| Native Preview | Human-readable localized content |
| English Prompt | Clean AI-ready prompt            |

Perfect for reviewing before generation.

---

### 📌 One-Click Copy

Copy the generated English prompt directly to your clipboard.

Features:

* Instant feedback
* Status bar notification
* Ready for Stable Diffusion, Midjourney, FLUX, ComfyUI, Forge, WebUI, etc.

---

## 🛠️ Installation

### Requirements

* Python 3.8+
* PyQt6

---

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Prompt-generation.git
cd Prompt-generation
```

---

### Install Dependencies

```bash
pip install PyQt6
```

---

### Run

```bash
python main.py
```

---

## 🚀 Usage Guide

### 1. Load a Prompt Library

The application loads:

```text
example_landscape.json
```

by default.

To load a custom library:

```text
File → Load Library...
```

or

```text
Ctrl + O
```

The interface will rebuild automatically.

---

### 2. Select Prompt Tags

Browse categories and click tags to activate them.

Selected tags are highlighted automatically.

---

### 3. Adjust Weights

Click:

```text
⚙
```

next to any tag.

Examples:

```text
(masterpiece:1.3)
(high quality:1.2)
```

---

### 4. Generate Inspiration

Click:

```text
🎲 Global Random
```

A temporary prompt combination will appear in the Inspiration Box.

Current selections remain unchanged.

If satisfied:

```text
✨ Apply Inspiration
```

to replace current selections.

---

### 5. Generate Prompt

Click:

```text
🚀 Generate Prompt
```

The output panel updates immediately.

---

### 6. Copy Prompt

Click:

```text
📋 Copy English
```

The prompt is copied directly to your clipboard.

---

### 7. Personalize Your Workspace

#### Change Language

```text
Settings → Language
```

Available:

* English
* 简体中文
* 日本語

#### Change Theme

```text
Theme
```

Available:

* Dark Cyber
* Light Minimal
* Dracula Purple

---

## 🏗️ Project Structure

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
│   ├── parser.py
│   └── config_manager.py
│
├── data/
│   └── example_landscape.json
│
└── assets/
    ├── i18n_en.json
    ├── i18n_zh.json
    ├── i18n_ja.json
    ├── theme_dark.qss
    ├── theme_light.qss
    └── theme_dracula.qss
```

---

## 📝 Custom Library Format

Example:

```json
{
  "project_name": "My Custom Library",
  "module_groups": [
    {
      "module_name": "Lighting & Time",
      "is_open": true,
      "sub_modules": [
        {
          "sub_module_name": "Time of Day",
          "tags": {
            "Dawn": "dawn",
            "Midnight": "midnight"
          }
        }
      ]
    }
  ]
}
```

---

## ⚖️ License

This project is licensed under:

### CC BY-NC 4.0

Creative Commons Attribution-NonCommercial 4.0 International

See the LICENSE file for complete legal details.

### ✅ You May

* Share the project
* Modify the source code
* Create derivative works
* Use for personal learning
* Use for non-commercial purposes

### ❌ You May Not

* Sell this software
* Bundle it into commercial products
* Use it for commercial monetization
* Redistribute commercially modified versions

### 📝 Attribution Required

You must:

* Credit the original author
* Include a link to this repository
* Clearly indicate modifications

---

## ⚠️ Disclaimer

### As-Is Basis

This software is provided "as is" without warranties of any kind.

The author is not responsible for:

* Data loss
* Compatibility issues
* Stability problems
* Unexpected behavior

---

### Content Responsibility

Users are solely responsible for:

* Generated prompts
* AI-generated content
* Copyright compliance
* Ethical use
* Legal consequences

---

### Legal Compliance

Users must comply with all applicable laws and regulations.

The author assumes no liability for damages or disputes arising from the use or misuse of this software.
