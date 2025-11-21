# Medical Term Relations with Affixes and Roots
---

A curated dataset for premed and nursing students

### Abstract

Memorizing medical terminology is a core task for many pre-medical and nursing students. While definitions are easy to look up, understanding why a term means what it means—through its affixes and roots—greatly improves memorization, grouping, and long-term retention.

This dataset links medical terms with their relevant prefixes, roots, and suffixes, accompanied by both English and Korean explanations. The relationships were generated automatically using Gemini-2.5-lite based on affix/root lists and the medical term list from the open-source repository below:

🔗 https://github.com/glutanimate/wordlist-medicalterms-en

Generation code is available in:
/scripts/generate_dict.py

The dataset is stored as a .jsonl file. Each entry follows this format:
``` json
{
    "term": "abetalipoproteinemia",
    "definition": "...",
    "korean_definition": "...",
    "affix_keys": ["ab-", "-al", "-emia"],
    "root_keys": [],
    "english_explanation": "...",
    "korean_explanation": "..."
}
```

---

### File Structure

```
├── README.md
├── data
│   ├── affixes.json
│   ├── medical-terms.txt
│   ├── medical_terms_dictionary.jsonl
│   └── roots.json
├── requirements.txt
└── scripts
    └── generate_dict.py
```
---

### Future Work

- **Flashcard export (Anki / Quizlet compatible formats)**

    - Provide scripts to convert medical_terms_dictionary.jsonl into formats that can be directly imported into tools like Anki and Quizlet (e.g., CSV, TSV, or custom note types).

    - Allow users to select which fields to include (term, definition, Korean definition, affixes/roots, explanations, etc.) so they can build personalized decks for their own study style.

- **Web-based medical vocabulary learning & exam management service**

    - Build a web application on top of this dataset that helps students memorize medical terms more efficiently by grouping them via shared affixes and roots.

    - Support features such as:

    - Custom quizzes based on topic, course, or exam date

    - “Jokbo” (past exam / frequently-tested term) management linked to the term database

    - Progress tracking, spaced repetition, and error history per user

- **Long-term goal**: provide an integrated platform where premed and nursing students can manage their term lists, past tests, and daily study schedule in one place.

---

### Disclaimer

This dataset is provided as-is, with no warranties or guarantees.
If you find errors or inconsistencies, please open an issue or submit a pull request.