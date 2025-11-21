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

#### Quizlet

Download the file from this path.

```
/data/quizlet/medical_terms.csv
```
Import the csv file in Quizlet.

#### Anki
Download the file from this path. 
*(For korean users, select data/anki/medical_terms_ko.apkg )*
```
/data/anki/medical_terms_en.apkg
```
Import the apkg file in Anki.

---

## Future Works

- **Web-based medical vocabulary learning & exam management service**

    - [ ] Build a web application on top of this dataset that helps students memorize medical terms more efficiently by grouping them via shared affixes and roots.

    - [ ] Support features such as:

    - [ ] Custom quizzes based on topic, course, or exam date

    - [ ] “Jokbo” (past exam / frequently-tested term) management linked to the term database

    - [ ] Progress tracking, spaced repetition, and error history per user

- **Long-term goal**: provide an integrated platform where premed and nursing students can manage their term lists, past tests, and daily study schedule in one place.

---

### Disclaimer

This dataset is provided as-is, with no warranties or guarantees.
If you find errors or inconsistencies, please open an issue or submit a pull request. Or if you want more features notice me any time.
