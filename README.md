# Transformer-based Question Answering (Q/A) System

## Overview
This project implements an **Extractive Question Answering (Q/A)** system using the
[HuggingFace Transformers](https://huggingface.co/docs/transformers/index) library.
The user provides a **context paragraph** and a **question**, and the system extracts the most relevant answer
span directly from the context.

This approach uses **extractive Q/A** (answers are selected from the given context), which is reliable for
document-based question answering systems.

---

## Model Used
- Model: [`deepset/roberta-base-squad2`](https://huggingface.co/deepset/roberta-base-squad2)
- Dataset: [SQuAD2](https://rajpurkar.github.io/SQuAD-explorer/) (includes unanswerable questions)

---

## Key Features
- CLI-based input: **Context + Question**
- Outputs:
  - Extracted **Answer**
  - **Confidence score**
  - Answer span **start/end indices**
- Highlights the extracted answer inside the context
- Supports **No-answer handling** using confidence thresholding

---

## Tech Stack
- [Python](https://www.python.org/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [PyTorch](https://pytorch.org/)

---

## Project Structure
- [`qna_app.py`](qna_app.py) — main application
- [`requirements.txt`](requirements.txt) — dependencies
- [`sample_tests.txt`](sample_tests.txt) — sample test cases
- [`README.md`](README.md) — documentation

---

## Installation
> Recommended: use **Python 3.10** for best compatibility.

```bash
pip install -r requirements.txt
