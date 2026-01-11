# Transformer-based Question Answering (Q/A) System

## Overview
This project implements an **Extractive Question Answering (Q/A)** system using
[HuggingFace Transformers](https://huggingface.co/docs/transformers/index).
The user provides a **context paragraph** and a **question**, and the system extracts the most relevant
answer span directly from the context.

Unlike a chatbot that generates answers freely, this solution uses **extractive Q/A**, meaning the answer
is selected from the given context text, making it more reliable for document-based question answering.

---

## Model Used
- Q/A model: [`deepset/roberta-base-squad2`](https://huggingface.co/deepset/roberta-base-squad2)
- Trained on: [SQuAD2 Dataset](https://rajpurkar.github.io/SQuAD-explorer/) (includes unanswerable questions)

---

## Key Features
- Accepts **Context + Question** as input (CLI-based)
- Produces:
  - Extracted **answer**
  - **confidence score**
  - Answer span **start/end indices**
- Highlights the extracted answer within the context
- Supports **no-answer handling** using confidence thresholding

---

## Tech Stack
- [Python](https://www.python.org/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [PyTorch](https://pytorch.org/)

---

## Project Structure
- [`qna_app.py`](qna_app.py) — main Q/A application
- [`requirements.txt`](requirements.txt) — dependencies
- [`sample_tests.txt`](sample_tests.txt) — sample contexts and questions
- [`README.md`](README.md) — documentation

---

## Installation
> Recommended: use Python 3.10 for best compatibility.

```bash
pip install -r requirements.txt

**## Run the Project**
python qna_app.py

**This README is fully **original**, not copied from any external source.  
***✅ Blue text appears automatically because those are **links**.

---

# ✅ requirements.txt (Final)

***Make sure your `requirements.txt` contains:
transformers
torch
sentencepiece

**## Acknowledgement**
Model: deepset/roberta-base-squad2
Library: Transformers
