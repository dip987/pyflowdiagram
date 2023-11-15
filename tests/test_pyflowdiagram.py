#!/usr/bin/env python

"""Tests for `pyflowdiagram` package."""


import unittest
from matplotlib.axes import Axes
from matplotlib.text import Text
from pyflowdiagram import draw_process_flow


class TestPyflowdiagram(unittest.TestCase):
    """Tests for `pyflowdiagram` package."""

    def setUp(self):
        self.labels = ["T1", "T2", "T3", "T4"]
        self.groups = [1, 1, 2, 2]
        self.fig = draw_process_flow(self.labels, 3.0, 1.5, self.groups)
        self.axes: Axes
        self.axes = self.fig.get_axes()[0]

    def test_draw_process_flow_contains_all_labels(self):
        text_elements = [x for x in self.axes.get_children() if isinstance(x, Text)]
        figure_labels = [x.get_text() for x in text_elements]
        for label in self.labels:
            self.assertIn(label, figure_labels)

    def test_draw_process_flow_contains_at_least_n_minus_1_arrows(self):
        text_elements = [x for x in self.axes.get_children() if isinstance(x, Text)]
        figure_labels = [x.get_text() for x in text_elements]
        empty_labels = [x for x in figure_labels if x == ""]
        self.assertGreater(len(empty_labels), len(self.labels) - 1)
