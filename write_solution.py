import json

def write_solution(
    filename: int, solution, instance
) -> None:
    out_data = {"a": 0}
    with open(f"solutions/{filename}", 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=4)
