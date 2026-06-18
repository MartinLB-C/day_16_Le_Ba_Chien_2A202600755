import json

def generate_data():
    with open('data/hotpot_mini.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    new_data = []
    # We have 8 records. Repeat them to get at least 100 (e.g. 13 times = 104)
    for i in range(13):
        for item in data:
            new_item = item.copy()
            new_item['qid'] = f"{item['qid']}_{i}"
            new_data.append(new_item)
            
    with open('data/test_100.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
        
    print(f"Generated {len(new_data)} records in data/test_100.json")

if __name__ == "__main__":
    generate_data()
