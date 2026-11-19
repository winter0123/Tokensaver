# Install Tokensaver

Tokensaver is a **catalog**, not a single binary or all-in-one package. Installing one plugin must not automatically install other plugins.

## Codex

```sh
codex plugin marketplace add winter0123/Tokensaver
```

Then install `tokensaver-docs@tokensaver` in the plugin manager. Check available commands in your installed Codex version. This is a Git-backed plugin, and its root `mcp.json` starts `tokensaver-docs mcp`, so the runtime must already be on the agent process `PATH`.

## Claude Code

```sh
claude plugin marketplace add winter0123/Tokensaver
claude plugin install tokensaver-docs@tokensaver
```

The plugin needs the `tokensaver-docs` native executable on the process `PATH` before its MCP server can run.

## Install native runtime first

See [TokenSaver Docs release instructions](https://github.com/winter0123/tokensaver-docs/blob/main/docs/distribution.md) for platform-specific ZIP archives and installers. **Note:** the current release installer places binaries in private versioned directories and does not automatically expose `tokensaver-docs` on `PATH`. A successful marketplace registration or plugin install alone does not imply that the native MCP tools work. Verify `tokensaver-docs --help` and a real MCP tool call in your actual host environment. The supported alternative is the self-contained native plugin bundle, which installs its own local marketplace.

## Existing users

If you installed `tokensaver-docs@tokensaver-docs-marketplace`, do not delete it just to try this catalog. The old local bundle and this new Git-backed catalog are distinct installations. Disable one copy before enabling the other to avoid duplicate server registrations. No automatic migration, release-binary distribution, or removal of legacy cache is performed by this repository.

## OpenCode

OpenCode uses its independent [TokenSaver Docs installer](https://github.com/winter0123/tokensaver-docs/blob/main/docs/distribution.md). This catalog does not change OpenCode registration.
