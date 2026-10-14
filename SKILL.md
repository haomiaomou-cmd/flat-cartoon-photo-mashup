---
name: flat-cartoon-photo-mashup
description: Turns a real photograph into a "real photo × flat cartoon character" mash-up — the photographic scene (background, lighting, depth of field) stays intact while the person in it is redrawn as a hand-drawn flat cartoon: thick even black outline, solid unshaded colour fills, minimal dot-eyes-and-smile face, plus optional doodle props such as a sun, clouds, flowers or a speech bubble. This skill should be used when the user supplies a photo and asks to cartoonize the person in it, wants "扁平插画", "手绘卡通人物", "真人照片加插画人物", "2D 人物融入实景照片", "flat illustration on photo", "cartoon me in this photo"; when the user asks to summarise or replicate that 2D-cartoon-on-photo art style; or when the user provides reference images in that style and asks for another image like them. Covers style analysis of reference images, one-step generative image-to-image, and a photo-preserving two-stage composite mode.
agent_created: true
---

# Flat Cartoon × Real Photo Mash-up

## Purpose

Produce images where a hand-drawn-flat cartoon figure stands inside a genuine photograph. The appeal is the deliberate seam between the two halves:

- the **photo** is sharp, correctly lit, with real depth of field, real texture, real clutter;
- the **character** is flat: thick uniform black outline, solid unshaded fills, five-minute face.

Both halves must stay pure. A photo that looks painted, or a character with gradients and soft shadows, kills the effect. The character should look cut out and pasted in — that is the joke, not a flaw.

## When to use

Trigger on requests such as:

- "把这张照片里的人画成插画 / 卡通" · "帮我把照片变成手绘插画风"
- "生成一张同风格的图片" after being shown flat-cartoon-on-photo references
- "总结这个风格" for images that mix photography with flat vector-style characters
- "真人照片＋扁平插画人物" · "加个小人在照片里" · "flat illustration on a real photo"
- Any request to reproduce a reference set built from real photos plus thick-outline unshaded cartoon people

## Style DNA — the seven rules

Every rule is load-bearing. Read the reference images in `assets/` before generating if the look is not already obvious.

1. **Two separate realities.** Background stays a photograph — keep its grain, bokeh, blown highlights, litter, road markings, other passers-by. Never stylise the photo into an illustration.
2. **Thick, even black contour.** A closed, confident black outline around the whole figure and around every internal colour boundary. Weight is consistent, roughly 3–5 px at 1000 px canvas height. Cleaner and calmer than a marker doodle — this is a *vector-like* line, not a sketchy one.
3. **Solid fills, zero shading.** Every region is one flat opaque colour. No gradients, no cast shadow, no soft light, no texture, no hatching. Highlights are separate flat shapes, if used at all.
4. **Minimal face.** Small black dot or short-oval eyes, one simplified nose stroke or none, a single smile arc, optional blush dots. No eyelashes, no eyeballs with whites, no rendering. Expression comes from a 3 px property of the mouth line.
5. **Simplified anatomy.** Slightly stylised proportion (bigger head, longer limbs), simple shape-language hands (often mitten-like), hair as a few flat masses — but the pose is copied faithfully from the photo. The figure must stand in the same stance, on the same ground plane, at the same scale as the original subject.
6. **Palette borrowed from the photo.** Keep the subject's real clothing colours so the figure belongs; keep the total palette small (4–7 colours), pulled from what is already in the scene.
7. **Doodle props intrude.** Flat extras float in the real scene: a smiling sun with radial rays, white cloud outlines, small daisies, a speech bubble, a hatched ground shadow under the feet. One to three props, never more.

Deliberately absent: photorealism in the character, painted texture in the background, 3D/CGI rendering, anime-style detailed eyes, airbrushed soft edges.

## Step 1 — read the photograph

Before writing any prompt, inspect the supplied photo and record:

| What to record | Why |
|---|---|
| Subject's clothing colours and carried items (bag, cup, hat) | Rule 6 — the palette must be copied, not invented |
| Subject's pose and facing direction | Rule 5 — the cartoon must inherit it |
| Subject's pixel height and feet position | Keeps the figure on the right ground plane at the right scale |
| Background type (street / park / indoor / mountain path) | Decides which props can plausibly float in it |
| Light direction and colour temperature | The figure's palette should agree with the light around it |

