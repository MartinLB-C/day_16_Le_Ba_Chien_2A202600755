# Reflexion Agent Lab - Đã Hoàn Thiện

## Tổng quan

Dự án này triển khai kiến trúc **Reflexion Agent** sử dụng mô hình LLM thực tế (hiện tại đang sử dụng mô hình họ Qwen qua API của Aliyun DashScope) thay vì mock data. Reflexion Agent có khả năng tự đánh giá (self-reflection) để học từ các lỗi sai trong suy luận ban đầu và cải thiện câu trả lời qua nhiều lần thử.

## Các tính năng đã thực hiện

- **Tích hợp LLM thật**: Đã thay thế thành công Mock Runtime bằng LLM Runtime (`src/reflexion_lab/llm_runtime.py`) để gọi trực tiếp các mô hình thật.
- **Biến môi trường linh hoạt**: Cấu hình API và Base URL động thông qua file `.env`.
- **Tùy biến Model**: Cập nhật script `run_benchmark.py` hỗ trợ tham số `--model` để linh hoạt thay đổi và tự động ghi nhận model đang sử dụng vào báo cáo đầu ra.
- **Đánh giá Benchmark thực tế**: Đã chạy benchmark và tạo báo cáo thành công cho hai bộ dữ liệu:
  - `hotpot_golden.json` (20 mẫu test)
  - `hotpot_dev_distractor_v1_100_formatted.json` (100 mẫu test)

## Cài đặt và Cấu hình

1. **Khởi tạo và cài đặt môi trường:**
   ```bash
   python -m venv .venv
   
   # Trên Windows:
   .venv\Scripts\activate
   # Trên Linux/Mac:
   source .venv/bin/activate
   
   pip install -r requirements.txt
   ```

2. **Cấu hình biến môi trường (`.env`):**
   Đảm bảo file `.env` ở thư mục gốc của dự án có định dạng như sau:
   ```env
   DASHSCOPE_API_KEY="api_key_cua_ban_tai_day"
   BASE_URL="https://ws-7z0pgh6qqcnccram.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
   ```

## Hướng dẫn chạy Benchmark

Script đo benchmark hỗ trợ ghi nhận kết quả và xuất báo cáo tự động ra thư mục `outputs/`.

**1. Chạy đánh giá trên bộ dữ liệu 100 câu hỏi:**
```bash
python run_benchmark.py --dataset data/hotpot_dev_distractor_v1_100_formatted.json --out-dir outputs/sample_run
```

**2. Chạy đánh giá trên bộ dữ liệu Golden (20 câu hỏi):**
```bash
python run_benchmark.py --dataset data/hotpot_golden.json --out-dir outputs/golden_run
```

*Ghi chú:* Mặc định tham số model là `qwen-flash`. Nếu bạn muốn đổi sang mô hình khác, bạn có thể truyền thêm cờ `--model`, ví dụ: `--model qwen-plus`.

## Cấu trúc Mã Nguồn

| File / Thư mục | Mô tả |
|---|---|
| `src/reflexion_lab/llm_runtime.py` | Tích hợp gọi API thực tế để tạo tương tác với Actor, Evaluator, Reflector. |
| `src/reflexion_lab/agents.py` | Vòng lặp chính của ReAct Agent và Reflexion Agent. |
| `src/reflexion_lab/schemas.py` | Định nghĩa các cấu trúc dữ liệu (`QAExample`, `JudgeResult`, `ReflectionEntry`, ...). |
| `run_benchmark.py` | Script để khởi chạy hệ thống đánh giá theo bộ dataset được chỉ định. |
| `data/` | Thư mục chứa các tệp dữ liệu kiểm thử (.json). |
| `outputs/` | Nơi lưu trữ nhật ký chạy và các báo cáo (`report.json`, `report.md`). |
