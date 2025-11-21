# Medical Term Relations with Affixes and Roots
---

A curated dataset for premed and nursing students

## Abstract

Memorizing medical terminology is a core task for many pre-medical and nursing students. While definitions are easy to look up, understanding why a term means what it means—through its affixes and roots—greatly improves memorization, grouping, and long-term retention.

This dataset links medical terms with their relevant prefixes, roots, and suffixes, accompanied by both English and Korean explanations. The relationships were generated automatically using Gemini-2.5-lite based on affix/root lists. The medical term list was fetched from the open-source repository below:

🔗 https://github.com/glutanimate/wordlist-medicalterms-en

The full dataset is stored as a .jsonl file. Each entry follows this format:

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

## How to use

#### Quizlet(For Korean)

Download the file from this path.

```
/data/quizlet/medical_terms.csv
```

Select the terms and make a new vocabulary set. Use ',' as a seperator.

<img width="1406" height="698" alt="image" src="https://github.com/user-attachments/assets/3cf95f0b-dcf8-4ef8-8f38-c9faa35ad7da" />


#### Anki(For both ko/en)
Download the file from this path. 
*(For korean users, select data/anki/medical_terms_ko.apkg )*
```
/data/anki/medical_terms_en.apkg
```
Import the apkg file in Anki.

<img width="638" height="377" alt="image" src="https://github.com/user-attachments/assets/6444fa76-59f4-4c57-a2bf-563ccec1e952" />


---

## Future Works

- **Web-based medical vocabulary learning & exam management service**

Build a web application on top of this dataset that helps students memorize medical terms more efficiently by grouping them via shared affixes and roots.

**Features**

- Custom quizzes based on topic, course, or exam date

- “Jokbo” (past exam / frequently-tested term) management linked to the term database

- Progress tracking, spaced repetition, and error history per user

- **Long-term goal**: provide an integrated platform where premed and nursing students can manage their term lists, past tests, and daily study schedule in one place.

---

### Disclaimer

This dataset is provided as-is, with no warranties or guarantees.
If you find errors or inconsistencies, please open an issue or submit a pull request. Or if you want more features notice me any time.