Report this list back in one or two lines so the user can correct you before credits are spent.

## Step 2 — choose a mode

| Signal | Mode |
|---|---|
| User supplies a photo and asks for the style (default) | **A — one-step generative** |
| "不要改变照片背景" / "只换人物" / "background must stay exactly as is" | **B — photo-preserving composite** |
| The character is not in the photo (empty landscape, object only) | **B**, or **A** with an explicit insertion prompt |
| Repeated failures to keep the background photographic | **B** |

State the chosen mode in one line before starting. Mention credit cost for Mode A first — roughly 5–10 credits per image; Mode B costs credits only for the character cut-out.

**Output count:** one image per pass. Offer variations instead of pre-generating a grid.

## Mode A — one-step generative image-to-image

Call the image generation tool with the user's photo as `image1`, `input_fidelity: "high"`, `quality: "high"`, and the size closest to the photo's own aspect ratio (`1024x1536` portrait, `1536x1024` landscape, `1024x1024` square).

Fill this template — every bracket matters, and all four mandatory clauses must be present:

```
保持原照片的真实背景完全不变（<scene description> 的背景、光影、构图均保持原样），
但将照片中的人物替换为一张手绘扁平风格插画卡通人物：
粗黑色描边、平涂色块、无渐变无阴影过渡，
简约圆润的五官（小黑点眼睛、简化鼻子和微笑嘴），
人物服装颜色沿用原图（<garment list with colours>），
<one or two held/worn props from the photo>。
插画人物与真实照片背景形成2D卡通与3D现实的趣味混搭效果，
人物姿态与原图一致（<pose description>）。
```

Mandatory clauses:
- `保持原照片的真实背景完全不变` — protects the photograph;
- `粗黑色描边、平涂色块、无渐变无阴影过渡` — forces the flat treatment;
- `插画人物与真实照片背景形成2D卡通与3D现实的趣味混搭效果` — keeps the deliberate seam instead of blending both into one soft style;
- `人物姿态与原图一致` — stops the model re-staging the pose.

Add when the background contains other people: `背景中的其他行人保持真实照片状态，不要卡通化`. Add when the frame risks invented credits: `不要添加任何署名、水印或摄影师文字`.

**Verified call.** Input: a 1200×1800 street photo of a woman in a white shirt and white wide-leg trousers crossing a zebra crossing, carrying a straw bag and a takeaway coffee. Size `1024x1536`, `input_fidelity: "high"`, `quality: "high"`. Result: background street, bokeh, passing pedestrian and crosswalk stripes all preserved; the subject became a flat black-outlined cartoon in the same whites, mid-stride on the same stripe, coffee cup and bag redrawn in flat style. See `assets/example-output-crossing.jpg`.

### Mode A quality control

| Observed | Fix |
|---|---|
| Background looks painted or filtered | Raise `input_fidelity`, re-emphasise `保持原照片的真实背景完全不变` |
| Character has gradients / soft shadows | Re-emphasise `无渐变无阴影过渡`, `平涂色块` |
| Face came out with detailed anime eyes | Add `不要动漫大眼，不要睫毛`, re-emphasise `小黑点眼睛` |
| Outline too thin or sketchy | Add `粗黑描边、线条干净均匀，不要铅笔草稿感` |
| Extra people in the background also cartoonised | Add `背景中的其他行人保持真实照片状态` |
| Pose or framing drifted | Regenerate once; if it drifts again, switch to Mode B |
| Invented signature or watermark text | Regenerate with the no-watermark clause, or remove it (recipe below) |

**Removing an invented watermark** (verified, two methods — prefer the first):

