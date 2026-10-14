# Style Analysis — Flat Cartoon × Real Photo

Detailed specifications distilled from a six-image reference set. Load this file when the compressed Style DNA in `SKILL.md` is not enough to hit the look.

## Per-reference breakdown

| Reference | Scene | Character treatment | Flat extras | Takeaway |
|---|---|---|---|---|
| `reference-park-coffee.jpg` | Sunny park, big cedar, pond | Long olive-green coat, dark navy culottes, chunky trainers, sunglasses perched on hair; holds a flat takeaway cup with a straw and a blue book | Smiling sun with 12 straight radial rays; three pink daisies scattered on the real grass | Props are drawn in the *same* flat language as the figure, never as stickers with drop shadows |
| `reference-cyclist-street.jpg` | European street, zebra crossing, buildings | Orange-haired girl in a red dress on a flat blue bicycle; empty flat shadow blob under the wheels | Straw basket on the handlebar with flat red flowers | The *vehicle* is fully redrawn in flat style — the hardest element; expect to iterate |
| `reference-bench-reader.jpg` | Park, lawn, path, trees | Yellow tee, blue jeans, sunglasses, small flat horns; sits on a real wooden bench | Four flat white clouds in the real sky; a large white speech bubble with handwritten text and a wink emoji; small daisies on the grass | Text inside a bubble works if kept short (three short lines) |
| `reference-kayak-drypath.jpg` | Dry gravel mountain road | Dark hooded figure paddling a flat yellow kayak with two flat oars | Flat white splash blobs and puddles under the boat | Pushing the mismatch to absurdity is allowed and intentional |
| `example-output-crossing.jpg` (this skill's own output) | City street, glass storefront, zebra crossing | White shirt, white wide-leg trousers, black pointed shoes, straw bag, coffee cup with straw — all redrawn flat | Background pedestrian left photographic | Mode A preserves background detail, including a second person, when told explicitly |

## Colour specification

- **Palette size**: 4–7 colours total for the figure. More than that and it stops reading as flat.
- **Saturation**: medium-low to medium. The references use muted olive, brick red, mustard yellow, navy, off-white — not neon.
- **Values**: one dark anchor (navy / charcoal / brick), one mid tone, one near-white. The black contour is the darkest element and always reads clearly against the fill.
- **Skin**: a single flat tone, often lighter than the photo's real skin. Optional blush: two flat pink ellipses.
- **Hair**: one to three flat masses, never strand-by-strand. A single darker crescent where the part is.
- **Background agreement**: sample 2–3 colours from the real photo and reuse them in the figure so the characters sit in the same light.

## Line specification

- Weight: uniform; approximately 3–5 px on a 1000 px-tall canvas (so ~0.3–0.5 % of height). Thicker on the outer silhouette than on interior details is acceptable and common.
- Colour: pure black or near-black (`#111111`–`#1A1A1A`). Never brown, never soft grey.
- Corners: rounded, generous. No sharp vector corners, no tapered brush strokes.
- Consistency: the same weight everywhere — this is what separates this style from marker doodles, whose line weight wobbles deliberately.

## Face specification

| Feature | Rendering |
|---|---|
| Eyes | Solid black dots or short vertical ovals, 3–5 px across at 1000 px height |
| Brows | Usually absent; a single short stroke when the expression needs it |
| Nose | A 3–6 px stroke, or omitted entirely |
| Mouth | One arc; changes curvature to carry the whole expression |
| Blush | Two flat ellipses, optional |
| Glasses | Flat opaque black or dark-navy lenses, drawn as filled shapes with the black contour |

## Prop specification

- Props obey the same thick contour and flat fill as the figure — a sun is a flat yellow circle with a dot face and straight line rays, not a gradient orb.
- Keep props *in front of* photographic detail that supports them: daisies on real grass, clouds in a real sky, splash on a real puddle.
- Ground contact: a flat elliptical shadow blob in a slightly darker version of the ground's colour, placed under the feet. Without it the figure floats.
- Speech bubbles: white flat fill, black contour, short text in a rounded handwritten face, tail pointing to the speaker.

## Failure modes seen in practice

- Background rendered as a soft illustration → the whole image unifies into one style and the joke disappears.
- Character given a gradient on the coat → looks like a mobile-game sticker, not a flat cartoon.
- Detailed anime eyes → the figure becomes a different genre entirely.
- Figure scale drifting from the original subject → ground contact breaks; also a common failure for wide-angle photos.
- Full-body redraw of a *vehicle* attempted in a single pass → wheels and frame usually come out warped; expect two or three iterations.
