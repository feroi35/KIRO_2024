import json


def write_solution(
    filename: int, solution, instance
) -> None:
    with open(f"solutions/{filename}", 'w', encoding='utf-8') as f:
        json.dump(solution, f, ensure_ascii=False, indent=4)
