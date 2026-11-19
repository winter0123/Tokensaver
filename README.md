# Tokensaver

**One lightweight marketplace. Independent plugin repositories.**

| Plugin | Repository | Purpose |
| --- | --- | --- |
| **TokenSaver Docs** (`tokensaver-docs`) | [winter0123/tokensaver-docs](https://github.com/winter0123/tokensaver-docs) | Convert documents and reuse context across AI agents. |

## Marketplace registration

Codex:

```sh
codex plugin marketplace add winter0123/Tokensaver
```

Claude Code:

```sh
claude plugin marketplace add winter0123/Tokensaver
claude plugin install tokensaver-docs@tokensaver
```

**Runtime requirement:** A Git-sourced TokenSaver Docs plugin needs the `tokensaver-docs` native command on `PATH` to start its MCP server. Marketplace registration does **not** download platform-specific release binaries. The existing native installer uses private versioned paths, so it does **not** automatically satisfy this prerequisite. See [installation and migration notes](docs/installation.md) before changing any existing installation.

## Structure

- `.agents/plugins/marketplace.json`: Codex catalog; ID `tokensaver`, display name `Tokensaver`.
- `.claude-plugin/marketplace.json`: Claude Code catalog; ID `tokensaver`.
- Each plugin remains in its own repository and owns its builds, GitHub Releases, and updates.

Read [installation](docs/installation.md) and [adding another plugin](docs/development.md). These source catalogs are separate from any official public plugin directory.
