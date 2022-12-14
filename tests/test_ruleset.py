from cmath import sqrt

import networkx as nx
import numpy as np
import pychrono as chrono

from rostok.block_builder.node_render import (ChronoRevolveJoint, ChronoTransform, FlatChronoBody,
                                              LinkChronoBody, MountChronoBody)
from rostok.block_builder.transform_srtucture import FrameTransform
from rostok.graph_grammar.node import ROOT, BlockWrapper, GraphGrammar
from rostok.graph_grammar.node_vocabulary import NodeVocabulary
from rostok.graph_grammar.rule_vocabulary import RuleVocabulary

# Define block types
mat = chrono.ChMaterialSurfaceNSC()
mat.SetFriction(0.5)
mat.SetDampingF(0.1)

# Bodies
link1 = BlockWrapper(LinkChronoBody, length=0.3)
link2 = BlockWrapper(LinkChronoBody, length=0.2)

flat1 = BlockWrapper(FlatChronoBody, width=0.4, length=0.1)
flat2 = BlockWrapper(FlatChronoBody, width=0.7, length=0.1)

u1 = BlockWrapper(MountChronoBody, width=0.1, length=0.1)

# Transforms
RZX = FrameTransform([0, 0, 0], [sqrt(2), 0, sqrt(2), 0])
RZY = FrameTransform([0, 0, 0], [sqrt(2), -sqrt(2), 0, 0])
RXY = FrameTransform([0, 0, 0], [sqrt(2), 0, 0, sqrt(2)])

MOVE_ZX_PLUS = FrameTransform([0.3, 0, 0.3], [1, 0, 0, 0])
MOVE_ZX_MINUS = FrameTransform([-0.3, 0, -0.3], [1, 0, 0, 0])

MOVE_X_PLUS = FrameTransform([0.3, 0, 0.], [1, 0, 0, 0])
MOVE_Z_PLUS_X_MINUS = FrameTransform([-0.3, 0, 0.3], [1, 0, 0, 0])

transform_rzx = BlockWrapper(ChronoTransform, RZX)
transform_rzy = BlockWrapper(ChronoTransform, RZY)
transform_rxy = BlockWrapper(ChronoTransform, RXY)
transform_mzx_plus = BlockWrapper(ChronoTransform, MOVE_ZX_PLUS)
transform_mzx_minus = BlockWrapper(ChronoTransform, MOVE_ZX_MINUS)
transform_mx_plus = BlockWrapper(ChronoTransform, MOVE_X_PLUS)
transform_mz_plus_x_minus = BlockWrapper(ChronoTransform, MOVE_Z_PLUS_X_MINUS)

type_of_input = ChronoRevolveJoint.InputType.TORQUE
# Joints
revolve1 = BlockWrapper(ChronoRevolveJoint, ChronoRevolveJoint.Axis.Z, type_of_input)

# %%
type_of_input = ChronoRevolveJoint.InputType.POSITION

# Joints
revolve1 = BlockWrapper(ChronoRevolveJoint, ChronoRevolveJoint.Axis.Z, type_of_input)

node_vocab = NodeVocabulary()
node_vocab.add_node(ROOT)
node_vocab.create_node("J")
node_vocab.create_node("L")
node_vocab.create_node("F")
node_vocab.create_node("M")
node_vocab.create_node("EF")
node_vocab.create_node("EM")

node_vocab.create_node(label="J1", is_terminal=True, block_wrapper=revolve1)
node_vocab.create_node(label="L1", is_terminal=True, block_wrapper=link1)
node_vocab.create_node(label="L2", is_terminal=True, block_wrapper=link2)
node_vocab.create_node(label="F1", is_terminal=True, block_wrapper=flat1)
node_vocab.create_node(label="F2", is_terminal=True, block_wrapper=flat2)
node_vocab.create_node(label="U1", is_terminal=True, block_wrapper=u1)
node_vocab.create_node(label="T1", is_terminal=True, block_wrapper=transform_mx_plus)
node_vocab.create_node(label="T2", is_terminal=True, block_wrapper=transform_mz_plus_x_minus)
node_vocab.create_node(label="T3", is_terminal=True, block_wrapper=transform_mzx_plus)
node_vocab.create_node(label="T4", is_terminal=True, block_wrapper=transform_mzx_minus)

