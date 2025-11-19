import json
import os
import time
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
from dotenv import load_dotenv
import itertools

load_dotenv()

# 1. 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
INPUT_FILE = os.path.join(DATA_DIR, 'medical-terms.txt') # 입력 파일 변경
OUTPUT_FILE = os.path.join(DATA_DIR, 'medical_terms_dictionary.jsonl')

# 2. 데이터 로드 함수 (텍스트 파일용)
def load_txt_terms(filename):
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        # 빈 줄 제거하고 리스트로 반환
        return [line.strip() for line in f if line.strip()]

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

# 3. 리스트 청킹 함수
def chunk_list(data_list, chunk_size):
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i:i + chunk_size]

# 4. 후보군 추출 함수
def get_candidates(term: str, db_list: list, type_key: str = 'affix') -> list:
    candidates = []
    term_lower = term.lower()
    for item in db_list:
        keys_to_check = []
        if type_key == 'affix':
            keys_to_check.append(item.get('affix', '').replace('-', ''))
        else:
            keys_to_check.extend([r.replace('-', '') for r in item.get('greek', [])])
            keys_to_check.extend([r.replace('-', '') for r in item.get('latin', [])])
            
        for k in keys_to_check:
            if k and k in term_lower:
                candidates.append(item)
                break 
    return candidates

# 5. 배치 분석 함수
def analyze_batch_with_llm(model, batch_terms, affixes, roots):
    
    batch_input_text = ""
    for term in batch_terms: # batch_terms는 이제 단순 문자열 리스트일 수도 있음
        # 후보군 추출
        affix_cands = get_candidates(term, affixes, 'affix')
        root_cands = get_candidates(term, roots, 'root')
        
        all_candidates = {
            "Affix_Candidates": affix_cands,
            "Root_Candidates": root_cands 
        }
        
        batch_input_text += f"""
        ---
        Target Term: {term}
        All Candidates: {json.dumps(all_candidates, ensure_ascii=False)} 
        ---
        """

    response_schema = {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "term": {"type": "STRING"},
                    "definition": {"type": "STRING"},        # LLM이 생성할 영문 정의
                    "korean_definition": {"type": "STRING"}, # LLM이 생성할 한글 정의
                    "affix_keys": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "root_keys": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "english_explanation": {"type": "STRING"},
                    "korean_explanation": {"type": "STRING"}
                },
                "required": ["term", "definition", "korean_definition", "affix_keys", "root_keys", "english_explanation", "korean_explanation"]
            }
        }

    prompt = f"""
        You are a medical etymology expert. 
        Analyze the following {len(batch_terms)} medical terms.
        
        Input Data:
        {batch_input_text}
        
        Task:
        1. **Generate Definitions:** Since no definition is provided, you MUST generate a precise, standard medical definition for the 'Target Term'.
        2. **Identify Parts:** Identify the parts of the term using the provided 'All Candidates'.
        
        3. **Schema Mapping:**
        - For **'definition'**: Write the English medical definition.
        - For **'korean_definition'**: Provide the Korean term and definition (e.g., "신장염: 신장에 생기는 염증").
        - For **'affix_keys'**: Select values from 'Affix_Candidates'.
        - For **'root_keys'**: Select values from 'Root_Candidates' (greek/latin strings only). 
        
        4. **Explanation Rules:**
        - **Meaning Synthesis:** Explain the etymology using the meanings of affixes and roots.
        - **Connection:** Explicitly explain how the etymology matches the **definition you generated**.
        - **Korean Explanation:** Use Korean language naturally. Avoid mixing English words unless necessary for the term itself.

        5. Return a JSON List containing exactly {len(batch_terms)} objects using the specified schema.
        """
    try:
        response = model.generate_content(
            prompt,
            generation_config=GenerationConfig(
                response_mime_type="application/json",
                response_schema=response_schema
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error analyzing batch: {e}")
        return []

# 6. 메인 실행
def main():
    vertexai.init(project=os.getenv("PROJECT_ID"), location="us-east1")
    model = GenerativeModel("gemini-2.5-flash-lite") 

    print("Loading data...")
    affixes = load_json('affixes.json')
    roots = load_json('roots.json')
    
    # 텍스트 파일 로드 
    terms = load_txt_terms('medical-terms.txt')
    print(f"Loaded {len(terms)} terms from text file.")
    
    # 이미 처리된 데이터 확인
    processed_terms = set()
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    processed_terms.add(data['term'])
                except: pass
    print(f"Already processed: {len(processed_terms)} terms")

    # 처리해야 할 데이터 필터링
    todo_terms = [t for t in terms if t not in processed_terms]
    print(f"Remaining to process: {len(todo_terms)} terms")

    BATCH_SIZE = 20

    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f_out:
        for batch in chunk_list(todo_terms, BATCH_SIZE):
            print(f"Processing batch of {len(batch)} items... ({batch[0]} ...)")
            
            results = analyze_batch_with_llm(model, batch, affixes, roots)
            
            if results:
                for res in results:
                    f_out.write(json.dumps(res, ensure_ascii=False) + "\n")
                    f_out.flush() 
            else:
                print("Skipping batch due to error.")

            time.sleep(1)

    print(f"Done! Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()