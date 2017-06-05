#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO


class Axis(object):

    """Docstring for Axis. """

    def __init__(self, io_dir, io_step, max_steps=400):
        """Axis Control Class

        :io_dir: Direction GPIO
        :io_step: Step GPIO
        :max_steps: Max Steps in One Direction

        """
        self._io_dir = io_dir
        self._io_step = io_step
        self._current_pos = 0
        GPIO.setup(self._io_dir, GPIO.OUT)
        GPIO.output(self._io_dir, 0)
        GPIO.setup(self._io_step, GPIO.OUT)
        GPIO.output(self._io_step, 0)

    def move_to(self, pos):
        """Move To Specific Position

        :pos: Specific Position
        """
        pass

    def reset(self):
        """Reset to the Zere Position
        """
        pass
