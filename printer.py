#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
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
        self._pulse_width_us = 2
        self._max_steps = max_steps

        GPIO.setup(self._io_dir, GPIO.OUT)
        GPIO.output(self._io_dir, GPIO.LOW)
        GPIO.setup(self._io_step, GPIO.OUT)
        GPIO.output(self._io_step, GPIO.HIGH)

    def step(self, direction):
        """One Step for direction

        :direction: direction

        """
        GPIO.output(self._io_dir, GPIO.LOW if direction else GPIO.HIGH)
        GPIO.output(self._io_step, GPIO.HIGH)
        time.sleep(self._pulse_width_us / float(1000000))
        GPIO.output(self._io_step, GPIO.LOW)

    def move_to(self, pos):
        """Move To Specific Position

        :pos: Specific Position
        """
        if pos > self._max_steps:
            pos = self._max_steps
        if pos < 0:
            pos = 0
        if pos < self._current_pos:
            steps = self._current_pos - pos
            direction = True
        else:
            steps = pos - self._current_pos
            direction = False
        for _ in range(steps):
            self.step(direction)
        self._current_pos = pos

    def reset(self):
        """Reset to the Zero Position
        """
        for _ in range(self._current_pos+20):
            self.step(False)
