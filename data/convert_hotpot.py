import json
import os

input_file = r"D:\VIn_GD2\track3\phase1-track3-lab1-advanced-agent-main\day_16_Le_Ba_Chien_2A202600755\data\hotpot_dev_distractor_v1_100.json"
output_file = r"D:\VIn_GD2\track3\phase1-track3-lab1-advanced-agent-main\day_16_Le_Ba_Chien_2A202600755\data\hotpot_dev_distractor_v1_100_formatted.json"

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

formatted_data = []
for item in data:
    # Handle both new formatted items and raw HotpotQA items
    if "_id" in item:
        formatted_item = {
            "qid": item["_id"],
            "difficulty": item.get("level", "medium"),
            "question": item["question"],
            "gold_answer": item["answer"],
            "context": [
                {
                    "title": ctx[0],
                    "text": " ".join(ctx[1]) if isinstance(ctx[1], list) else ctx[1]
                }
                for ctx in item["context"]
            ]
        }
        formatted_data.append(formatted_item)
    else:
        formatted_data.append(item)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, indent=2, ensure_ascii=False)

print(f"Successfully formatted {len(formatted_data)} items and saved to {output_file}")
