# Installing TokenSaver Docs from Tokensaver

This marketplace is a catalog of independent plugins; it does not bundle all plugin engines or change any existing installations.

## Codex

```sh
codex plugin marketplace add winter0123/Tokensaver
```

Open the plugin manager and install `tokensaver-docs@tokensaver`. The Git source points to `marketplace-plugin/`, which contains the required `.codex-plugin/plugin.json`, its skill and native CLI launchers. No manual MCP server registration is needed.

## Claude Code

```sh
claude plugin marketplace add winter0123/Tokensaver
claude plugin install tokensaver-docs@tokensaver
```

The Git source points at the same `marketplace-plugin/` directory, including its `.claude-plugin/plugin.json` and SKILL.

## OpenCode

OpenCode does not consume Codex/Claude marketplace files. Its own Git package is installed independently:

```sh
opencode plugin add 'github:winter0123/tokensaver-docs#main::path:plugins/opencode'
```

The package includes its JS plugin, research-routing settings, skill and native runtime resolver. No manual MCP server registration is required. The existing OpenCode native ZIP installer remains another fully self-contained option.

## First use and runtime download

The new Codex/Claude SKILL + CLI package runs `scripts/run.sh` on macOS or `scripts/run.ps1` on Windows. OpenCode calls its native runtime resolver. When needed, these launchers obtain a **pinned v0.5.6** platform-specific artifact from `winter0123/tokensaver-docs` GitHub Releases, verify it against the published SHA-256 checksums, and store it in a per-user cache. They do **not** run another agent installer or edit MCP settings. No global `PATH` modification is required.

- macOS: arm64/x64
- Windows: x64
- Linux: no packaged native binary; install from source separately.

Network connectivity, firewall rules and OS execution policies may affect the download or launch. A first-use download is a side effect; agents should inform the user and respect approval requirements. Checksums protect against accidental corruption or substitution relative to the published manifest but are **not** a signature for release provenance.

## Existing installations

The legacy `tokensaver-docs-marketplace` is not automatically removed, migrated or overwritten. Avoid enabling both legacy and new Codex/Claude versions simultaneously. Keep existing data and caches. This change is not a rename of the old marketplace entry; it introduces a separate shared catalog.

## Verification status

This branch provides source packaging and static checks only. **Real Codex, Claude Code and OpenCode installs on macOS/Windows must be tested before a production-ready or one-click claim.** Do not merge until platform tests are satisfactory.
