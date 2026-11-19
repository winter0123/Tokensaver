# Tokensaver

**Lightweight marketplace for independent AI token-optimization plugins.**

| Plugin | Repository | Supported host |
| --- | --- | --- |
| **TokenSaver Docs** | [winter0123/tokensaver-docs](https://github.com/winter0123/tokensaver-docs) | Codex, Claude Code, OpenCode |

## Codex

```sh
codex plugin marketplace add winter0123/Tokensaver
```

Then select **TokenSaver Docs** from the Codex plugin manager. The marketplace loads the independent [SKILL + CLI package](https://github.com/winter0123/tokensaver-docs/tree/main/marketplace-plugin). You do **not** configure an MCP server. The first actual document operation may download the checked native runtime (v0.5.6) from the plugin's GitHub Releases.

## Claude Code

```sh
claude plugin marketplace add winter0123/Tokensaver
claude plugin install tokensaver-docs@tokensaver
```

The same SKILL + CLI package is installed. No manual MCP configuration.

## OpenCode

OpenCode uses its own plugin management system, **not** the Codex/Claude marketplace catalogs:

```sh
opencode plugin add 'github:winter0123/tokensaver-docs#main::path:plugins/opencode'
```

This points at the independent OpenCode plugin package in the same repository. The plugin resolves a bundled CLI or prepares a checksummed cached runtime on first startup/use. It manages its own internal tools; the user does not register an MCP server.

## Runtime and status

First use can require an HTTPS download from GitHub Releases, with SHA-256 verification. Native binaries are currently released for **macOS arm64/x64 and Windows x64**. Linux is source-install only. Existing standalone release ZIP installers remain supported and are not removed or migrated automatically. Image/audio AI provider choices and consent remain separate from installing the plugin.

These are review-branch integrations; the [Tokensaver PR](https://github.com/winter0123/Tokensaver/pull/1) and [TokenSaver Docs PR](https://github.com/winter0123/tokensaver-docs/pull/2) must both be merged before the commands target the new packages on `main`. Real host installations have not yet been verified.

See [installation and migration](docs/installation.md) and [how to add another plugin](docs/development.md).
