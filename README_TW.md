# Prompt-generation 🎨 極簡使用指南

Prompt-generation 是一款專為 AI 圖像生成工作流程（Stable Diffusion、Midjourney、FLUX 等）打造的輕量級桌面工具。

不再需要使用雜亂的文字檔或試算表來管理提示詞。透過直觀的點選式介面，你可以高效率地組織、編輯與生成提示詞，完全無需撰寫程式碼。

## 🚀 快速開始

### 第一步：下載與執行

**一般使用者（推薦）**

從 GitHub Releases 頁面下載最新的 `.zip` 壓縮檔，解壓縮後直接執行 `PromptGenerator.exe`。

**開發者**

需要 Python 3.8 或更新版本。

```bash
pip install PyQt6
python main.py
```

### 第二步：選擇標籤與調整權重

#### 載入詞庫

軟體內建預設提示詞庫。

你也可以透過：

`File → Load Library...`

載入自己的 JSON 詞庫。

#### 選擇標籤

瀏覽不同分類，點擊你想加入提示詞的標籤。

#### 調整權重

點擊標籤旁的 ⚙ 圖示即可快速調整權重。

例如：

```text
(masterpiece:1.3)
```

#### 自訂提示詞

使用「Custom Prompts」欄位輸入臨時想到的提示詞或修飾內容。

### 第三步：靈感模式

當你沒有靈感時，點擊：

🎲 Global Random

軟體會在獨立的靈感框中產生一組隨機組合，而不會影響目前已選取的內容。

如果你喜歡這組結果，點擊：

✨ Apply Inspiration

即可立即套用到目前的選擇。

### 第四步：生成與複製

點擊：

🚀 Generate Prompt

軟體會顯示：

* 方便檢查的本地語言預覽
* 可直接用於 AI 生成的英文提示詞

接著點擊：

📋 Copy English

即可直接貼到你喜愛的 AI 繪圖工具中使用。

## 💡 進階技巧

### 視覺化詞庫編輯器

按下：

```text
Ctrl + E
```

即可開啟視覺化詞庫編輯器。

你可以透過類似試算表的介面建立分類、整理提示詞以及編輯詞庫，完全不需要手動修改 JSON 檔案。

### 個人化設定

本軟體支援：

* 多語言使用者介面
* 即時語言切換
* 三套內建主題

  * Dark Cyber
  * Light Minimal
  * Dracula Purple
