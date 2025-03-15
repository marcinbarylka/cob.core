"""Module for testing the serialization module."""

import pygame

from citadel_of_blood.gui.colors import ColorPair, WidgetColors
from citadel_of_blood.gui.serialization import serialize_color, deserialize_color


# --- Tests for serialize_color and deserialize_color functions ---


def test_serialize_color_with_tuple():
    color_in = (123, 45, 67)
    result = serialize_color(color_in)
    assert result == (123, 45, 67)


def test_serialize_color_with_pygame_color():
    color_in = pygame.Color(10, 20, 30)
    result = serialize_color(color_in)
    assert result == (10, 20, 30)


def test_serialize_color_with_hex_str():
    color_in = "#ff0000"
    result = serialize_color(color_in)
    assert result == "#ff0000"


def test_deserialize_color_with_tuple():
    data = (200, 150, 100)
    result = deserialize_color(data)
    expected = pygame.Color(200, 150, 100)
    assert (result.r, result.g, result.b) == (expected.r, expected.g, expected.b)


def test_deserialize_color_with_hex_str():
    data = "#0000ff"
    result = deserialize_color(data)
    expected = pygame.Color("#0000ff")
    assert (result.r, result.g, result.b) == (expected.r, expected.g, expected.b)


# --- Tests for ColorPair ---


def test_colorpair_background_serialization():
    cp = ColorPair(background_color=(255, 0, 0), foreground_color="#00ff00")
    cp_dict = cp.serialize()
    assert cp_dict["background_color"] == (255, 0, 0)


def test_colorpair_foreground_serialization():
    cp = ColorPair(background_color=(255, 0, 0), foreground_color="#00ff00")
    cp_dict = cp.serialize()
    assert cp_dict["foreground_color"] == "#00ff00"


def test_colorpair_background_deserialization():
    cp_dict = {"background_color": (255, 0, 0), "foreground_color": "#00ff00"}
    cp = ColorPair.deserialize(cp_dict)
    expected = pygame.Color(255, 0, 0)
    assert (cp.background_color.r, cp.background_color.g, cp.background_color.b) == (expected.r, expected.g, expected.b)


def test_colorpair_foreground_deserialization():
    cp_dict = {"background_color": (255, 0, 0), "foreground_color": "#00ff00"}
    cp = ColorPair.deserialize(cp_dict)
    expected = pygame.Color("#00ff00")
    assert (cp.foreground_color.r, cp.foreground_color.g, cp.foreground_color.b) == (expected.r, expected.g, expected.b)


# --- Tests for WidgetColors ---


def test_widgetcolors_normal_serialization():
    cp_normal = ColorPair(background_color="#000000", foreground_color="#ffffff")
    wc = WidgetColors(normal=cp_normal, hover=cp_normal, click=None)
    wc_dict = wc.serialize()
    assert "normal" in wc_dict
    # Test only normal colors here
    normal = wc_dict["normal"]
    assert normal["background_color"] == "#000000"
    assert normal["foreground_color"] == "#ffffff"


def test_widgetcolors_hover_serialization():
    cp_hover = ColorPair(background_color="#808080", foreground_color=(100, 100, 100))
    wc = WidgetColors(normal=cp_hover, hover=cp_hover, click=None)
    wc_dict = wc.serialize()
    hover = wc_dict["hover"]
    assert hover["background_color"] == "#808080"
    assert hover["foreground_color"] == (100, 100, 100)


def test_widgetcolors_click_serialization():
    cp_click = ColorPair(background_color=(50, 50, 50), foreground_color="#ffff00")
    wc = WidgetColors(normal=cp_click, hover=cp_click, click=cp_click)
    wc_dict = wc.serialize()
    click = wc_dict["click"]
    assert click["background_color"] == (50, 50, 50)
    assert click["foreground_color"] == "#ffff00"


def test_widgetcolors_normal_deserialization():
    wc_dict = {
        "normal": {"background_color": "#000000", "foreground_color": "#ffffff"},
        "hover": {"background_color": "#808080", "foreground_color": (100, 100, 100)},
        "click": None,
    }
    wc = WidgetColors.deserialize(wc_dict)
    expected_normal_bg = pygame.Color("#000000")
    expected_normal_fg = pygame.Color("#ffffff")
    n = wc.normal
    assert (n.background_color.r, n.background_color.g, n.background_color.b) == (
        expected_normal_bg.r,
        expected_normal_bg.g,
        expected_normal_bg.b,
    )
    assert (n.foreground_color.r, n.foreground_color.g, n.foreground_color.b) == (
        expected_normal_fg.r,
        expected_normal_fg.g,
        expected_normal_fg.b,
    )


def test_widgetcolors_hover_deserialization():
    wc_dict = {
        "normal": {"background_color": "#000000", "foreground_color": "#ffffff"},
        "hover": {"background_color": "#808080", "foreground_color": (100, 100, 100)},
        "click": None,
    }
    wc = WidgetColors.deserialize(wc_dict)
    expected_hover_bg = pygame.Color("#808080")
    expected_hover_fg = pygame.Color(100, 100, 100)
    h = wc.hover
    assert (h.background_color.r, h.background_color.g, h.background_color.b) == (
        expected_hover_bg.r,
        expected_hover_bg.g,
        expected_hover_bg.b,
    )
    assert (h.foreground_color.r, h.foreground_color.g, h.foreground_color.b) == (
        expected_hover_fg.r,
        expected_hover_fg.g,
        expected_hover_fg.b,
    )


def test_widgetcolors_click_deserialization():
    wc_dict = {
        "normal": {"background_color": "#000000", "foreground_color": "#ffffff"},
        "hover": {"background_color": "#808080", "foreground_color": (100, 100, 100)},
        "click": {"background_color": (50, 50, 50), "foreground_color": "#ffff00"},
    }
    wc = WidgetColors.deserialize(wc_dict)
    expected_click_bg = pygame.Color(50, 50, 50)
    expected_click_fg = pygame.Color("#ffff00")
    c = wc.click
    assert (c.background_color.r, c.background_color.g, c.background_color.b) == (
        expected_click_bg.r,
        expected_click_bg.g,
        expected_click_bg.b,
    )
    assert (c.foreground_color.r, c.foreground_color.g, c.foreground_color.b) == (
        expected_click_fg.r,
        expected_click_fg.g,
        expected_click_fg.b,
    )
