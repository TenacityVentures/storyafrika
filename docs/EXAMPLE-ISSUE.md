# Example GitHub Issue

This is an example of what a GitHub issue will look like when created by the script.

---

**Title:** `[REQ-PLAT-001] Platform Identity - Logo and Branding`

**Labels:** `platform`, `frontend`, `ui`, `high-priority`

**Milestone:** Common Platform

**Body:**

```markdown
## Requirement ID: REQ-PLAT-001

**Category:** Platform  
**Priority:** HIGH

### User Story
As a user, I want to see the StoryAfrika name and logo clearly, so that I know I am on the correct platform.

### Acceptance Criteria
- [ ] The StoryAfrika logo and name are clearly visible in the site header on all pages
- [ ] The design follows dark-mode-first aesthetic
- [ ] The logo is clickable and returns to homepage
- [ ] Logo displays correctly on both mobile and desktop

### Technical Notes
- Logo should be SVG format for scalability
- Consider using next/image for optimization

---
*This issue was auto-generated from the StoryAfrika SRS document*
```

---

## How to Track Progress

As you work on the requirement:

1. **Check off acceptance criteria** as they are completed
2. **Add comments** with implementation details or questions
3. **Reference commits** that address the requirement
4. **Link related PRs** using GitHub's PR linking feature
5. **Update labels** if the scope changes (e.g., add `needs-review`)
6. **Move between project columns** to show progress

## Example Workflow

### When Starting Work
1. Assign yourself to the issue
2. Move to "In Progress" column
3. Create a feature branch: `feature/req-plat-001-platform-identity`
4. Add a comment: "Started work on this, implementing logo component"

### While Working
1. Make commits referencing the issue: `git commit -m "Add StoryAfrika logo component (REQ-PLAT-001)"`
2. Check off acceptance criteria as completed
3. Add screenshots or code snippets in comments

### When Complete
1. Create PR referencing issue: "Closes #1" in PR description
2. Request review
3. After approval and merge, issue automatically closes
4. Move to "Done" column

## Issue Dependencies

When an issue has dependencies (like REQ-PLAT-002 depends on REQ-PLAT-001):

1. Add a task list in the issue
2. Link to dependent issues: "Depends on #1"
3. Use GitHub's "blocked by" label if needed
4. Don't start dependent issues until prerequisites are complete

## Custom Fields (if using GitHub Projects)

You may want to add:
- **Estimate**: Story points or time estimate
- **Sprint**: Which sprint this belongs to
- **Team**: Frontend/Backend/Both
- **Status**: Not Started/In Progress/Review/Done
- **Complexity**: Low/Medium/High

---

See the full requirements in [docs/srs-requirements.md](./srs-requirements.md)
