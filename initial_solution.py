import numpy as np
import random


def create_initial_solution(instance):
    solution = {
        "body": {
            "entry": [],
            "exit": []
        },
        "paint": {
            "entry": [],
            "exit": []
        },
        "assembly": {
            "entry": [],
            "exit": []
        },
    }
    two_tones_list = []
    for vehicle in instance["vehicles"]:
        id = int(vehicle["id"])
        if vehicle["type"] == "two-tone":
            two_tones_list.append(id)
        elif vehicle["type"] == "regular":
            pass
        else:
            raise ValueError("type does not exist")

    initial_scheduling = get_random_initial_sequence(instance)

    solution["body"]["entry"] = initial_scheduling
    solution["body"]["exit"] = initial_scheduling
    solution["paint"]["entry"] = initial_scheduling

    delta = instance["parameters"]["two_tone_delta"]
    paint_exit = execute_paint_move(
        input_paint_sequence=initial_scheduling,
        two_tones_list=two_tones_list,
        delta=delta
    )

    solution["paint"]["exit"] = paint_exit
    solution["assembly"]["entry"] = paint_exit
    solution["assembly"]["exit"] = paint_exit

    return solution


def lot_first_try(instance):
    for constraint in instance["constraints"]:
        if constraint["type"] == "lot_change" and constraint["shop"] in ["paint", "body"]:
            initial_sequence = []
            for lot in constraint["partition"]:
                lot_ = lot.copy()
                random.shuffle(lot_)
                initial_sequence += lot_
    return initial_sequence


def get_random_initial_sequence(instance):
    n_vehicles = len(instance["vehicles"])
    initial_sequence = np.random.permutation(np.arange(1, n_vehicles + 1))
    initial_sequence = initial_sequence.tolist()
    return initial_sequence


def execute_paint_move(input_paint_sequence, two_tones_list, delta):
    order_two_tones = \
        sorted(two_tones_list, key=lambda x: input_paint_sequence.index(x))

    output_sequence = input_paint_sequence.copy()
    n_vehicles = len(input_paint_sequence)
    for u in order_two_tones:
        t = output_sequence.index(u)
        last_in_cycle = min(delta, n_vehicles - (t+1))

        output_sequence[t:t+last_in_cycle] = \
            output_sequence[t+1:t+last_in_cycle+1]
        output_sequence[t+last_in_cycle] = u

    return output_sequence


# def get_similarity_matrix(instance):
#     n_vehicles = len(instance["vehicles"])
#     similarity_matrix = np.zeros((n_vehicles, n_vehicles))

#     for constraint in instance["constraints"]:
