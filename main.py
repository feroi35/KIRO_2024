from read_instance import read_instance
from write_solution import write_solution
from initial_solution import create_initial_solution
from local_search import local_search


def main():
    instances = [
        "tiny",
        "small_1",
        "small_2",
        "medium_1",
        "medium_2",
        "large_1",
        "large_2"
    ]

    for instance in instances:
        print(instance)
        instance_dict = read_instance(instance)

        initial_solution = create_initial_solution(instance_dict)

        # solution = local_search(initial_solution, instance_dict)

        write_solution(f"{instance}.json",
                       initial_solution, instance_dict)


if __name__ == "__main__":
    main()
