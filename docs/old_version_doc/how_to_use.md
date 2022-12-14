# Usage of the framework

The framework allows user to specify nodes/parts of the mechanism and rules that can change the design. The rules can either change the morphology (nonterminal rules) or set the physical properties (terminal rules). The search algorithm requires user to create objects of `NodeVocabulary`, `RuleVocabulary` and specify the classes of nodes.

## Use graph builder

The graph that represent the mechanism can be built by setting the sequence of building rules. User can visualize the graph...

## Use simulation module

Set the joint trajectories and carry out a virtual experiment with the built graph/mechanism. Add objects and see how the mechanism interact with them. User can either add be one of predefined bodies or set the object as a Pychrono object.

## Use trajectory optimization

Any dynamic mechanism requires the control trajectories for joints. Optimize control trajectories for the built mechanisms according to the task  

## Use search algorithms

Graph representation allows to effectively search the space of mechanisms achievable with preset nodes and rules. The main goal of the framework is to search for the most effective designs for the given task.  
