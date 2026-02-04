#!/bin/bash
# Wrapper script for creating GitHub issues from StoryAfrika SRS

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}StoryAfrika GitHub Issue Creator${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Please install Python 3 and try again"
    exit 1
fi

# Check if PyGithub is installed
if ! python3 -c "import github" 2>/dev/null; then
    echo -e "${YELLOW}PyGithub is not installed${NC}"
    echo "Installing dependencies..."
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
    echo -e "${GREEN}✓ Dependencies installed${NC}"
    echo ""
fi

# Check for GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${YELLOW}GitHub token not found in environment${NC}"
    echo "Please enter your GitHub personal access token:"
    read -s GITHUB_TOKEN
    echo ""
fi

# Determine mode
MODE="live"
if [ "$1" == "--dry-run" ] || [ "$1" == "-d" ]; then
    MODE="dry-run"
fi

# Repository
REPO="${GITHUB_REPO:-TenacityVentures/storyafrika}"

echo -e "${BLUE}Configuration:${NC}"
echo "  Repository: $REPO"
echo "  Mode: $MODE"
echo ""

if [ "$MODE" == "live" ]; then
    echo -e "${YELLOW}This will create 27 issues in the repository${NC}"
    echo -n "Continue? (yes/no): "
    read CONFIRM
    if [ "$CONFIRM" != "yes" ]; then
        echo "Cancelled."
        exit 0
    fi
    echo ""
fi

# Run the Python script
echo -e "${GREEN}Running issue creator...${NC}"
echo ""

if [ "$MODE" == "dry-run" ]; then
    python3 "$SCRIPT_DIR/create-github-issues.py" \
        --token "$GITHUB_TOKEN" \
        --repo "$REPO" \
        --dry-run
else
    python3 "$SCRIPT_DIR/create-github-issues.py" \
        --token "$GITHUB_TOKEN" \
        --repo "$REPO"
fi

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ Success!${NC}"
    if [ "$MODE" == "live" ]; then
        echo "View issues at: https://github.com/$REPO/issues"
    fi
else
    echo -e "${RED}✗ Failed with exit code $EXIT_CODE${NC}"
    exit $EXIT_CODE
fi
