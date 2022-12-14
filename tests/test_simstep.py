import random

import numpy as np
import pychrono as chrono
from test_ruleset import (get_terminal_graph_no_joints,
                          get_terminal_graph_three_finger,
                          get_terminal_graph_two_finger)

import rostok.virtual_experiment.simulation_step as step
from test_ruleset import rule_vocab
from rostok.graph_grammar import make_random_graph
from rostok.block_builder.basic_node_block import SimpleBody
from rostok.block_builder.node_render import (ChronoBodyEnv,
                                              DefaultChronoMaterial,
                                              FrameTransform)
from rostok.criterion.flags_simualtions import FlagMaxTime
from rostok.graph_grammar.node import BlockWrapper
from rostok.trajectory_optimizer.control_optimizer import num_joints
from rostok.trajectory_optimizer.trajectory_generator import \
    create_torque_traj_from_x


def test_create_graph():
    """
        Test for graph grammar and rule
    """
    graph = make_random_graph.make_random_graph(5, rule_vocab)


def test_control_bind_and_create_sim():
    """
        Test for simulation class, control binder and control generator
    """

    mechs = [
        get_terminal_graph_three_finger, get_terminal_graph_no_joints, get_terminal_graph_two_finger
    ]

    for get_graph in mechs:
        G = get_graph()
        number_trq = num_joints(G)

        config_sys = {"Set_G_acc": chrono.ChVectorD(0, 0, 0)}
        max_time = 1
        flags = [FlagMaxTime(max_time)]
        times_step = 1e-3

        const_torque_koef = [random.random() for _ in range(number_trq)]
        arr_trj = create_torque_traj_from_x(G, const_torque_koef, 1, 0.1)

        matich = DefaultChronoMaterial()
        matich.Friction = 0.65
        matich.DampingF = 0.65
        obj = BlockWrapper(ChronoBodyEnv,
                           shape=SimpleBody.ELLIPSOID,
                           material=matich,
                           pos=FrameTransform([0, 1, 0], [0, -0.048, 0.706, 0.706]))

        sim = step.SimulationStepOptimization(arr_trj, G, obj)
        sim.set_flags_stop_simulation(flags)
        sim.change_config_system(config_sys)
        sim_output = sim.simulate_system(times_step)