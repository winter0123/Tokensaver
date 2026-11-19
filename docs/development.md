# Adding a plugin

1. Keep the plugin in its **own** GitHub repository. Do not copy its source, native releases, or runtime dependencies into `Tokensaver`.
2. Publish tested plugin metadata in that repository (`plugin.json`, and for Claude Code `.claude-plugin/plugin.json` where appropriate). Include `skills/` and MCP config if supported. Test its runtime setup independently.
3. Add exactly one entry to `.agents/plugins/marketplace.json` using a documented Codex Git source type (`url` or `git-subdir`) and one entry to `.claude-plugin/marketplace.json` with a documented Claude Code Git source (`github` or `git-subdir`). Keep plugin IDs identical across platforms, with stable kebab-case names.
4. Pin the source to a reviewed release ref or SHA when ready for stable distribution; do not assume that moving `main` will be safe for every user. The initial Docs entry tracks `main` while source packaging is being developed.
5. Update the README plugin table and run the catalog validation script. Test real plugin installation and MCP startup on supported operating systems before claiming full compatibility.
6. Each plugin owns its GitHub Actions, build artifacts, release notes, and cache. A release of one plugin must not rebuild or uninstall another.

The catalog does **not** execute install scripts. Platform-specific runtime downloads must be implemented and tested inside the independent plugin's distribution flow; never silently download executable code from a skill or MCP prompt.