rule_vocab = RuleVocabulary(node_vocab)

rule_vocab.create_rule("FlatCreate", ["ROOT"], ["F"], 0, 0)
rule_vocab.create_rule("Mount", ["F"], ["F", "M", "EM"], 0, 0, [(0, 1), (1, 2)])
rule_vocab.create_rule("MountAdd", ["M"], ["M", "EM"], 0, 1, [(0, 1)])
rule_vocab.create_rule("FingerUpper", ["EM"], ["J", "L", "EM"], 0, 2, [(0, 1), (1, 2)])

rule_vocab.create_rule("TerminalFlat1", ["F"], ["F1"], 0, 0)
rule_vocab.create_rule("TerminalFlat2", ["F"], ["F2"], 0, 0)

rule_vocab.create_rule("TerminalL1", ["L"], ["L1"], 0, 0)
rule_vocab.create_rule("TerminalL2", ["L"], ["L2"], 0, 0)

rule_vocab.create_rule("TerminalTransformRX", ["M"], ["T1"], 0, 0)
rule_vocab.create_rule("TerminalTransformLZ", ["M"], ["T2"], 0, 0)
rule_vocab.create_rule("TerminalTransformR", ["M"], ["T3"], 0, 0)
rule_vocab.create_rule("TerminalTransformL", ["M"], ["T4"], 0, 0)
rule_vocab.create_rule("TerminalEndLimb", ["EM"], ["U1"], 0, 0)
rule_vocab.create_rule("TerminalJoint", ["J"], ["J1"], 0, 0)

rule_action_non_terminal_three_finger = np.asarray([
    "FlatCreate", "Mount", "Mount", "Mount", "FingerUpper", "FingerUpper", "FingerUpper",
    "FingerUpper", "FingerUpper", "FingerUpper"
])
rule_action_terminal_three_finger = np.asarray([
    "TerminalFlat1", "TerminalL1", "TerminalL1", "TerminalL1", "TerminalL2", "TerminalL2",
    "TerminalL2", "TerminalTransformL", "TerminalTransformLZ", "TerminalTransformRX",
    "TerminalEndLimb", "TerminalEndLimb", "TerminalEndLimb", "TerminalJoint", "TerminalJoint",
    "TerminalJoint", "TerminalJoint", "TerminalJoint", "TerminalJoint"
])
rule_action_three_finger = np.r_[rule_action_non_terminal_three_finger,
                                 rule_action_terminal_three_finger]

rule_action_non_terminal_two_finger = np.asarray([
    "FlatCreate", "Mount", "Mount", "FingerUpper", "FingerUpper", "FingerUpper", "FingerUpper",
    "FingerUpper"
])

rule_action_terminal_two_finger = np.asarray([
    "TerminalFlat1", "TerminalL1", "TerminalL1", "TerminalL1", "TerminalL2", "TerminalL2",
    "TerminalTransformL", "TerminalTransformLZ", "TerminalEndLimb", "TerminalEndLimb",
    "TerminalJoint", "TerminalJoint", "TerminalJoint", "TerminalJoint", "TerminalJoint"
])
rule_action_two_finger = np.r_[rule_action_non_terminal_two_finger, rule_action_terminal_two_finger]

rule_action_non_terminal_ladoshaka = np.asarray(["FlatCreate", "Mount"])

rule_action_terminal_no_joints = np.asarray(
    ["TerminalFlat1", "TerminalTransformL", "TerminalEndLimb"])

rule_action_no_joints = np.r_[rule_action_non_terminal_ladoshaka, rule_action_terminal_no_joints]


def get_terminal_graph_three_finger():
    G = GraphGrammar()
    for i in list(rule_action_three_finger):
        G.apply_rule(rule_vocab.get_rule(i))
    return G


def get_terminal_graph_no_joints():
    G = GraphGrammar()
    for i in list(rule_action_no_joints):
        G.apply_rule(rule_vocab.get_rule(i))
    return G


def get_terminal_graph_two_finger():
    G = GraphGrammar()
    for i in list(rule_action_two_finger):
        G.apply_rule(rule_vocab.get_rule(i))
    return G


def get_nonterminal_graph_two_finger():
    G = GraphGrammar()
    for i in list(rule_action_non_terminal_two_finger):
        G.apply_rule(rule_vocab.get_rule(i))
    return G