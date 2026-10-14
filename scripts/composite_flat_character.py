#!/usr/bin/env python3
"""Composite a transparent-background flat cartoon character onto a real photo.

The source photograph is NEVER modified: it is read, the character is pasted on a
copy, and the copy is written to --out. The script prints md5 hashes of the source
photo before and after so the caller can prove the original is untouched.

Requires Pillow.

Examples
--------
# paste the figure at 62% of the photo height, feet at 52%/94% of the frame
python composite_flat_character.py --photo street.jpg --character figure.png \
    --out street-cartoon.png --height-ratio 0.62 --anchor 0.52,0.94 --shadow

# mirror the figure and soften the cut-out edge by 1 px
python composite_flat_character.py --photo p.jpg --character c.png --out o.png \
    --flip --feather 1
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")


def md5(path: str) -> str:
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_pair(value: str, name: str) -> tuple[float, float]:
    try:
        a, b = value.split(",")
        return float(a), float(b)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{name} must be 'x,y' (got {value!r})")


def load_character(path: str) -> Image.Image:
    img = Image.open(path).convert("RGBA")
    # If the image is fully opaque, warn: it was probably not generated with alpha.
    alpha = img.getchannel("A")
    if alpha.getextrema()[0] == 255:
        print(
            "WARNING: character PNG has no transparency. Regenerate it on a "
            "transparent background, or the whole rectangle will be pasted.",
            file=sys.stderr,
        )
    return img


def trim_alpha(img: Image.Image, threshold: int = 8) -> Image.Image:
    """Crop to the bounding box of non-transparent pixels."""
    box = img.getchannel("A").point(lambda v: 255 if v > threshold else 0).getbbox()
    return img.crop(box) if box else img


def make_shadow(
    size: tuple[int, int],
    opacity: int,
    blur: int,
    colour: tuple[int, int, int] = (0, 0, 0),
) -> Image.Image:
    """Flat elliptical contact shadow on its own RGBA layer."""
    w, h = size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.ellipse((0, 0, w - 1, h - 1), fill=colour + (opacity,))
    if blur > 0:
        layer = layer.filter(ImageFilter.GaussianBlur(blur))
    return layer


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--photo", required=True, help="source photograph (read-only)")
    ap.add_argument("--character", required=True, help="transparent-background PNG cut-out")
    ap.add_argument("--out", required=True, help="output path (a NEW file)")
    ap.add_argument(
        "--height-ratio",
        type=float,
        default=0.6,
        help="character height as a fraction of photo height (default 0.6)",
    )
    ap.add_argument(
        "--anchor",
        type=lambda v: parse_pair(v, "anchor"),
        default=(0.5, 0.9),
        help="normalised x,y of the character's feet in the photo (default 0.5,0.9)",
    )
    ap.add_argument("--offset", type=lambda v: parse_pair(v, "offset"), default=(0.0, 0.0),
                    help="extra pixel offset 'dx,dy' applied after anchoring")
    ap.add_argument("--flip", action="store_true", help="mirror the character horizontally")
    ap.add_argument("--feather", type=float, default=0.0,
                    help="blur the cut-out alpha edge by this many px to hide halos")
    ap.add_argument("--shadow", action="store_true", help="add a flat ground shadow under the feet")
    ap.add_argument("--shadow-width", type=float, default=0.55,
                    help="shadow width as a fraction of the character width (default 0.55)")
    ap.add_argument("--shadow-opacity", type=int, default=70, help="shadow alpha 0-255 (default 70)")
    ap.add_argument("--shadow-blur", type=int, default=6, help="shadow gaussian blur radius (default 6)")
    ap.add_argument("--rotate", type=float, default=0.0, help="rotate the character by this many degrees")
    args = ap.parse_args()

    for path in (args.photo, args.character):
        if not os.path.isfile(path):
            sys.exit(f"not found: {path}")
    if os.path.abspath(args.photo) == os.path.abspath(args.out):
        sys.exit("refusing to write over the source photo; choose a different --out")

    before = md5(args.photo)

    photo = Image.open(args.photo).convert("RGBA")
    pw, ph = photo.size

    char = trim_alpha(load_character(args.character))
    if args.flip:
        char = char.transpose(Image.FLIP_LEFT_RIGHT)
    if args.rotate:
        char = char.rotate(args.rotate, expand=True, resample=Image.BICUBIC)

    target_h = max(1, int(round(ph * args.height_ratio)))
    scale = target_h / char.height
    target_w = max(1, int(round(char.width * scale)))
    char = char.resize((target_w, target_h), Image.LANCZOS)

    if args.feather and args.feather > 0:
        alpha = char.getchannel("A").filter(ImageFilter.GaussianBlur(args.feather))
        char.putalpha(alpha)

    ax, ay = args.anchor
    cx = int(round(pw * ax + args.offset[0]))
    by = int(round(ph * ay + args.offset[1]))
    paste_x = cx - target_w // 2
    paste_y = by - target_h

    canvas = photo.copy()

    if args.shadow:
        sw = max(8, int(round(target_w * args.shadow_width)))
        sh = max(4, int(round(sw * 0.16)))
        shadow = make_shadow((sw, sh), args.shadow_opacity, args.shadow_blur)
        sx = cx - sw // 2
        sy = by - sh // 2
        canvas.alpha_composite(shadow, (sx, sy))

    canvas.alpha_composite(char, (paste_x, paste_y))
    canvas.convert("RGB").save(args.out)

    after = md5(args.photo)
    print(f"photo      : {args.photo}")
    print(f"character  : {args.character} -> {target_w}x{target_h} px")
    print(f"output     : {args.out}")
    print(f"source md5 : {before}")
    print(f"after  md5 : {after}")
    print("SOURCE UNCHANGED" if before == after else "WARNING: SOURCE PHOTO CHANGED")
    return 0 if before == after else 1


if __name__ == "__main__":
    raise SystemExit(main())
