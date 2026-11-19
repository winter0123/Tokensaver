# Add another Tokensaver plugin

1. Develop each plugin in its own GitHub repository, owning its code, tests, binaries and releases. Do not copy engines into the `Tokensaver` marketplace.
2. Provide a tested platform-appropriate plugin package. For Codex use `.codex-plugin/plugin.json`; for Claude Code use `.claude-plugin/plugin.json`. Where convenient, put both manifests and shared skill files in a single subdirectory.
3. For a package hosted under a subdirectory, register `git-subdir` with its Git URL, the precise plugin directory, and a reviewed source ref or SHA. Add the matching ID to both marketplace catalogs.
4. OpenCode uses its own plugin manager. Supply a separate npm/Git package as needed, and document its install command; don't invent an OpenCode `marketplace.json` format.
5. Verify package completeness and any native runtime bootstrap, review its downloaded artifacts, update README and run `scripts/validate_marketplaces.py`.
6. Test in actual Codex/Claude/OpenCode clients, including fresh installs, updates and coexistence with legacy versions. GitHub marketplace metadata alone cannot prove host/runtime behavior.

Do not trigger npm lifecycle scripts or untrusted downloads implicitly. For TokenSaver Docs, the CLI launchers pin the release version and validate SHA-256, and the existing conversion engine is kept in its independent repository.
