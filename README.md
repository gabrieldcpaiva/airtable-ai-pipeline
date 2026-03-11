# 🚀 Airtable AI Pipeline

**Transform your Airtable data into an AI-powered engine with just a few clicks!**

Bridging the gap between your structured data and OpenAI's intelligence, this pipeline allows you to seamlessly process, analyze, and manipulate your Airtable records using Python, Node.js, or Docker. Perfect for beginners and developers alike!

---

## Repository Structure

The repository is organized as follows:

- `src/python`: Python implementation and wrappers.
- `src/node`: Node.js implementation and wrappers.
- `assets`: Project assets.
- `docs`: Documentation.
- `prompts`: AI prompts used in the pipeline.

## ✨ Features

- 🤖 **AI-Powered**: Fully integrated with OpenAI's latest models (like `gpt-4o-mini`).
- ⚡ **Multi-Language Support**: Choose your weapon—Python or Node.js.
- 📦 **Docker Ready**: Deploy instantly without worrying about dependencies.
- 🛠️ **Simple Config**: Just one `.env` file and you're good to go.
- 📊 **Real-time Processing**: Effortlessly manage your Airtable bases.

---

## 🚦 Getting Started

### 📋 Prerequisites

Before you dive in, make sure you have:
1.  **An Airtable Account**: [Sign up here](https://airtable.com) if you haven't already.
2.  **An OpenAI API Key**: Get one from the [OpenAI Dashboard](https://platform.openai.com).
3.  **Your Base ID and Table Name**: Found in your Airtable's API documentation.

### ⚙️ Configuration

1.  **Create your Environment File**:
    Copy the template below into a new file named `.env` in your project root.

    ```.env
    AIRTABLE_API_KEY=your_airtable_api_key
    AIRTABLE_BASE_ID=your_base_id
    AIRTABLE_TABLE_NAME=your_table_name
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_MODEL=gpt-4o-mini
    LOG_LEVEL=info
    ```

    > **💡 Pro Tip**: Never share your `.env` file! We've included a `.gitignore` to help keep your keys safe.

---

## 🚀 Quickstart Instructions

### 🐍 Python
```bash
cd src/python
pip install airtable-python-wrapper==0.15.3
pip install -r requirements.txt
```

### 🟢 Node.js
```bash
cd src/node
npm install airtable@0.12.2
npm install
```

### 🐳 Docker
```bash
docker pull gabrieldcpaiva/airtable-ai-pipeline:<version>
```

---

## 🛠️ How It Works

This pipeline connects to your specified Airtable table, fetches records, and uses OpenAI's models to perform intelligent transformations based on your requirements. It’s designed to be modular and scalable, whether you're building a small automation or a large-scale AI application.

---

## 📺 Demo & Output

### Example Output
![](example-output.png)

---

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest enhancements.

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
