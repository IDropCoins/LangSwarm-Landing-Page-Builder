# Contributing

## Commit messages

This repository follows **[Conventional Commits](https://www.conventionalcommits.org/)**.

Format:

```
<type>(<optional scope>): <short summary>

<optional body: what changed and why>

<optional footer: BREAKING CHANGE:, Refs #123, etc.>
```

**Types** (common):

| Type | Use for |
|------|---------|
| `feat` | New feature or behavior |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code change that is not a fix or feature |
| `test` | Adding or updating tests |
| `chore` | Maintenance, tooling, deps, scaffolding |
| `ci` | CI configuration |
| `build` | Build system or packaging |

**Summary line:** imperative mood (“add”, not “added”), ~72 characters or fewer, no trailing period.

**Examples:**

```
chore(repo): add gitignore for Python venv and env files
feat(swarm): wire copywriter and designer handoff tools
fix(cli): handle missing OPENAI_API_KEY before invoke
docs(readme): document setup and Python version requirement
```

## Using the commit template (optional)

```bash
git config commit.template .gitmessage
```

Then `git commit` opens the template in your editor.
