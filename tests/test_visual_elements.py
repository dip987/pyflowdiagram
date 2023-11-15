#!/usr/bin/env python

"""Tests for `pyflowdiagram` package."""


import unittest
import matplotlib.pyplot as plt
from matplotlib.text import Text
from pyflowdiagram.visual_elements import CenteredRectangle, create_axes, Axes, draw_block, draw_arrow


class TestVisualElements(unittest.TestCase):
    """Tests for `pyflowdiagram` package."""
    def setUp(self):
        self.fig_width = 10
        self.fig_height = 5
        self.fig = plt.figure(figsize=(self.fig_width, self.fig_height))

    def test_centered_rectangle_super_has_correct_xy(self):
        width, height = 2.0, 2.0
        rect = CenteredRectangle((0, 0), width, height)
        self.assertEqual(rect.xy, (-width/2, -height/2))

    def test_create_axes_returns_axes(self):
        axes = create_axes(self.fig, self.fig_width, self.fig_height)
        self.assertIsInstance(axes, Axes)

    def test_create_axes_has_correct_limits(self):
        axes = create_axes(self.fig, self.fig_width, self.fig_height)
        self.assertEqual(axes.get_xlim(), (0, self.fig_width))
        self.assertEqual(axes.get_ylim(), (0, self.fig_height))

    def test_draw_block_draws_text_and_centered_rec(self):
        axes = create_axes(self.fig, self.fig_width, self.fig_height)
        initial_elements = axes.get_children().copy()
        draw_block('Test', (0, 0), axes, 2, 2, 'blue')
        elements_after_draw = axes.get_children().copy()
        new_elements = [x for x in elements_after_draw if x not in initial_elements]
        axes_element_types = [type(x) for x in new_elements]
        self.assertIn(CenteredRectangle, axes_element_types, "Could not find a CenteredRectangle")
        self.assertIn(Text, axes_element_types, "Could not find a block text")

    def test_draw_block_draws_correct_text(self):
        axes = create_axes(self.fig, self.fig_width, self.fig_height)
        initial_elements = axes.get_children().copy()
        block_text = "Test"
        draw_block(block_text, (0, 0), axes, 2, 2, 'blue')
        elements_after_draw = axes.get_children().copy()
        new_elements = [x for x in elements_after_draw if x not in initial_elements]
        for element in new_elements:
            if element is Text:
                self.assertEqual(element.get_text(), block_text)
                return

    def test_draw_arrow_draws_something(self):
        axes = create_axes(self.fig, self.fig_width, self.fig_height)
        initial_elements = axes.get_children().copy()
        draw_block('Test', (0, 0), axes, 2, 2, 'blue')
        elements_after_draw = axes.get_children().copy()
        new_elements = [x for x in elements_after_draw if x not in initial_elements]
        self.assertNotEqual(len(new_elements), 0)
