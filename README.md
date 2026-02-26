# Project Overview

This project provides an interface to Airtable's API, enabling easy access and manipulation of your Airtable data from Python, Node.js, or Docker environments.

## Demo

[Demo Link](#)

## Quickstart Instructions

### Python
```bash
pip install airtable-python-wrapper
```

### Node
```bash
npm install airtable
```

### Docker
```bash
docker pull gabrieldcpaiva/airtable-ai-pipeline
```

## Example Output

![](example-output.png)

## Configuration

You can create a `.env` file using the following template:
```.env
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_base_id
AIRTABLE_TABLE_NAME=your_table_name
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
LOG_LEVEL=info
```

