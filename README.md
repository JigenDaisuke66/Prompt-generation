# Prompt-generation 🎨

## Screenshot
<img width="1184" height="815" alt="image" src="https://github.com/user-attachments/assets/58dd6a8d-432f-4e9c-9c2c-f794bc6775df" />
<img width="1146" height="803" alt="image" src="https://github.com/user-attachments/assets/0c20b248-445a-4c0b-a27c-f322af01c143" />
<img width="1186" height="819" alt="动画" src="https://github.com/user-attachments/assets/f15d4bf4-ff56-4e63-8b3b-eb14ff3cee9c" />

# Prompt-generation

🌍 Documentation

| Language | Link |
|-----------|------|
| 🇺🇸 English | [README](README.md) |
| 🇨🇳 简体中文 | [README_CN.md](README_CN.md) |
| 🇹🇼 繁體中文 | [README_TW.md](README_TW.md) |
| 🇯🇵 日本語 | [README_JP.md](README_JP.md) |
| 🇩🇪 Deutsch | [README_DE.md](README_DE.md) |
| 🇷🇺 Русский | [README_RU.md](README_RU.md) |
# Prompt-generation 🎨 Quick Start Guide

Prompt-generation is a lightweight desktop tool designed for AI image generation workflows (Stable Diffusion, Midjourney, FLUX, and more).

Instead of managing prompts in messy text files or spreadsheets, it provides an intuitive point-and-click interface for organizing, editing, and generating prompts efficiently—without coding.

## 🚀 Getting Started

### Step 1: Download & Run

**For most users (recommended)**

Download the latest `.zip` package from the GitHub Releases page, extract it, and launch `PromptGenerator.exe`.

**For developers**

Requires Python 3.8+.

```bash
pip install PyQt6
python main.py
```

### Step 2: Select Tags & Adjust Weights

**Load a library**

A default prompt library is included. You can also load your own JSON library through:

`File → Load Library...`

**Select tags**

Browse categories and click any tags you want to include in your prompt.

**Adjust weights**

Click the ⚙ icon next to a tag to quickly adjust its weight.

Example:

```text
(masterpiece:1.3)
```

**Custom prompts**

Use the "Custom Prompts" field to add temporary ideas or modifiers.

### Step 3: Inspiration Mode

When you're out of ideas, click:

🎲 Global Random

The application generates a random combination inside a separate Inspiration Box without affecting your current selections.

If you like the result, click:

✨ Apply Inspiration

to instantly replace the current selection.

### Step 4: Generate & Copy

Click:

🚀 Generate Prompt

The application displays:

* A localized preview for easy review
* A clean English prompt for AI generation

Then click:

📋 Copy English

and paste it directly into your favorite AI image generator.

## 💡 Advanced Tips

### Visual Library Editor

Press:

```text
Ctrl + E
```

to open the Visual Library Editor.

Create categories, organize prompts, and edit libraries through a spreadsheet-like interface instead of manually editing JSON files.

### Personalization

The application supports:

* Multiple UI languages
* Instant language switching
* Three built-in themes:

  * Dark Cyber
  * Light Minimal
  * Dracula Purple
