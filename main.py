from read_instance import read_instance
from write_solution import write_solution
from initial_solution import create_initial_solution
from local_search import local_search

def main():
    instances_size = [
        "tiny",
        "small",
        "medium",
        "large"
    ]
    
    instance_size = "tiny"
    instance_dict = read_instance(instance_size)

    initial_solution = create_initial_solution(instance_dict)

    solution = local_search(initial_solution, instance_dict)

    write_solution(f"{instance_size}_0.json", solution, instance_dict)

if __name__ == "__main__":
    main()
