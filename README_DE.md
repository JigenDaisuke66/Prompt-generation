# Prompt-generation 🎨 クイックスタートガイド

Prompt-generation は、Stable Diffusion、Midjourney、FLUX などの AI画像生成ツール向けに開発された軽量デスクトップアプリです。

複雑なテキストファイルやスプレッドシートの代わりに、直感的なGUIでプロンプトを管理・編集・生成できます。

## 🚀 はじめに

### ステップ 1: ダウンロードと起動

**一般ユーザー向け**

GitHub Releases から最新の `.zip` ファイルをダウンロードし、解凍後に `PromptGenerator.exe` を実行してください。

**開発者向け**

Python 3.8 以上が必要です。

```bash
pip install PyQt6
python main.py
```

### ステップ 2: タグ選択と重み調整

* デフォルトのライブラリが付属しています。
* `File → Load Library...` から独自の JSON ライブラリを読み込めます。
* 必要なタグをクリックして選択します。
* ⚙ ボタンから重みを調整できます。

例:

```text
(masterpiece:1.3)
```

* 一時的な追加プロンプトは「Custom Prompts」に入力できます。

### ステップ 3: インスピレーションモード

アイデアが欲しいときは:

🎲 Global Random

をクリックしてください。

現在の選択内容を変更せずに、別枠のインスピレーションボックスへランダムな組み合わせを生成します。

気に入った場合は:

✨ Apply Inspiration

をクリックして適用できます。

### ステップ 4: プロンプト生成

🚀 Generate Prompt

をクリックすると、

* 確認用のローカライズ表示
* AI向け英語プロンプト

が表示されます。

📋 Copy English

をクリックすると、そのままコピーできます。

## 💡 上級者向けヒント

### ビジュアルライブラリエディタ

```text
Ctrl + E
```

でエディタを開けます。

JSON を直接編集することなく、カテゴリやプロンプトをGUI上で管理できます。

### カスタマイズ

対応機能:

* 多言語UI
* 即時言語切り替え
* 3種類のテーマ

  * Dark Cyber
  * Light Minimal
  * Dracula Purple
