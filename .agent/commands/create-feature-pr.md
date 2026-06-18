Create a feature branch, commit changes, push, and open a Pull Request following the project's Gitflow conventions.

## Steps

### 1. Confirm starting point
```bash
git branch --show-current   # should be main
git status                  # check for uncommitted changes
```

### 2. Ask the user for
- **Feature name** — short slug for the branch (e.g. `add-config-system`)
- **Brief description** — used in commit message and PR body

### 3. Create feature branch (if not already on one)
```bash
git checkout -b feature/<feature-name>
```

### 4. Run tests before committing
```bash
pytest -v
```
Do not proceed if tests fail.

### 5. Stage and commit
Review `git diff` first, then stage specific files (avoid `git add .` which may include temp/build artifacts).

Use Conventional Commits format:
```
<type>: <short description>

<bullet list of changes>

Co-Authored-By: Antigravity IDE <noreply@google.com>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

### 6. Push
```bash
git push -u origin feature/<feature-name>
```

### 7. Create PR
```bash
gh pr create \
  --title "<concise title under 70 chars>" \
  --body "$(cat <<'EOF'
## Summary
- <bullet 1>
- <bullet 2>

## Test plan
- [ ] Tests pass (`pytest -v`)
- [ ] Tested manually with sample book build

🤖 Generated with Antigravity IDE
EOF
)" \
  --base main
```

### 8. Return summary
Show branch name, commit hash, and PR URL as a plain table (no bold around the URL — it breaks clickable links).

## Notes
- Never commit directly to `main`
- Always run tests before creating the PR
- `temp/` and `build/` are gitignored — don't force-add them
- Link related GitHub issues in the PR body if applicable
