---
description: Commit changes, push to branch, and create a pull request with description
---

This workflow automates the complete process of committing changes, pushing to a branch, and creating a pull request. It handles the entire flow in one execution.

## Automated Execution Steps

This workflow performs the following steps automatically:

1. **Review current state**
   - Check `git status` for staged and unstaged changes
   - Review `git diff` for unstaged changes
   - Review `git diff --staged` for staged changes
   - Check current branch with `git branch --show-current`

2. **Stage all changes**
   - Stage all modified files with `git add .`
   - Confirm staged changes with `git diff --staged`

3. **Create commit with standards**
   - Use commit message format: `<type>: <short description>` (under 72 chars)
   - Types: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
   - Describe WHAT changed and WHY, not HOW
   - NO implementation details (function names, query syntax, line counts)
   - NO technical specifics
   - Include attribution via commit-msg hook

4. **Handle branch management**
   - If on main/master: create new branch `git checkout -b feature/descriptive-name`
   - If on feature branch: continue with current branch
   - Branch naming: `feature/`, `fix/`, `docs/`, `refactor/`, etc.

5. **Push to remote**
   - Push branch with `git push -u origin <branch-name>`
   - Handle any merge conflicts if they arise

6. **Create pull request**
   - Use `gh pr create` with descriptive title and body
   - Title matches commit message (without attribution)
   - Body includes summary, context, testing, and related issues
   - NO attribution text in PR description (commit-msg hook handles this for commits)

## Commit Message Format

Follow commit standards:

```
<type>: <short description>

- High-level change 1
- High-level change 2
```

**Rules:**
- First line: type, colon, short description (under 72 chars)
- Types: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- Describe WHAT changed and WHY, not HOW
- NO implementation details
- NO technical specifics
- Attribution added automatically by commit-msg hook

## PR Description Template

```markdown
## Summary
- Change 1
- Change 2

## Context
Explanation of why these changes are necessary.

## Testing
Description of testing performed.

## Related Issues
Fixes #123
```

## Example Commands

```bash
# Complete workflow execution
git status
git diff
git add .
git commit -m "feat: add user authentication flow"
git checkout -b feature/user-auth
git push -u origin feature/user-auth
gh pr create --title "feat: add user authentication flow" --body "$(cat <<'EOF'
## Summary
- Added user authentication module
- Implemented login/logout functionality
- Added session management

## Context
Users need secure authentication to access protected features.

## Testing
- Tested login with valid credentials
- Tested logout functionality
- Verified session persistence

## Related Issues
Fixes #123
EOF
)"
```

## Notes

- Reference related issues in commit message and PR description
- Keep PRs focused on single feature or fix
- Do not include attribution text in PR description (commit-msg hook handles this for commits)
- This workflow is designed to be executed end-to-end without manual intervention
