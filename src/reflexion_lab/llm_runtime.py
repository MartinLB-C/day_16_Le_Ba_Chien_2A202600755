import json
import time
import os
from dotenv import load_dotenv
from openai import OpenAI
from .schemas import QAExample, JudgeResult, ReflectionEntry
from .prompts import ACTOR_SYSTEM, EVALUATOR_SYSTEM, REFLECTOR_SYSTEM

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY", ""), 
    base_url="https://ws-7z0pgh6qqcnccram.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
)

FAILURE_MODE_BY_QID = {}

def call_llm(messages, temperature=0.0):
    start_time = time.time()
    try:
        response = client.chat.completions.create(
            model="qwen-flash",
            messages=messages,
            temperature=temperature
        )
        latency = int((time.time() - start_time) * 1000)
        content = response.choices[0].message.content
        tokens = response.usage.total_tokens if response.usage else 0
        return content, tokens, latency
    except Exception as e:
        print(f"LLM API Error: {e}")
        return "{}", 0, int((time.time() - start_time) * 1000)

def extract_json(text: str) -> str:
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1:
        return text[start:end+1]
    return "{}"

def actor_answer(example: QAExample, attempt_id: int, agent_type: str, reflection_memory: list[str]) -> tuple[str, int, int]:
    context_str = "\n".join([f"Source: {c.title}\n{c.text}" for c in example.context])
    user_prompt = f"Question: {example.question}\nContext:\n{context_str}\n"
    if reflection_memory:
        user_prompt += "\nMemory from previous failed attempts:\n" + "\n".join(reflection_memory)
        
    messages = [
        {"role": "system", "content": ACTOR_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]
    
    content, tokens, latency = call_llm(messages, temperature=0.7)
    
    ans = content.strip()
    if "Final Answer:" in ans:
        ans = ans.split("Final Answer:")[-1].strip()
    return ans, tokens, latency

def evaluator(example: QAExample, answer: str) -> tuple[JudgeResult, int]:
    user_prompt = f"Question: {example.question}\nGold Answer: {example.gold_answer}\nPredicted Answer: {answer}"
    messages = [
        {"role": "system", "content": EVALUATOR_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]
    content, tokens, _ = call_llm(messages, temperature=0.0)
    json_str = extract_json(content)
    try:
        data = json.loads(json_str)
        return JudgeResult(**data), tokens
    except Exception:
        return JudgeResult(score=0, reason="Failed to parse evaluator response.", missing_evidence=[], spurious_claims=[]), tokens

def reflector(example: QAExample, attempt_id: int, judge: JudgeResult) -> tuple[ReflectionEntry, int]:
    user_prompt = f"Question: {example.question}\nFailure Reason: {judge.reason}\nMissing Evidence: {judge.missing_evidence}"
    messages = [
        {"role": "system", "content": REFLECTOR_SYSTEM},
        {"role": "user", "content": user_prompt}
    ]
    content, tokens, _ = call_llm(messages, temperature=0.0)
    json_str = extract_json(content)
    try:
        data = json.loads(json_str)
        data["attempt_id"] = attempt_id
        return ReflectionEntry(**data), tokens
    except Exception:
        return ReflectionEntry(attempt_id=attempt_id, failure_reason=judge.reason, lesson="Unknown", next_strategy="Try again carefully."), tokens
