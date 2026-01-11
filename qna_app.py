from transformers import pipeline
import textwrap

# If score is less than this threshold => treat as "No Answer"
NO_ANSWER_THRESHOLD = 0.25


def highlight_answer(context: str, start: int, end: int) -> str:
    """Highlights predicted answer span inside context."""
    if start < 0 or end < 0 or start >= len(context) or end > len(context):
        return context
    return context[:start] + " [ANSWER: " + context[start:end] + "] " + context[end:]


def format_and_print(result: dict, context: str):
    answer = result.get("answer", "")
    score = float(result.get("score", 0.0))
    start = int(result.get("start", -1))
    end = int(result.get("end", -1))

    print("\n" + "=" * 70)
    print("📌 QUESTION ANSWERING RESULT")
    print("=" * 70)

    # No-answer handling
    if answer.strip() == "" or answer.strip().lower() in ["no answer", ""]:
        answer = "No Answer"
    if score < NO_ANSWER_THRESHOLD:
        print("⚠️  No confident answer found in the context.")
        print(f"Confidence : {score * 100:.2f}%")
        print("=" * 70 + "\n")
        return

    print(f"Answer     : {answer}")
    print(f"Confidence : {score * 100:.2f}%")
    print(f"Span       : start={start}, end={end}")

    highlighted = highlight_answer(context, start, end)

    print("\n" + "-" * 70)
    print("🧾 CONTEXT WITH HIGHLIGHTED ANSWER")
    print("-" * 70)
    print("\n".join(textwrap.wrap(highlighted, width=95)))
    print("=" * 70 + "\n")


def main():
    print("\n========== Q/A System using Transformers (RoBERTa SQuAD2) ==========\n")

    context = input("Enter CONTEXT:\n> ").strip()
    if not context:
        print("\n❌ Context cannot be empty.")
        return

    question = input("\nEnter QUESTION:\n> ").strip()
    if not question:
        print("\n❌ Question cannot be empty.")
        return

    print("\n⏳ Loading Transformer Q/A model...")
    qa = pipeline("question-answering", model="deepset/roberta-base-squad2")
    print("✅ Model loaded successfully.")

    print("\n⏳ Generating answer...")
    result = qa(question=question, context=context)

    format_and_print(result, context)


if __name__ == "__main__":
    main()