1. **Re-paste from the original photo (best for large or multi-material watermark areas).** The generated background is copied from the user's photo, so map the watermark box back into the original photo (separate horizontal/vertical scale factors — generated canvas is 1024×1536, the photo may have a slightly different aspect), crop that clean region, resize to the box, and paste with a feathered mask (inset ≈16 px, GaussianBlur ≈9). No tone matching is usually needed. This survives striped, gradient and multi-material corners where both inpaint and patch-copying fail.
2. **cv2 inpaint (good for text on one uniform material).** Crop the corner region, build a mask of the bright text: `bg = cv2.medianBlur(gray, 21)`, `mask = (gray - bg > 12)` dilated 5×5 twice, then `cv2.inpaint(roi, mask, 5, cv2.INPAINT_TELEA)`. If a semi-transparent smear survives, rerun on the residue with threshold 6, medianBlur 31, 7×7 dilation. When the text sits on more than one material (e.g. dark concrete *and* a lit edge), a brightness mask fails — try `mask = (S < 70) & (V > 115)` in HSV to catch the desaturated grey overlay; if the area is large, inpainting produces mush and method 1 is required.
3. **Row-sampling fallback (no numpy/cv2 needed).** Fill the watermark box row by row with colour sampled from a clean margin of the *same* row, add ±6 per-pixel noise, then Gaussian-blur only the patch (radius ≈2) through a feathered mask (radius ≈4). Only use on uniform ground material — on zebra stripes or gradients it leaves visible seams.

Always check the bottom-right corner after every generation: this image-to-image pipeline adds an "AI生成 WORKBUDDY" corner mark on nearly every run, and prompt clauses cannot suppress it.

## Mode B — photo-preserving composite (background provably untouched)

Use when the photo must not change at all, or when Mode A keeps failing.

1. **Generate only the character**, on a transparent background: same style clauses as Mode A, plus `单个全身卡通人物，<pose>，透明背景，不要背景元素，不要地面阴影`. Save the PNG with alpha.
2. **Composite with `scripts/composite_flat_character.py`.** It scales the cut-out to a target height ratio, anchors its feet at a normalised point on the photo, optionally mirrors it, adds a soft ground shadow, and writes a NEW file — the source photo is never written to.
3. **Verify the source** — the script prints the md5 before and after; report that they match.

```bash
python scripts/composite_flat_character.py \
  --photo photo.jpg --character character.png --out result.png \
  --height-ratio 0.62 --anchor 0.5,0.93 --shadow
```

`--anchor` is the normalised `x,y` of the figure's feet; `--flip` mirrors horizontally; `--feather 1` softens the cut-out edge by 1 px to hide anti-aliasing halos. Match the height ratio to the person actually in the photo, not to a fixed default.

## Variations and extras

- **Multi-character**: several flat figures at different depths in one photo. Vary pose and props; identical treatment of every figure reads as lazy. Keep the flatness uniform.
- **Doodle props**: append to the prompt — `天空中加一个扁平卡通太阳和小白云` / `画面里散落几朵扁平小花` / `人物旁边一个扁平对话气泡，里面写"<short line>"`. Keep all props in the same flat, thick-outline language.
- **Speech bubble**: keep text short (2–8 characters), one flat colour, black outline. Garbled text is the most common failure — shorten and regenerate.
- **Object instead of person**: the same formula works on a statue, mannequin or statue-like animal — "replace the subject with a flat cartoon version of <object>".
- **Palette swap series**: change only the character's clothing palette while the photo stays; useful for producing a set.

## Bundled resources

- `assets/reference-park-coffee.jpg` — flat figure with a smiling sun, daisy props, thick outline, flat hair masses.
- `assets/reference-cyclist-street.jpg` — flat figure riding a flat bicycle on a real street; blueprint for drawing a *prop vehicle* in flat style.
- `assets/reference-bench-reader.jpg` — flat figure sitting on a real park bench; cloud props and a speech bubble.
- `assets/reference-kayak-drypath.jpg` — flat figure paddling a flat kayak on a dry gravel road; splash drawn as flat blobs. Shows how far the mismatch can be pushed.
- `assets/example-output-crossing.jpg` — verified Mode A output for this skill.
- `references/style-analysis.md` — colour, line-weight and prop specifications plus a per-reference breakdown.
- `references/prompt-examples.md` — ready-to-paste prompts by scene type, plus a Mode B character cut-out prompt.
- `scripts/composite_flat_character.py` — Mode B compositor (Pillow).

## Presentation

Present with `present_files`. In one line, name the mode used, what the character inherits from the photo (clothing, pose, props), and which flat extras were added. In Mode B, state that the source photo was not modified and give the md5 check result. Then offer one concrete next idea — a second figure in the scene, a speech-bubble line, or the same photo in a different palette.
