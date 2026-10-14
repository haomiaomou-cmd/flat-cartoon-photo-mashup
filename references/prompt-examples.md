# Prompt Examples — Flat Cartoon × Real Photo

Ready-to-paste prompts. Replace bracketed slots with values read off the actual photograph. Always pass the user's photo as `image1` in Mode A.

## Mode A — 1. Street / city (verified template)

```
保持原照片的真实背景完全不变（<城市街景>的背景、光影、构图均保持原样），
但将照片中的人物替换为一张手绘扁平风格插画卡通人物：
粗黑色描边、平涂色块、无渐变无阴影过渡，
简约圆润的五官（小黑点眼睛、简化鼻子和微笑嘴），
人物服装颜色沿用原图（白色衬衫、白色阔腿裤、黑色尖头高跟鞋），
手捧一杯插吸管的咖啡，肩背草编包。
插画人物与真实照片背景形成2D卡通与3D现实的趣味混搭效果，
人物姿态与原图一致（正迈步行走过斑马线）。
背景中的其他行人保持真实照片状态，不要卡通化。
不要添加任何署名、水印或摄影师文字。
```

## Mode A — 2. Travel / mountain / nature

```
保持原照片的自然背景完全不变（<山林步道/峡谷>的背景、树影、光线均保持原样），
将照片中的人物替换为手绘扁平插画卡通人物：
粗黑色描边、平涂色块、无渐变无阴影过渡，
五官极简（黑点眼睛、一条微笑弧线），
服装沿用原图配色（浅黄色背心、米白色长裤、藏青发色），
手部动作与原图一致（<举手掌心朝前打招呼>）。
人物与原照片形成2D卡通与3D实景的趣味混搭，
不要3D渲染感，不要改变背景的光影与落叶质感。
```

## Mode A — 3. Park / lawn (with props)

```
保持原照片的真实背景完全不变（公园草坪、大树、小径均保持原样），
将人物替换为手绘扁平插画卡通人物：粗黑色描边、平涂色块、无渐变无阴影，
极简五官，服装颜色沿用原图（卡其外套、白色内搭、藏青长裙、条纹运动鞋），
一手拿咖啡杯一手拿书。
天空中加一个扁平卡通太阳（黄色圆脸、直线光芒），
草地上散落两三朵扁平小花（粉色花瓣、黄色花心）。
整体是2D插画人物融入3D真实照片的混搭效果，不要3D渲染感。
```

## Mode A — 4. Indoor / café / store

```
保持原照片的室内背景完全不变（<咖啡馆/店铺>的结构、灯光、陈设均保持原样），
将人物替换为手绘扁平插画卡通人物：粗黑色描边、平涂色块、无渐变无阴影过渡，
小黑点眼睛和微笑嘴，服装颜色沿用原图，
旁边加一个扁平白色对话气泡（黑色描边），气泡内写"<2–8个字>"。
2D卡通人物与真实照片混搭，背景保持照片质感，不要整体插画化。
```

## Mode A — 5. Speech bubble / multi-character

```
保持原照片的真实背景完全不变，将画面中的<两个人/人物与宠物>都替换为
同一套手绘扁平插画风格：粗黑描边、平涂色块、无阴影，
但两人姿态不同（<一人举手机拍照，一人比手势>），
服装各自沿用原图配色。
两人头顶各加一个扁平白色对话气泡，文字简短清晰。
整体保持2D卡通与真实照片的混搭效果。
```

## Mode A — 6. No person in the photo (insert a character)

```
保持原照片的真实背景完全不变（<空景描述>），
在画面<前景/中景>位置添加一个手绘扁平插画卡通人物：
站在真实地面上，脚部有扁平的椭圆形影子，
粗黑色描边、平涂色块、无渐变无阴影，
极简五官（黑点眼睛、微笑弧线），服装配色与画面环境协调（<颜色>）。
人物大小与场景透视协调，与真实照片形成2D卡通与3D实景的混搭效果。
```

## Mode B — character cut-out (transparent background)

Generate first, then composite with `scripts/composite_flat_character.py`.

```
单个全身手绘扁平插画卡通人物，<正面/侧面/背面>站姿，<具体姿态>，
粗黑色描边、平涂色块、无渐变无阴影过渡，
简约圆润的五官（小黑点眼睛、简化鼻子、微笑嘴），
服装：<garments with colours>，<手持道具>。
透明背景，不要背景元素，不要地面阴影，不要文字，
纯平涂色块风格，不要3D渲染，不要动漫大眼。
```

Then:

```bash
python scripts/composite_flat_character.py \
  --photo street.jpg --character figure.png --out street-cartoon.png \
  --height-ratio 0.62 --anchor 0.52,0.94 --shadow --feather 1
```

## Fast reference: scene → props → mandatory clause to add

| Scene | Plausible flat props | Extra clause |
|---|---|---|
| Street / city | Clouds, small flat logo-free signs, ground shadow | `背景中的其他行人保持真实照片状态，不要卡通化` |
| Park / lawn | Smiling sun, daisies, clouds, speech bubble | `草地上散落两三朵扁平小花` |
| Mountain / forest | Rays of light as flat lines, birds as flat "m" shapes | `保持树影和自然光斑的真实质感` |
| Beach / seaside | Flat sun, flat gulls, hatched sand shadow | `保留海面真实的波纹与反光` |
| Indoor / café | Speech bubble only | `保持室内真实光线与陈设` |
| Night / neon | Flat moon, flat stars | `保留真实的霓虹反光与暗部噪点` |
