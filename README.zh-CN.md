# PrintCraft 插件

预发布 **0.1.0-dev.6**，包含六项上游独立技能和一项插件本地 `printcraft-harness`。技能源快照逐文件绑定摘要，另有来源 suite 版本/摘要；`source-release.lock.json` 锁定真实技能源仓库、tag、commit、版本与 78 项文件摘要；`candidate-source.json` 保留为兼容快照登记，状态为 published-release。

默认任务入口 **printcraft-use**，专业入口按名称显式调用；Harness 负责路由、状态和产物展示。Codex 加载后名称带插件命名空间，例如 `$printcraft:printcraft-cli-setup`。其他宿主尚未实际验收。

## 当前能力

- 独立版本化 execution/1、verification/1 协议，未知协议拒绝。
- UNKNOWN/部分失败只读对账，不换 runId 重放；零退出仍需产物和视觉验收。
- 复用既有授权，新增原件覆盖、真实打印或外部范围才确定新授权。
- 同包六项独立执行脚本，安装后不依赖开发仓库、兄弟项目或源码构建。
- portable `plugin.json` 与生成的 `.codex-plugin/plugin.json` 保持同名同版本。
- 来源、包完整性、固定运行时、宿主加载、模型实际选用和业务结果分别记录证据。

## 本地入口与校验

从宿主实际加载路径确定 `PLUGIN_ROOT`；每个上游技能都有自己的 SKILL.md、references、examples 和脚本。

```bash
python3 -I -B "$PLUGIN_ROOT/skills/printcraft-harness/scripts/harness.py" route pages
python3 -I -B "$PLUGIN_ROOT/skills/printcraft-harness/scripts/harness.py" route general --explicit printcraft-cli-inspect
python3 -I -B "$PLUGIN_ROOT/skills/printcraft-harness/scripts/harness.py" delegate status "$TASK_DIR/receipt.json"
python3 -I -B "$PLUGIN_ROOT/skills/printcraft-harness/scripts/harness.py" show "$TASK_DIR/receipt.json"
python3 -I -B scripts/validate_package.py
python3 -I -B -m unittest discover -s tests
python3 -I -B scripts/generate_host_manifest.py
```

上游增量同步工具由 **printcraft-skills** 维护：在其源码仓库运行 `scripts/sync_local_snapshot.py --plugin-root "$PLUGIN_ROOT"`。同步拒绝用户漂移、源删除、跨域和正式身份降级，保留本地 Harness。该开发工具不是安装后运行依赖。

`check_update.py` 只读检查版本/协议兼容及任务数据必须位于包缓存之外；不迁移任务数据，不把旧/不兼容回执重新初始化。正式发行来源锁需要可核验 tag/commit/版本/摘要；当前已实际核对远端 tag、公开预发布、下载制品及 78 项文件；静态校验仍只报告离线完整性，远端证据见 remote-source-dev6.json。

## 证据与未完成门禁

详见 [实施验收报告](docs/verification/implementation-2026-10-08.md)、[宿主支持矩阵](docs/host-support.md)、[证据索引](docs/verification/evidence-index.json)和[任务](openspec/changes/harden-printcraft-plugin-delivery/tasks.md)。

固定原生页面任务和专项样例已运行。签名样例为未受信任自签名；PDF/A 是原生有限子集。固定原生仍拒绝中文 OCR；显式 Tesseract 简繁后端已在 macOS arm64 的原创多页扫描件验证。PDF 阅读顺序与长句搜索存在限制，见 [专项报告](docs/verification/external-ocr-2026-10-08.md)。五平台直接原生/英语 OCR 已通过；包装器仍仅 macOS arm64，手机真机交付仍开放。真实 ArtCraft 本机交接和定向返工已有独立证据。当前 CLI 对 gpt-6-astra 的兼容限制与可用模型测试结果分别记录。

GitHub 与市场发行状态见 project-status.json 和 docs/verification/release-2026-10-08.md；预发布不代表全部专项门禁通过。

## 市场预发布安装

```bash
codex plugin marketplace add partme-ai/full-aigc-plugins
codex plugin add printcraft@full-aigc-plugins
```

Codex 为实测目标。ZCode/Kimi 清单仅按 portable 元数据生成，加载与模型调用 NOT_RUN；市场候选用于受控测试。
