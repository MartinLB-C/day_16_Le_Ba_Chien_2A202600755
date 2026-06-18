import json
import os

input_file = r"D:\VIn_GD2\track3\phase1-track3-lab1-advanced-agent-main\day_16_Le_Ba_Chien_2A202600755\data\hotpot_dev_distractor_v1.json"
output_file = r"D:\VIn_GD2\track3\phase1-track3-lab1-advanced-agent-main\day_16_Le_Ba_Chien_2A202600755\data\hotpot_dev_distractor_v1_100.json"

if not os.path.exists(input_file):
    print(f"Error: File not found: {input_file}")
    exit(1)

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Original data type: {type(data)}")
if isinstance(data, list):
    print(f"Total records: {len(data)}")
    sampled_data = data[:100]
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sampled_data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(sampled_data)} samples to {output_file}")
else:
    print(f"Unexpected data type. Expected list but got {type(data)}.")
    if isinstance(data, dict):
        print(f"Keys: {list(data.keys())[:5]}")
