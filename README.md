# Prompt-generation

🚀 **A data-driven, highly modular desktop application for managing and generating AI prompts.** Built with Python and PyQt6, this tool features a responsive UI and a modern dark mode design. It strictly follows the **Separation of Concerns (SoC)** architecture, completely decoupling the core parsing engine, UI rendering, and configuration data. It provides an intuitive way to manage, randomly sample, and fine-tune AI drawing prompts (for tools like Stable Diffusion, Midjourney, etc.).

## ✨ Features

* **📂 Data-Driven Dynamic UI**: No hardcoding required. Simply edit the JSON configuration files, and the system will automatically parse and generate a multi-level UI tree.
* **🌊 Responsive Flow Layout**: Custom flow layout algorithm ensures tag buttons automatically wrap based on window width, adapting perfectly to any screen size.
* **⚙️ Seamless Weight Adjustment**: Click the gear icon (`⚙`) next to any tag to bring up a frameless, floating weight control panel. Supports manual keyboard input for precise adjustments.
* **🎲 Smart Randomized Sampling**: Supports both module-level and global randomization. The algorithm is category-aware, perfectly avoiding logical conflicts between mutually exclusive tags (e.g., sampling both "noon" and "midnight" simultaneously).
* **🌐 Dual-Column Output**: The bottom panel displays both a "Native Language Preview" (with weights) and a "Clean English Prompt" side-by-side, making it easy to review and copy.
* **🎨 Modern Dark Theme**: Deeply customized QSS dark cyber-theme, easy on the eyes for extended use.

## 🛠️ Installation

Make sure you have Python 3.8 or higher installed on your system.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Prompt-generation.git](https://github.com/YOUR_USERNAME/Prompt-generation.git)
   cd Prompt-generation

2.Install dependencies:
This project is lightweight and only requires PyQt6.
  pip install PyQt6
  
3.Run the application:
  python main.py

🚀 How to Use
Select Tags: Browse the categories and click on the tags you want to use. Selected tags will be highlighted in blue.

Adjust Weights: Click the small ⚙ icon attached to a tag to open the weight adjustment popup. Enter a value (e.g., 1.2 or 0.8) or use the up/down arrows. The UI will format it automatically as (tag:1.2).

Randomize:

Click "🎲 随机抽取" (Random Pick) on a specific module to randomly sample tags just from that category.

Click the large "🎲 全局一键随机" (Global Random) button at the bottom to sample tags across all currently expanded modules. (Collapsed modules are ignored).

Generate: Click "🚀 生成提示词" (Generate Prompt). The bottom panel will instantly display your final prompt. Copy the text from the right column and paste it into your AI image generator.

🏗️ Project Structure
The project follows a strict modular design:
Prompt-generation/
├── main.py                # Application entry point and initialization
├── ui/                    # UI rendering modules
│   ├── main_window.py     # Main window and dual-column layout
│   ├── flow_layout.py     # Custom responsive wrapping layout
│   └── components.py      # Reusable widgets (WeightPopup, TagWidget, ModuleGroupWidget)
├── core/                  # Core logic and parsers
│   └── parser.py          # Dynamic data parser (JSON to memory tree)
├── data/                  # User data directory
│   └── example_landscape.json # Example prompt library
└── assets/                # Static resources
    └── styles.qss         # Global dark theme stylesheet

⚖️ License
This project is licensed under the CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International) License.
Please see the LICENSE file in the root directory for the full legal text.

In plain English:

✅ You are free to: Share, copy, and modify the code for personal, educational, or non-commercial purposes.

❌ You may NOT: Use this project or its derivatives for any commercial purposes (e.g., selling it, bundling it with paid software, or using it for enterprise monetization).

📝 You must: Give appropriate credit to the original author and provide a link to this repository.

⚠️ Disclaimer
"As Is" Basis: This open-source tool is provided "as is", without warranty of any kind, express or implied. The author is not responsible for absolute stability or data security.

Content Responsibility: This tool only facilitates the concatenation and management of text prompts. The user assumes all copyright, legal, and ethical responsibilities for the prompts generated and the subsequent content (images/text) produced by AI models using these prompts.

Legal Compliance: Users must comply with local laws and regulations. The author assumes no liability for any legal disputes arising from the misuse of this software.
