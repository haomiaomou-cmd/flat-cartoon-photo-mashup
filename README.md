# flat-cartoon-photo-mashup

> 真人照片 × 扁平插画卡通人物混搭风格 —— WorkBuddy / Claude Code Agent Skill

把一张真实照片变成「实景照片 + 手绘扁平卡通人物」的混搭插画：照片本身（背景、光影、景深、路人）一寸不改，画面里的人物被重画成粗黑描边、平涂色块、极简五官的扁平卡通，两者之间的接缝就是这张图的趣味所在。

> 本仓库已附带 `assets/` 风格参考图与示例成品图，来源与版权说明见文末 [assets 说明](#assets-说明)。

---

## 这是什么

一个可复用的 Agent Skill。装上之后，你只要丢一张照片说「用这个风格画一张」，Agent 就会自动：

1. 读取照片（人物服装配色、姿态、脚底位置、背景类型、光位）；
2. 按 skill 里沉淀的风格 DNA 写中文提示词，走图生图；
3. 质检（背景是否仍像照片、人物是否真扁平、五官是否过细、有无乱加署名/水印）；
4. 清除生成链路必带的角落水印。

## 风格 DNA（七条）

| # | 规则 | 说明 |
|---|---|---|
| 1 | 两个世界 | 背景必须保持摄影质感：颗粒、散景、过曝、杂物、路人一个不删 |
| 2 | 粗黑均匀描边 | 闭合黑色轮廓，线宽一致（1000px 高画布约 3–5px），像矢量而非铅笔草稿 |
| 3 | 纯平涂、零明暗 | 每块颜色一个纯色，无渐变、无投影、无软光、无排线 |
| 4 | 极简五官 | 黑点眼 + 一条微笑弧，可选腮红；不画睫毛、眼白、结构 |
| 5 | 姿态照抄 | 头身比可微调，但站姿、朝向、接地位置必须与原图一致 |
| 6 | 配色借照片 | 4–7 色，取自原照片里已有的颜色 |
| 7 | 涂鸦道具闯入 | 扁平太阳、云、小花、对话气泡、脚底椭圆影子，1–3 个 |

刻意不做的：卡通写实化、背景插画化、3D/CGI 渲染、动漫大眼、柔光边缘。

## 两种工作模式

| 模式 | 适用 | 代价 |
|---|---|---|
| **A 一步式图生图**（默认） | 用户给照片，要求换风格 | 约 5–10 积分/张，背景可能被轻微重新演绎 |
| **B 保原图合成** | 背景必须像素级不动，或模式 A 反复失败 | 先生成透明背景人物抠图，再用 `scripts/composite_flat_character.py` 合成；脚本输出前后 md5 证明原图未动 |

## 提示词模板（模式 A）

```
保持原照片的真实背景完全不变（<场景>的背景、光影、构图均保持原样），
但将照片中的人物替换为一张手绘扁平风格插画卡通人物：
粗黑色描边、平涂色块、无渐变无阴影过渡，
简约圆润的五官（小黑点眼睛、简化鼻子和微笑嘴），
人物服装颜色沿用原图（<服装与颜色>），<手中/身上道具>。
插画人物与真实照片背景形成2D卡通与3D现实的趣味混搭效果，
人物姿态与原图一致（<姿态描述>）。
```

四条强制子句一个都不能少：保背景 / 保平涂 / 保混搭感 / 保姿态。更多场景模板见 [`references/prompt-examples.md`](references/prompt-examples.md)。

## 水印清除工具箱

这条图生图链路几乎每次都会在右下角加一个角落标记，提示词拦不住；用户照片本身也常自带水印。仓库里沉淀了四级方案（按优先级）：

1. **同图克隆回填** —— 高频纹理（草叶、砂石）上最稳
2. **原照片映射回贴** —— 水印区域大、跨多种材质时最稳
3. **cv2 inpaint** —— 单一材质上的文字；暗底白字用亮度差分掩膜，彩底白字用饱和度差分掩膜
4. **同行取样 + 噪声 + 羽化** —— 无 numpy/cv2 时的兜底

细节、参数与失败模式见 [`SKILL.md`](SKILL.md)。

## 安装

**独立仓库：**

```bash
git clone https://github.com/<你的账号>/flat-cartoon-photo-mashup.git
cp -r flat-cartoon-photo-mashup ~/.workbuddy/skills/
```

**作为 `skills` 集合仓库的子目录：**

```bash
git clone https://github.com/<你的账号>/skills.git
cp -r skills/flat-cartoon-photo-mashup ~/.workbuddy/skills/
```

装好后目录应为 `~/.workbuddy/skills/flat-cartoon-photo-mashup/SKILL.md`，重启会话即可被识别。

## 目录结构

```
flat-cartoon-photo-mashup/
├── SKILL.md                        # 主工作流（风格 DNA、双模式、质检表、水印工具箱）
├── references/
│   ├── style-analysis.md           # 配色/线条/五官/道具规格 + 逐图拆解 + 失败模式
│   └── prompt-examples.md          # 街景/山野/公园/室内/无人物/抠图 六类提示词模板
├── scripts/
│   └── composite_flat_character.py # 模式 B 合成器（缩放、锚点、镜像、羽化、地面阴影、md5 校验）
└── assets/                         # 风格参考图（见下方说明）
```

`scripts/composite_flat_character.py` 依赖 Pillow：

```bash
python composite_flat_character.py --photo street.jpg --character figure.png \
    --out street-cartoon.png --height-ratio 0.62 --anchor 0.52,0.94 --shadow --feather 1
```

## assets 说明

仓库**已包含** `assets/` 下的参考图与示例图：

| 文件 | 内容 |
|---|---|
| `reference-park-coffee.jpg` | 扁平人物 + 微笑太阳 + 小雏菊道具，粗描边、扁平发块 |
| `reference-cyclist-street.jpg` | 扁平人物骑扁平自行车行进在真实街道，示范「道具载具」画法 |
| `reference-bench-reader.jpg` | 扁平人物坐在真实公园长椅，配云朵与对话气泡道具 |
| `reference-kayak-drypath.jpg` | 扁平人物在干涸碎石路上划扁平皮划艇，示范反差能推到多远 |
| `example-output-crossing.jpg` | 本 skill 模式 A 的实测成品（白衬衫女士过斑马线） |

版权提示：参考图来自网络截图（部分带 CapCut、reNote 等平台水印），版权归原作者，仅作风格分析依据，不随本仓库授权；示例图由真人照片衍生而来，如需公开传播请自行确认肖像权。

自行扩充分时按此命名即可被 SKILL.md 直接引用：

```
assets/reference-*.jpg      # 风格参考
assets/example-output-*.jpg # 你自己跑出来的成品
```

## 适用与不适用

**适合**：街拍、旅行、通勤、公园、室内等有人物的照片；想要「时间静止」反差（清晰卡通 vs 虚化人潮）的构图；同一场景批量出系列图。

**不适合**：纯风景照（需改成模式 B 或显式插入人物）；要求人物与照片光影完全融合的光影向需求；需要精确复刻复杂载具/机械结构的场景（建议模式 B）。

## License

文本与代码：MIT，见 [LICENSE](LICENSE)。
`assets/` 下的参考图版权归原作者，不随本仓库授权。
