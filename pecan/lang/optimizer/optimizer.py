#!/usr/bin/env python3.6
# -*- coding=utf-8 -*-

from pecan.lang.optimizer.boolean import BooleanOptimizer
from pecan.lang.optimizer.arithmetic import ArithmeticOptimizer

from pecan.lang.ir import *

class Optimizer:
    def __init__(self, prog):
        self.prog = prog

    def optimize(self):
        for i, d in enumerate(self.prog.defs):
            if type(d) is NamedPred:
                self.prog.defs[i] = NamedPred(d.name, d.args, self.run_optimizations(d.body), restriction_env=d.restriction_env)

        if self.prog.debug > 1:
            print('Optimized program:')
            print(self.prog)

        return self.prog

    def run_optimizations(self, node):
        if self.prog.debug > 2:
            print('Optimizing:', node)
        optimization_pass = [ArithmeticOptimizer(), BooleanOptimizer()]
        new_node = node

        ast_changed = True # Default to true so we run at least once
        while ast_changed:
            ast_changed = False
            for optimization in optimization_pass:
                changed, new_node = optimization.optimize(new_node)
                ast_changed |= changed

        if self.prog.debug > 2:
            print('Optimized node:', new_node)
        return new_node

