#!/usr/bin/python3
#
# SPDX-FileCopyrightText: ExtremeXT
# SPDX-License-Identifier: 	AGPL-3.0-only
#

from scipy.interpolate import PchipInterpolator
import numpy as np
import xml.etree.ElementTree as ET


# Configurable values
LOW_NITS = 150  # Nits up to which it should be more accurate than usual.
LOW_WEIGHT = 5  # 1-10, "weight" of the lower nits.
MID_NITS = 500  # Middle nit value, HBM cutoff.
TARGET_POINTS = 10  # Number of points the map will have; this should be the lowest value possible that still generates a workable map.


def parse_overlay(path):
    root = ET.parse(path).getroot()

    def get_array(name):
        for arr in root.findall('.//integer-array'):
            if arr.get('name') == name:
                return [float(i.text.strip()) for i in arr.findall('item')]
        for arr in root.findall('.//array'):
            if arr.get('name') == name:
                return [float(i.text.strip()) for i in arr.findall('item')]
        raise KeyError(name)

    backlight = get_array('config_screenBrightnessBacklight')
    nits = get_array('config_screenBrightnessNits')
    xs = np.array([b / max(backlight) for b in backlight])
    ys = np.array(nits, dtype=float)
    return xs, ys


xs, ys = parse_overlay('overlay.xml')

full = PchipInterpolator(xs, ys)
inv = PchipInterpolator(ys, xs)


def fmt(x: float) -> str:
    s = f'{x:.4f}'.rstrip('0').rstrip('.')
    return s + '.0' if '.' not in s else s


selected_x = [0.0, float(inv(MID_NITS)), 1.0]
selected_y = [float(full(0.0)), float(MID_NITS), float(full(1.0))]

weight = np.where(ys < LOW_NITS, LOW_WEIGHT, 1.0)

while len(selected_x) < TARGET_POINTS:
    pred = PchipInterpolator(selected_x, selected_y)(xs)
    err_w = np.abs(pred - ys) * weight

    idx = int(np.argmax(err_w))
    wx, wy = float(xs[idx]), float(ys[idx])

    if wx in selected_x:
        for cand in np.argsort(err_w)[::-1]:
            if float(xs[cand]) not in selected_x:
                wx, wy = float(xs[cand]), float(ys[cand])
                break
        else:
            break

    selected_x.append(wx)
    selected_y.append(wy)
    selected_x, selected_y = map(
        list, zip(*sorted(zip(selected_x, selected_y)))
    )

cx, cy = selected_x, selected_y
print(', '.join(fmt(x) for x in cx))
print(', '.join(f'{y:.1f}'.rstrip('0').rstrip('.') for y in cy))
