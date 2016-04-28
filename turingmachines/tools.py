#!/usr/bin/env python3
"""Functions for displaying and maniuplating Turing machines."""


def print_config(current_state, tape, min_position_offset):
    """Print the machine's current configuration in a readable form."""
    print('{current_state}: {tape}\n{current_position}'.format(
        current_state=current_state,
        tape=str(tape).rjust(
            len(tape) + tape.position_offset - min_position_offset,
            tape.blank_symbol),
        current_position='^'.rjust(
            tape.current_position - min_position_offset +
            len(current_state) + 3),
    ))


def _get_min_position_offset(configs):
    """Return the smallest position offset the tape reached at any point."""
    return min(tape.position_offset for current_state, tape in configs)


def print_configs(validation_generator):
    """Print each machine configuration represented by the given generator."""
    configs = []
    for current_state, tape in validation_generator:
        configs.append((current_state, tape.copy()))
    min_position_offset = _get_min_position_offset(configs)
    for current_state, tape in configs:
        print_config(current_state, tape, min_position_offset)
