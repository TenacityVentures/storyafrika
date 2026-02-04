# GitHub Issues Generation for StoryAfrika SRS

This directory contains tools to convert the Software Requirements Specification (SRS) document into GitHub issues for project management.

## Files

- **srs-requirements.md**: Complete SRS document with all functional and non-functional requirements
- **create-github-issues.py**: Python script to automatically create GitHub issues from requirements
- **requirements.txt**: Python dependencies for the script
- **USAGE.md**: Detailed instructions (this file)

## Quick Start

### Prerequisites

1. Python 3.7 or higher
2. GitHub personal access token with `repo` permissions
3. Access to the TenacityVentures/storyafrika repository

### Installation

```bash
# Navigate to the docs directory
cd docs

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### 1. Dry Run (Recommended First)

Test the script without creating actual issues:

```bash
python create-github-issues.py --token YOUR_GITHUB_TOKEN --dry-run
```

#### 2. Create Issues

Create all 27 issues in the repository:

```bash
python create-github-issues.py --token YOUR_GITHUB_TOKEN
```

#### 3. Custom Repository

If you want to test on a different repository:

```bash
python create-github-issues.py --token YOUR_GITHUB_TOKEN --repo your-org/your-repo
```

## Getting a GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "StoryAfrika Issue Creator")
4. Select the `repo` scope (full control of private repositories)
5. Click "Generate token"
6. Copy the token immediately (you won't be able to see it again)

**Security Note**: Never commit your GitHub token to the repository!

## What Gets Created

The script will create:

- **27 GitHub Issues**: One for each requirement in the SRS
- **7 Milestones**: To organize issues by category
  - Common Platform (4 issues)
  - Story Discovery (6 issues)
  - Story Creation (5 issues)
  - User Profiles (3 issues)
  - Editorial Workflow (3 issues)
  - Non-Functional (6 issues)

Each issue includes:
- Requirement ID (e.g., REQ-PLAT-001)
- User story
- Acceptance criteria (as checkboxes)
- Technical notes
- Dependencies (if any)
- Appropriate labels (category, priority)
- Milestone assignment

## Issue Labels

The script uses the following labels:

**By Category:**
- `platform` - Common platform features
- `discovery` - Story discovery features
- `creation` - Story creation features
- `profile` - User profile features
- `editorial` - Editorial workflow features
- `non-functional` - Non-functional requirements

**By Priority:**
- `critical` - Must-have features
- `high-priority` - Important features
- `medium-priority` - Nice-to-have features

**By Component:**
- `frontend` - Frontend implementation
- `backend` - Backend implementation
- `ui` - UI/UX work
- `database` - Database changes
- `authentication` - Auth-related

**By Type:**
- `enhancement` - New feature
- `documentation` - Documentation work

## Milestones Structure

1. **Common Platform** - Foundation features (logo, navigation, search, themes)
2. **Story Discovery** - Browse, search, and discover stories
3. **Story Creation** - Writer tools and editorial submission
4. **User Profiles** - Reader and writer profiles
5. **Editorial Workflow** - Editorial review and curation
6. **Non-Functional** - Performance, security, accessibility, SEO, PWA

## Manual Adjustments After Creation

After running the script, you may want to:

1. **Assign Team Members**: Add appropriate assignees to each issue based on the team roles document
2. **Set Due Dates**: Add deadlines to milestones
3. **Create Project Board**: Organize issues into a GitHub Project board with columns (Backlog, To Do, In Progress, Review, Done)
4. **Add Epic Labels**: Consider adding epic labels to group related issues
5. **Prioritize Within Milestones**: Order issues within each milestone by priority
6. **Link Issues**: Add cross-references between dependent issues

## Troubleshooting

### "Rate limit exceeded"
GitHub has API rate limits. If you hit this, wait an hour or use a different token.

### "Resource not accessible by integration"
Your token doesn't have the necessary permissions. Regenerate with `repo` scope.

### "Validation Failed"
Usually means a label or milestone name is too long or contains invalid characters.

### Issues created but milestones are missing
The script will create milestones if they don't exist, but you may need to create them manually first if there are permission issues.

## Modifying Requirements

To add, remove, or modify requirements:

1. Edit the `REQUIREMENTS` list in `create-github-issues.py`
2. Follow the existing structure for each requirement dictionary
3. Run with `--dry-run` to test
4. Run without `--dry-run` to create issues

## Best Practices

1. **Always run with --dry-run first** to verify what will be created
2. **Use a test repository first** if you're making significant changes
3. **Don't run the script multiple times** on the same repository to avoid duplicates
4. **Keep the SRS document updated** as requirements evolve
5. **Close issues via commits** by referencing issue numbers in commit messages

## Example Workflow

```bash
# 1. Test first
python create-github-issues.py --token $GITHUB_TOKEN --dry-run

# 2. Review the output

# 3. Create issues for real
python create-github-issues.py --token $GITHUB_TOKEN

# 4. Visit GitHub to verify
# https://github.com/TenacityVentures/storyafrika/issues

# 5. Create a project board and add issues to it
```

## Environment Variable

For security, consider using an environment variable for your token:

```bash
# Set the token (add to your .bashrc or .zshrc)
export GITHUB_TOKEN="your_token_here"

# Use it
python create-github-issues.py --token $GITHUB_TOKEN
```

## Alternative: Manual Issue Creation

If you prefer not to use the script, you can create issues manually using the SRS document as a reference. Each requirement section in `srs-requirements.md` contains all the information needed to create a comprehensive GitHub issue.

## Support

For questions or issues with the script:
1. Check the troubleshooting section above
2. Review the SRS requirements document
3. Contact the development team

---

**Note**: This script is designed for one-time bulk creation of issues. For ongoing requirement management, consider using GitHub's issue templates and project boards.
