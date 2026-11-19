#!/usr/bin/env python3
"""Builds the Sauna & Banya Icon Set: svg/*.svg, sprite.svg, icons.json, preview.html.
The icon drawings live in ICONS below (hand-written path data on a 24 x 24 grid).
License: CC BY 4.0 - DIVELUX, https://diveluxsaunahat.com
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STROKE = "1.5"


def P(d):
    return f'<path d="{d}"/>'


def C(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'


def R(x, y, w, h, rx):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'


def snowflake():
    out = []
    for k in range(6):
        a = math.radians(60 * k - 90)
        def pt(r, da=0.0):
            return (12 + r * math.cos(a + da), 12 + r * math.sin(a + da))
        f = lambda p: f"{round(p[0], 2):g} {round(p[1], 2):g}"
        tip, mid = pt(9.5), pt(6)
        l = (mid[0] + 2.6 * math.cos(a - math.radians(50)), mid[1] + 2.6 * math.sin(a - math.radians(50)))
        r = (mid[0] + 2.6 * math.cos(a + math.radians(50)), mid[1] + 2.6 * math.sin(a + math.radians(50)))
        out.append(f"M12 12 {f(tip)}M{f(l)} {f(mid)} {f(r)}")
    return P("".join(out))


# name: (title, [elements], [tags])
ICONS = {
    "sauna-hat": ("Sauna hat", [
        P("M5.5 16.5c1.2-3.2.8-11 6.5-11s5.3 7.8 6.5 11"),
        P("M4.5 16.5h15a1.5 1.5 0 0 1 0 3h-15a1.5 1.5 0 0 1 0-3z"),
        P("M12 5.5c-1.6-.8-1.7-2.8-.5-3 1.2-.2 1.7 1.5.5 3z"),
        P("M12 5.5c1.3 3 1.8 6.5 1.8 11")],
        ["sauna hat", "bell hat", "felt hat", "wool", "banya hat", "headwear"]),
    "bucket-hat": ("Bucket sauna hat", [
        P("M7.5 13.2c.2-4.3 1.2-7.7 4.5-7.7s4.3 3.4 4.5 7.7"),
        P("M2.5 17.2c2-2.6 5-4 9.5-4s7.5 1.4 9.5 4c-2.6 1.4-6 2.1-9.5 2.1s-6.9-.7-9.5-2.1z")],
        ["bucket hat", "sauna hat", "brim", "felt hat", "wool", "headwear"]),
    "sauna-stove": ("Sauna stove with stones", [
        R(4.5, 11.5, 15, 7.5, 1),
        P("M7 19v2M17 19v2"),
        P("M5.5 11.5a2.3 2.3 0 0 1 4.3-1.1 2.6 2.6 0 0 1 4.6-.2 2.3 2.3 0 0 1 4.1 1.3"),
        P("M8.7 8.2a2.2 2.2 0 0 1 3.8-1.1 2.1 2.1 0 0 1 3.2 1.3"),
        P("M8 14.3h8M8 16.5h8")],
        ["stove", "heater", "kiuas", "stones", "rocks", "sauna heater"]),
    "bucket-ladle": ("Sauna bucket and ladle", [
        P("M4 10h12l-1.2 10.5H5.2z"),
        P("M4.4 13.5h11.2M4.8 17.2h10.4"),
        P("M12.5 10 20 3.5"),
        P("M7 10c.3-1.6 1.2-2.5 2.5-2.5")],
        ["bucket", "ladle", "pail", "water", "kiulu", "scoop"]),
    "birch-whisk": ("Birch whisk", [
        P("M3 21.5l5.2-5.2"),
        P("M6.6 15.1l2.8 2.8"),
        P("M8.2 16.3c-2.3-3.2-1.5-6.3.8-7.3.2-3 3-4.7 5.5-3.7 2.5-1.5 5.3.5 4.8 3.2 2 2 1 5.2-1.5 5.7-1 2.5-4 3-5.5 1.5-1.5.8-3 .7-4.1.6z"),
        P("M9.5 15 16 8.5M12.7 11.8V8.5M14.5 10H18")],
        ["whisk", "venik", "vihta", "vasta", "birch", "banya", "leaves"]),
    "thermometer": ("Thermometer", [
        P("M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0z"),
        P("M12 9v9.3"),
        P("M17 6h2.5M17 9.5h2.5M17 13h2.5")],
        ["thermometer", "temperature", "heat", "degrees"]),
    "hygrometer": ("Hygrometer", [
        C(12, 12, 9),
        P("M12 8c2 2.4 3 3.9 3 5.3a3 3 0 0 1-6 0c0-1.4 1-2.9 3-5.3z"),
        P("M12 3v1.5M3 12h1.5M19.5 12H21")],
        ["hygrometer", "humidity", "moisture", "gauge", "dial"]),
    "sand-timer": ("Sand timer", [
        P("M6 3h12M6 21h12"),
        P("M7.5 3v3c0 2.5 4.5 3.5 4.5 6s-4.5 3.5-4.5 6v3"),
        P("M16.5 3v3c0 2.5-4.5 3.5-4.5 6s4.5 3.5 4.5 6v3"),
        P("M10 18.5h4M12 14.5v1")],
        ["sand timer", "hourglass", "timer", "15 minutes", "time"]),
    "sauna-bench": ("Sauna bench", [
        R(9, 6, 12, 3, 0.5),
        R(3, 13, 13, 3, 0.5),
        P("M5 16v5M14 16v5M11.5 9v4M19 9v12")],
        ["bench", "tiers", "seat", "upper bench", "wood"]),
    "steam": ("Steam", [
        P("M7 21c-2-2.5 2-4.5 0-7s2-4.5 0-7"),
        P("M12 18c-2-2.5 2-4.5 0-7s2-4.5 0-7"),
        P("M17 21c-2-2.5 2-4.5 0-7s2-4.5 0-7")],
        ["steam", "vapor", "heat", "hot", "humidity"]),
    "loyly": ("Löyly: water on the stones", [
        P("M2.5 21a3 3 0 0 1 5.6-1.5 3.6 3.6 0 0 1 6.3-.4A3 3 0 0 1 21.5 21z"),
        P("M12 4.5c1.6 2 2.4 3.2 2.4 4.3a2.4 2.4 0 0 1-4.8 0c0-1.1.8-2.3 2.4-4.3z"),
        P("M12 13.5v1.5"),
        P("M5.5 14c-1.3-1.6 1.3-2.8 0-4.4S5 7 5.5 6.2M18.5 14c-1.3-1.6 1.3-2.8 0-4.4s-.5-2.6 0-3.4")],
        ["loyly", "löyly", "steam", "water on stones", "stones", "sauna"]),
    "towel": ("Towel", [
        P("M3 5h18"),
        P("M7 5v14.5h10V5"),
        P("M7 15h10M7 17h10")],
        ["towel", "linen", "bath", "dry", "rail"]),
    "robe": ("Robe", [
        P("M9 3 4 5.5l1.3 6.5L7 11.5V21h10v-9.5l1.7.5L20 5.5 15 3"),
        P("M9 3l3 6.5L15 3"),
        P("M12 9.5V14M7 14.5h10M12 14.5V18")],
        ["robe", "bathrobe", "spa", "kimono", "clothing"]),
    "slippers": ("Slippers", [
        R(3, 3.5, 7.5, 17.5, 3.75),
        R(13.5, 3.5, 7.5, 17.5, 3.75),
        P("M3.2 11c2.2-2.2 4.9-2.2 7.1 0M13.7 11c2.2-2.2 4.9-2.2 7.1 0")],
        ["slippers", "slides", "sandals", "footwear", "spa"]),
    "cold-plunge": ("Cold plunge", [
        P("M3 11.5h18V16a4.5 4.5 0 0 1-4.5 4.5h-9A4.5 4.5 0 0 1 3 16z"),
        P("M6.5 15.5c1-.9 2-.9 3 0s2 .9 3 0 2-.9 3 0 2 .9 2.5.3"),
        P("M12 2v6.5M9.2 3.6l5.6 3.3M14.8 3.6 9.2 6.9")],
        ["cold plunge", "ice bath", "cold water", "tub", "contrast"]),
    "shower": ("Shower", [
        P("M5 21V7.5a4 4 0 0 1 8 0V9"),
        P("M8.5 12.5a4.5 4.5 0 0 1 9 0z"),
        P("M9.5 15.5v1M13 15.5v1M16.5 15.5v1M9.5 19.5v1M13 19.5v1M16.5 19.5v1")],
        ["shower", "rinse", "water", "wash", "cool down"]),
    "snowflake": ("Snowflake", [snowflake()],
        ["snowflake", "cold", "ice", "winter", "snow", "freeze"]),
    "fire-wood": ("Fire and wood", [
        P("M12 2.5c.3 3.2 4.2 4.8 4.2 9a4.2 4.2 0 0 1-8.4 0c0-1.6.7-2.8 1.6-3.7.2 1.3.8 2 1.5 2.3-.5-2.9-.1-5.6 1.1-7.6z"),
        P("M3.5 17.5l17 3.5M3.5 21l17-3.5")],
        ["fire", "flame", "wood", "logs", "wood-burning", "firewood"]),
    "sauna-cabin": ("Sauna cabin", [
        P("M2.5 11.5 12 4l9.5 7.5"),
        P("M5 9.5V21h14V9.5"),
        P("M10 21v-7.5h4V21M12.5 17.5v.5"),
        P("M16 7.2V3.5h2.5v5.7")],
        ["sauna", "cabin", "hut", "house", "outdoor sauna", "building"]),
    "barrel-sauna": ("Barrel sauna", [
        C(12, 11, 8.5),
        P("M9.3 19V11a2.7 2.7 0 0 1 5.4 0v8"),
        P("M12.8 14v.5"),
        P("M4 21.5l2-3.5M20 21.5 18 18")],
        ["barrel sauna", "outdoor sauna", "round", "barrel", "cabin"]),
    "infrared-panel": ("Infrared panel", [
        R(3, 3.5, 6, 17, 1),
        P("M6 6.5v11"),
        P("M12 7c1.5-1.5 3 1.5 4.5 0s3 1.5 4.5 0M12 12c1.5-1.5 3 1.5 4.5 0s3 1.5 4.5 0M12 17c1.5-1.5 3 1.5 4.5 0s3 1.5 4.5 0")],
        ["infrared", "IR sauna", "heater", "panel", "radiant heat"]),
    "sauna-door": ("Sauna door", [
        P("M3 21h18"),
        R(6, 3, 12, 18, 1),
        P("M15 10v4.5"),
        P("M9 8.5 11.5 6M9 12l5-5")],
        ["door", "glass door", "entrance", "exit"]),
    "lamp": ("Lamp", [
        P("M12 3a6 6 0 0 0-4 10.5c.6.6 1 1.3 1 2.1V16h6v-.4c0-.8.4-1.5 1-2.1A6 6 0 0 0 12 3z"),
        P("M9.5 18.5h5M10.5 21h3")],
        ["lamp", "light", "bulb", "lighting"]),
    "essential-oil": ("Essential oil", [
        P("M7.5 12.5a2 2 0 0 1 2-2h5a2 2 0 0 1 2 2V19a2 2 0 0 1-2 2h-5a2 2 0 0 1-2-2z"),
        P("M10 10.5V8h4v2.5"),
        P("M10.8 8V4.5a1.2 1.2 0 0 1 2.4 0V8"),
        P("M12 13.5c1.1 1.3 1.6 2.1 1.6 2.9a1.6 1.6 0 0 1-3.2 0c0-.8.5-1.6 1.6-2.9z")],
        ["essential oil", "aroma", "scent", "dropper", "eucalyptus", "aromatherapy"]),
    "water-bottle": ("Water bottle", [
        R(10, 2.5, 4, 2.5, 0.5),
        P("M10 5c0 2.2-2.5 2.8-2.5 5.5v9a2 2 0 0 0 2 2h5a2 2 0 0 0 2-2v-9C16.5 7.8 14 7.2 14 5"),
        P("M7.5 13.5c1.5-1.1 3 1.1 4.5 0s3 1.1 4.5 0")],
        ["water bottle", "hydration", "drink", "water"]),
    "tea-cup": ("Tea cup", [
        P("M4 10h13v4a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"),
        P("M17 11.5h1a2.3 2.3 0 0 1 0 4.6h-1.4"),
        P("M3 21.5h15"),
        P("M8 7c-1.1-1.2 1.1-2.3 0-3.5M12.5 7c-1.1-1.2 1.1-2.3 0-3.5")],
        ["tea", "cup", "herbal tea", "drink", "hot drink", "mug"]),
    "clock": ("Clock", [
        C(12, 12, 9),
        P("M12 7v5l3.5 2")],
        ["clock", "time", "session", "duration"]),
    "heart-rate": ("Heart rate", [
        P("M12 20.5C5.5 16.5 3 12.8 3 9.2A4.6 4.6 0 0 1 12 7.8a4.6 4.6 0 0 1 9 1.4c0 3.6-2.5 7.3-9 11.3z"),
        P("M6.5 12h2.7l1.5-2.7 2.6 5.2 1.4-2.5h2.8")],
        ["heart rate", "pulse", "heart", "heartbeat"]),
    "leaf": ("Leaf", [
        P("M20 4C10.5 4 5 8.5 5 15.5c0 1.2.2 2.3.6 3.4C13.5 19 20 14.5 20 4z"),
        P("M3.5 21.5c2.2-6 6.2-10 11.5-12")],
        ["leaf", "natural", "plant", "eucalyptus", "birch", "eco"]),
    "lake-dock": ("Lake and dock", [
        P("M2 10h13.5M5 10v5.5M11 10v5.5M15.5 7.5v8"),
        P("M2 18c1.7-1.2 3.3-1.2 5 0s3.3 1.2 5 0 3.3-1.2 5 0 3.3 1.2 5 0"),
        P("M2 21.2c1.7-1.2 3.3-1.2 5 0s3.3 1.2 5 0 3.3-1.2 5 0 3.3 1.2 5 0"),
        C(19, 5, 2.5)],
        ["lake", "dock", "pier", "swim", "water", "nature"]),
    "hammam-dome": ("Hammam dome", [
        P("M5.5 11.5a6.5 6.5 0 0 1 13 0"),
        P("M12 5V2.5"),
        P("M3 11.5h18M5 11.5V21M19 11.5V21M3 21h18"),
        P("M9.5 21v-3.5a2.5 2.5 0 0 1 5 0V21"),
        P("M9.5 8.7h.01M12 7.6h.01M14.5 8.7h.01")],
        ["hammam", "turkish bath", "dome", "bathhouse", "steam bath"]),
    "hot-tub": ("Hot tub", [
        P("M3 12h18v5.5a3.5 3.5 0 0 1-3.5 3.5h-11A3.5 3.5 0 0 1 3 17.5z"),
        P("M8.5 12v9M15.5 12v9"),
        P("M8 9c-1.2-1.3 1.2-2.4 0-3.7S7.5 3.3 8 2.5M12 9c-1.2-1.3 1.2-2.4 0-3.7s-.5-2 0-2.8M16 9c-1.2-1.3 1.2-2.4 0-3.7s-.5-2 0-2.8")],
        ["hot tub", "tub", "bath", "spa", "jacuzzi", "ofuro"]),
    "hook": ("Hook", [
        R(5.5, 2.5, 5, 10.5, 1.5),
        P("M8 5.5h.01M8 10h.01"),
        P("M8 13v3.5a4.5 4.5 0 0 0 9 0V14")],
        ["hook", "hanger", "wall hook", "hang", "storage"]),
    "soap": ("Soap", [
        R(3, 11, 14.5, 9.5, 3),
        P("M7.5 15.8h5.5"),
        C(17.5, 6, 2.5), C(11.5, 5.5, 1.5)],
        ["soap", "wash", "bubbles", "clean", "bath"]),
    "bath-brush": ("Bath brush", [
        R(2.5, 7.5, 10.5, 4.5, 2.25),
        P("M13 9.8h6.5"),
        C(20.5, 9.8, 1),
        P("M4.7 12v4M7.7 12v5M10.7 12v4")],
        ["bath brush", "body brush", "scrub", "back brush", "wash"]),
    "do-not-machine-wash": ("Do not machine wash", [
        R(4, 3, 16, 18, 2),
        C(12, 13.5, 4),
        P("M14 6.5h.01M17 6.5h.01"),
        P("M2.5 2.5l19 19")],
        ["care", "do not machine wash", "hand wash only", "laundry", "washing machine", "wool care"]),
}

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="{STROKE}" stroke-linecap="round" stroke-linejoin="round">')


def main():
    os.makedirs(os.path.join(ROOT, "svg"), exist_ok=True)
    meta, symbols = [], []
    for name, (title, els, tags) in ICONS.items():
        body = "".join(els)
        svg = f"{HEAD}<title>{title}</title>{body}</svg>\n"
        with open(os.path.join(ROOT, "svg", f"{name}.svg"), "w", encoding="utf-8") as f:
            f.write(svg)
        symbols.append(f'<symbol id="{name}" viewBox="0 0 24 24"><title>{title}</title>{body}</symbol>')
        meta.append({"name": name, "title": title, "file": f"svg/{name}.svg", "tags": tags})
    sprite = ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" fill="none" stroke="currentColor" '
              f'stroke-width="{STROKE}" stroke-linecap="round" stroke-linejoin="round">\n' + "\n".join(symbols) + "\n</svg>\n")
    with open(os.path.join(ROOT, "sprite.svg"), "w", encoding="utf-8") as f:
        f.write(sprite)
    with open(os.path.join(ROOT, "icons.json"), "w", encoding="utf-8") as f:
        json.dump({"name": "Sauna & Banya Icon Set", "version": "1.0.0", "author": "DIVELUX",
                   "homepage": "https://diveluxsaunahat.com", "license": "CC-BY-4.0",
                   "attribution": "DIVELUX — diveluxsaunahat.com", "grid": 24, "stroke": float(STROKE),
                   "count": len(meta), "icons": meta}, f, ensure_ascii=False, indent=2)
    print(len(meta), "icons")


if __name__ == "__main__":
    main()
