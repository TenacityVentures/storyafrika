#!/usr/bin/env python3
"""
Script to create GitHub issues from the StoryAfrika SRS requirements.

This script reads requirements from the SRS document and creates corresponding
GitHub issues with proper labels, milestones, and descriptions.

Usage:
    python create-github-issues.py --token YOUR_GITHUB_TOKEN --repo TenacityVentures/storyafrika

Requirements:
    - PyGithub: pip install PyGithub
    - GitHub personal access token with repo permissions
"""

import argparse
import sys
from typing import List, Dict, Optional

try:
    from github import Github, GithubException
except ImportError:
    print("Error: PyGithub is not installed. Please run: pip install PyGithub")
    sys.exit(1)


# Define all requirements with their metadata
REQUIREMENTS = [
    # Common Platform Requirements
    {
        "id": "REQ-PLAT-001",
        "title": "Platform Identity - Logo and Branding",
        "category": "Platform",
        "priority": "high",
        "labels": ["platform", "frontend", "ui", "high-priority"],
        "assignees": [],
        "milestone": "Common Platform",
        "user_story": "As a user, I want to see the StoryAfrika name and logo clearly, so that I know I am on the correct platform.",
        "acceptance_criteria": [
            "The StoryAfrika logo and name are clearly visible in the site header on all pages",
            "The design follows dark-mode-first aesthetic",
            "The logo is clickable and returns to homepage",
            "Logo displays correctly on both mobile and desktop"
        ],
        "technical_notes": [
            "Logo should be SVG format for scalability",
            "Consider using next/image for optimization"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-PLAT-002",
        "title": "Theme Switching - Dark/Light/System Mode",
        "category": "Platform",
        "priority": "medium",
        "labels": ["platform", "frontend", "ui", "medium-priority"],
        "assignees": [],
        "milestone": "Common Platform",
        "user_story": "As a user, I want to switch between dark, light, and system theme modes, so that I can read comfortably in different lighting conditions.",
        "acceptance_criteria": [
            "Theme toggle is visible in the header on all pages",
            "Three options available: Dark, Light, and System",
            "Selecting an option updates the interface immediately",
            "Theme preference is saved to localStorage",
            "Default is dark mode for first-time visitors",
            "System theme option respects OS preferences"
        ],
        "technical_notes": [
            "Use CSS custom properties for theme colors",
            "Consider using next-themes package",
            "Ensure smooth transition between themes"
        ],
        "dependencies": ["REQ-PLAT-001"]
    },
    {
        "id": "REQ-PLAT-003",
        "title": "Global Search - Story Keyword Search",
        "category": "Platform",
        "priority": "high",
        "labels": ["platform", "frontend", "backend", "search", "high-priority"],
        "assignees": [],
        "milestone": "Common Platform",
        "user_story": "As a user, I want an active global search bar, so that I can quickly find stories by keyword.",
        "acceptance_criteria": [
            "Search bar is visible in the header on all pages",
            "Search is triggered after typing (with 300ms debounce)",
            "Minimum 3 characters required to trigger search",
            "Results display as a dropdown with story title, excerpt, and author",
            "Clicking a result navigates to that story",
            "Search queries across story titles and content",
            "Search includes loading state indicator"
        ],
        "technical_notes": [
            "Use full-text search in backend",
            "Consider implementing search indexing",
            "Add keyboard navigation for results (arrow keys, enter)"
        ],
        "dependencies": ["REQ-PLAT-001"]
    },
    {
        "id": "REQ-PLAT-004",
        "title": "Responsive Navigation - Mobile and Desktop",
        "category": "Platform",
        "priority": "high",
        "labels": ["platform", "frontend", "ui", "responsive", "high-priority"],
        "assignees": [],
        "milestone": "Common Platform",
        "user_story": "As a user, I want responsive navigation that works on mobile and desktop, so that I can browse the platform on any device.",
        "acceptance_criteria": [
            "Mobile (< 768px): Hamburger menu icon is visible",
            "Mobile: Clicking hamburger reveals navigation links",
            "Mobile: Menu can be closed by clicking outside or close button",
            "Desktop (≥ 768px): Navigation links are visible inline",
            "Desktop: Dropdowns work on hover",
            "Navigation includes links to: Home, Categories, Countries, Contribute",
            "Current page is highlighted in navigation"
        ],
        "technical_notes": [
            "Implement with CSS media queries",
            "Consider using headlessui for accessible dropdowns",
            "Ensure keyboard navigation support"
        ],
        "dependencies": ["REQ-PLAT-001"]
    },
    
    # Story Discovery Requirements
    {
        "id": "REQ-DISC-001",
        "title": "Browse by Category - Story Organization",
        "category": "Discovery",
        "priority": "high",
        "labels": ["discovery", "frontend", "backend", "high-priority"],
        "assignees": [],
        "milestone": "Story Discovery",
        "user_story": "As a reader, I want to explore stories by category, so that I can find narratives that match my interests.",
        "acceptance_criteria": [
            "Categories are visible on the homepage",
            "Clicking a category navigates to /categories/{category-slug}",
            "Category page displays all published stories in that category",
            "Stories are sorted by publication date (newest first)",
            "Each story card shows: title, excerpt, author, country, reading time",
            "Pagination shows 20 stories per page",
            "Page includes category name and description"
        ],
        "technical_notes": [
            "Categories (Fixed): Stories of Life, Culture & Traditions, History & Memory, Journeys & Lessons, Creative Voices",
            "Categories should be stored in database",
            "Implement pagination with page numbers",
            "Consider SEO meta tags for category pages"
        ],
        "dependencies": ["REQ-PLAT-004"]
    },
    {
        "id": "REQ-DISC-002",
        "title": "Browse by Country - Geographic Story Discovery",
        "category": "Discovery",
        "priority": "high",
        "labels": ["discovery", "frontend", "backend", "high-priority"],
        "assignees": [],
        "milestone": "Story Discovery",
        "user_story": "As a reader, I want to explore stories by African country, so that I can discover narratives from specific regions.",
        "acceptance_criteria": [
            "\"Explore by Country\" section is visible on homepage",
            "Clicking it navigates to /countries",
            "Countries page shows a grid/list of all African countries",
            "Each country shows: name, flag (optional), story count",
            "Clicking a country navigates to /countries/{country-slug}",
            "Country page displays: country name, description, all published stories",
            "Country page includes filters by category",
            "Stories show title, excerpt, author, reading time",
            "Optional: Related countries section"
        ],
        "technical_notes": [
            "Create comprehensive list of African countries",
            "Store country flags as optimized images or use flag API",
            "Implement efficient querying for story counts"
        ],
        "dependencies": ["REQ-PLAT-004"]
    },
    {
        "id": "REQ-DISC-003",
        "title": "Curated Homepage - Featured Stories Display",
        "category": "Discovery",
        "priority": "critical",
        "labels": ["discovery", "frontend", "critical", "homepage"],
        "assignees": [],
        "milestone": "Story Discovery",
        "user_story": "As a reader, I want a curated homepage with featured stories, so that I can discover quality content without algorithmic noise.",
        "acceptance_criteria": [
            "Hero section with mission statement",
            "1 primary featured story (large card)",
            "3-5 secondary featured stories (medium cards)",
            "\"Browse by Country\" section",
            "\"Browse by Category\" section",
            "NO like counts visible",
            "NO view counts visible",
            "NO \"Trending\" sections",
            "NO infinite scroll (use pagination)",
            "NO algorithmic recommendations"
        ],
        "technical_notes": [
            "Featured stories should be manually curated by editors",
            "Implement lazy loading for images",
            "Consider using ISR (Incremental Static Regeneration) for homepage"
        ],
        "dependencies": ["REQ-PLAT-001", "REQ-EDIT-003"]
    },
    {
        "id": "REQ-DISC-004",
        "title": "Related Stories - Story Recommendations",
        "category": "Discovery",
        "priority": "medium",
        "labels": ["discovery", "backend", "medium-priority", "recommendations"],
        "assignees": [],
        "milestone": "Story Discovery",
        "user_story": "As a reader, I want to see related story recommendations, so that I can explore similar narratives.",
        "acceptance_criteria": [
            "\"Related Stories\" section appears at the end of each story",
            "Shows 3-5 related stories",
            "Recommendations based on: Same country (40%), Same category (30%), Shared tags (30%)",
            "Each story shows: title, excerpt, author, reading time",
            "Stories are clickable and navigate to the story page",
            "Section has clear heading: \"Related Stories\""
        ],
        "technical_notes": [
            "Implement recommendation algorithm in backend",
            "Cache recommendations for performance",
            "Exclude current story from recommendations"
        ],
        "dependencies": ["REQ-DISC-001"]
    },
    {
        "id": "REQ-DISC-005",
        "title": "Reading Without Registration - Open Access",
        "category": "Discovery",
        "priority": "critical",
        "labels": ["discovery", "frontend", "backend", "critical", "authentication"],
        "assignees": [],
        "milestone": "Story Discovery",
        "user_story": "As a reader, I want to read all content without forced registration, so that I can explore freely and anonymously.",
        "acceptance_criteria": [
            "Unauthenticated users can access any story page",
            "Full story content is visible without login",
            "NO \"Sign up to continue reading\" modals",
            "NO blurred content",
            "NO article limits",
            "Attempting to bookmark shows optional login/signup prompt",
            "Login/signup prompt is dismissible",
            "Reading experience is identical for authenticated and unauthenticated users"
        ],
        "technical_notes": [
            "Implement bookmark feature only for authenticated users",
            "Use JWT for authentication when users do sign up",
            "Track anonymous reading metrics without user identification"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-DISC-006",
        "title": "Story Search - Full-Text Search with Ranking",
        "category": "Discovery",
        "priority": "high",
        "labels": ["discovery", "frontend", "backend", "search", "high-priority"],
        "assignees": [],
        "milestone": "Story Discovery",
        "user_story": "As a reader, I want to search for stories by keyword, so that I can find specific narratives quickly.",
        "acceptance_criteria": [
            "Entering search query and pressing Enter navigates to /search?q={keyword}",
            "Results show matching stories ranked by relevance",
            "Relevance ranking: Title matches (highest), Content matches (medium), Author name (low), Tags (low)",
            "Each result shows: title, excerpt with highlighted keywords, author, country",
            "\"No results\" message if query returns zero stories",
            "Search is case-insensitive",
            "Special characters are handled properly",
            "Pagination for search results (20 per page)"
        ],
        "technical_notes": [
            "Use PostgreSQL full-text search or Elasticsearch",
            "Implement keyword highlighting in excerpts",
            "Add search analytics to improve results over time"
        ],
        "dependencies": ["REQ-PLAT-003"]
    },
    
    # Story Creation Requirements
    {
        "id": "REQ-CREATE-001",
        "title": "Story Submission Flow - Writer Application",
        "category": "Creation",
        "priority": "high",
        "labels": ["creation", "frontend", "backend", "high-priority"],
        "assignees": [],
        "milestone": "Story Creation",
        "user_story": "As a writer, I want to apply to contribute stories, so that I can share my narratives on the platform.",
        "acceptance_criteria": [
            "\"Contribute a Story\" link is visible in navigation",
            "Clicking it shows contributor guidelines and application form",
            "Form requires: Full name, Email, Writing sample/portfolio link, Brief explanation",
            "All fields are validated before submission",
            "Submitting form shows confirmation: \"Application received. We'll review and contact you.\"",
            "Editorial team receives email notification with application details",
            "Applicant receives confirmation email"
        ],
        "technical_notes": [
            "Store applications in database with status (pending, approved, rejected)",
            "Implement email notifications using Django email backend",
            "Consider using a form validation library"
        ],
        "dependencies": ["REQ-PLAT-004"]
    },
    {
        "id": "REQ-CREATE-002",
        "title": "Rich Text Editor - Long-Form Writing Interface",
        "category": "Creation",
        "priority": "critical",
        "labels": ["creation", "frontend", "editor", "critical"],
        "assignees": [],
        "milestone": "Story Creation",
        "user_story": "As an approved writer, I want to use a rich-text editor optimized for long-form writing, so that I can focus on crafting my story.",
        "acceptance_criteria": [
            "\"New Story\" button visible in writer's dashboard",
            "Editor supports: Headers (H2, H3), Paragraphs, Bold, Italic, Underline",
            "Editor supports: Lists (ordered, unordered), Links, Block quotes, Images (upload)",
            "Output is stored as clean HTML",
            "Editor autosaves every 30 seconds",
            "Word count displays in bottom corner",
            "Reading time estimate updates dynamically (based on 200 words/minute)",
            "Image uploads are validated (format, size)",
            "Unsaved changes warning when navigating away"
        ],
        "technical_notes": [
            "Recommended: TipTap or Lexical editor",
            "Implement image upload to cloud storage (S3 or similar)",
            "Autosave to drafts table in database",
            "Calculate reading time: wordCount / 200 rounded up"
        ],
        "dependencies": ["REQ-CREATE-001"]
    },
    {
        "id": "REQ-CREATE-003",
        "title": "Story Metadata - Title, Category, Tags, Cover",
        "category": "Creation",
        "priority": "high",
        "labels": ["creation", "frontend", "backend", "high-priority"],
        "assignees": [],
        "milestone": "Story Creation",
        "user_story": "As a writer, I want to assign metadata to my story, so that it is properly archived and discoverable.",
        "acceptance_criteria": [
            "\"Story Details\" section visible after draft content",
            "Title field (required, max 200 characters, character count shown)",
            "Category dropdown (required, shows 5 categories)",
            "Country dropdown (required, searchable, lists African countries)",
            "Tags field (optional, multi-select, max 5 tags, autocomplete)",
            "Cover image upload/URL (optional, validates format and size)",
            "Excerpt field (optional, max 300 characters, auto-generated from first 150 if empty)",
            "Validation prevents submission without required fields",
            "Error messages display clearly for invalid inputs"
        ],
        "technical_notes": [
            "Implement tag autocomplete based on existing tags",
            "Auto-generate excerpt from story content if not provided",
            "Store cover images in cloud storage",
            "Validate image dimensions and file size (max 2MB)"
        ],
        "dependencies": ["REQ-CREATE-002"]
    },
    {
        "id": "REQ-CREATE-004",
        "title": "Draft Management - Save and Edit Drafts",
        "category": "Creation",
        "priority": "high",
        "labels": ["creation", "frontend", "backend", "high-priority"],
        "assignees": [],
        "milestone": "Story Creation",
        "user_story": "As a writer, I want to save my work as a draft, so that I can return and finish it later.",
        "acceptance_criteria": [
            "\"Save Draft\" button visible in editor",
            "Clicking saves all content and metadata",
            "Story status is set to \"draft\"",
            "Confirmation message: \"Draft saved\" appears",
            "User can navigate away without losing work",
            "Dashboard shows all drafts with: Title, Last edited date, Word count",
            "Each draft has \"Edit\" and \"Delete\" actions",
            "Deleting draft shows confirmation dialog",
            "Drafts are sorted by last edited date (newest first)"
        ],
        "technical_notes": [
            "Store drafts with status='draft' in database",
            "Implement soft delete for drafts (keep in DB but mark as deleted)",
            "Show last edited timestamp, not creation time"
        ],
        "dependencies": ["REQ-CREATE-002"]
    },
    {
        "id": "REQ-CREATE-005",
        "title": "Story Submission for Review - Editorial Queue",
        "category": "Creation",
        "priority": "critical",
        "labels": ["creation", "backend", "workflow", "critical"],
        "assignees": [],
        "milestone": "Story Creation",
        "user_story": "As a writer, I want to submit my story for editorial review, so that it can be published on the platform.",
        "acceptance_criteria": [
            "\"Submit for Review\" button visible when story is complete",
            "Clicking validates all required fields (title, category, country)",
            "Story status changes from \"draft\" to \"submitted\"",
            "Confirmation message: \"Story submitted for review\"",
            "Editorial team receives email notification",
            "Writer receives email confirmation",
            "Story appears in editor's review queue",
            "Writer cannot edit story while it's \"submitted\" or \"in_review\"",
            "If editor requests changes, status returns to \"draft\" and editing is enabled"
        ],
        "technical_notes": [
            "Implement status workflow: draft → submitted → in_review → published/changes_requested",
            "Send notifications via email queue",
            "Lock editing when status is submitted or in_review"
        ],
        "dependencies": ["REQ-CREATE-003", "REQ-CREATE-004"]
    },
    
    # User Profile Requirements
    {
        "id": "REQ-PROFILE-001",
        "title": "Writer Profile Page - Author Portfolio",
        "category": "Profile",
        "priority": "medium",
        "labels": ["profile", "frontend", "backend", "medium-priority"],
        "assignees": [],
        "milestone": "User Profiles",
        "user_story": "As a writer, I want a dedicated profile page, so that readers can discover my other stories and learn about me.",
        "acceptance_criteria": [
            "Writer's name is clickable throughout the platform",
            "Clicking navigates to /writers/{writer-slug}",
            "Page displays: Full name, Profile photo (if uploaded), Bio (if provided), Country (if selected)",
            "List of published stories (newest first)",
            "Total story count displayed",
            "Each story shows: title, excerpt, category, reading time",
            "Stories are paginated (20 per page)",
            "Page includes social share buttons (optional)"
        ],
        "technical_notes": [
            "Generate writer slugs from names (handle duplicates)",
            "Implement profile photo upload (max 1MB, formats: jpg, png)",
            "Bio should support basic markdown formatting"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-PROFILE-002",
        "title": "Reader Account & Bookmarks - Save Stories",
        "category": "Profile",
        "priority": "medium",
        "labels": ["profile", "frontend", "backend", "authentication", "medium-priority"],
        "assignees": [],
        "milestone": "User Profiles",
        "user_story": "As a reader, I want to create an account and save stories, so that I can return to them later.",
        "acceptance_criteria": [
            "\"Bookmark\" icon visible on story pages",
            "Clicking bookmark when unauthenticated shows login/signup modal",
            "Creating account and logging in automatically bookmarks the story",
            "Bookmarks accessible from /dashboard/bookmarks",
            "Bookmarks page shows: Story title, excerpt, author, Date bookmarked",
            "Each bookmark has \"Remove\" action",
            "Bookmarks are sorted by date bookmarked (newest first)",
            "Removing bookmark shows confirmation",
            "Empty state message when no bookmarks exist"
        ],
        "technical_notes": [
            "Store bookmarks in many-to-many relationship between users and stories",
            "Implement optimistic UI updates for bookmark toggle",
            "Use JWT authentication for API requests"
        ],
        "dependencies": ["REQ-DISC-005"]
    },
    {
        "id": "REQ-PROFILE-003",
        "title": "User Settings - Account and Preferences Management",
        "category": "Profile",
        "priority": "medium",
        "labels": ["profile", "frontend", "backend", "settings", "medium-priority"],
        "assignees": [],
        "milestone": "User Profiles",
        "user_story": "As a user, I want to manage my account settings, so that I can update my profile and preferences.",
        "acceptance_criteria": [
            "Settings accessible from /dashboard/settings",
            "Profile section: Full name, Bio, Profile photo upload, Country dropdown",
            "Account section: Email (with verification), Password change",
            "Preferences section: Email notifications toggle (on/off)",
            "\"Save Changes\" button validates and updates data",
            "Confirmation message: \"Settings updated\"",
            "Email change requires verification via email",
            "Password change requires current password confirmation",
            "All fields are validated before saving"
        ],
        "technical_notes": [
            "Implement email verification flow for email changes",
            "Hash passwords using Django's built-in password hashers",
            "Validate email format and uniqueness",
            "Store preferences in user profile model"
        ],
        "dependencies": ["REQ-PROFILE-002"]
    },
    
    # Editorial Workflow Requirements
    {
        "id": "REQ-EDIT-001",
        "title": "Editorial Review Dashboard - Story Queue Management",
        "category": "Editorial",
        "priority": "critical",
        "labels": ["editorial", "frontend", "backend", "critical", "admin"],
        "assignees": [],
        "milestone": "Editorial Workflow",
        "user_story": "As an editor, I want a dashboard showing all submitted stories, so that I can review and manage them efficiently.",
        "acceptance_criteria": [
            "Dashboard accessible at /editorial (requires editor or admin role)",
            "Table shows stories with status \"submitted\" or \"in_review\"",
            "Each row shows: Story title (clickable), Author name, Category, Submission date, Word count",
            "Actions: Review, Publish, Request Changes",
            "Stories are sorted by submission date (oldest first)",
            "Pagination shows 20 stories per page",
            "Filter options: By status, By category, By submission date range",
            "Search by title or author name"
        ],
        "technical_notes": [
            "Implement role-based access control (RBAC)",
            "Only users with editor or admin role can access",
            "Optimize query to avoid N+1 problems"
        ],
        "dependencies": ["REQ-CREATE-005"]
    },
    {
        "id": "REQ-EDIT-002",
        "title": "Story Review Actions - Publish, Request Changes, Reject",
        "category": "Editorial",
        "priority": "critical",
        "labels": ["editorial", "backend", "workflow", "critical"],
        "assignees": [],
        "milestone": "Editorial Workflow",
        "user_story": "As an editor, I want to review stories and provide feedback, so that we maintain high editorial standards.",
        "acceptance_criteria": [
            "Clicking \"Review\" shows full story preview with metadata",
            "Preview shows: Full content, Category, Country, Tags, Author info",
            "Action buttons: Publish, Request Changes, Reject",
            "Clicking \"Publish\": Story status → \"published\", Story appears on platform, Writer receives email",
            "Clicking \"Request Changes\": Text field for feedback notes, Status → \"draft\", Writer can edit and resubmit, Writer receives email with notes",
            "Clicking \"Reject\": Text field for rejection reason, Status → \"archived\", Writer receives email with reason",
            "All actions show confirmation dialog",
            "Actions are logged with editor name and timestamp"
        ],
        "technical_notes": [
            "Implement audit trail for all editorial actions",
            "Store feedback notes in database",
            "Queue email notifications for async processing",
            "Only editors can perform these actions"
        ],
        "dependencies": ["REQ-EDIT-001"]
    },
    {
        "id": "REQ-EDIT-003",
        "title": "Featured Story Curation - Homepage Story Selection",
        "category": "Editorial",
        "priority": "high",
        "labels": ["editorial", "frontend", "backend", "curation", "high-priority"],
        "assignees": [],
        "milestone": "Editorial Workflow",
        "user_story": "As an editor, I want to select stories to feature on the homepage, so that we showcase the best content.",
        "acceptance_criteria": [
            "\"Featured Stories\" section in editorial dashboard",
            "Current featured stories displayed with drag-to-reorder functionality",
            "Search to add new featured stories (only published stories)",
            "\"Remove from featured\" action for each story",
            "Adding a story makes it immediately visible on homepage",
            "Maximum 6 featured stories allowed",
            "Order is preserved: First = primary hero, Next 5 = secondary cards",
            "Changes take effect immediately (no cache delay)"
        ],
        "technical_notes": [
            "Store featured stories with sort order in database",
            "Implement drag-and-drop using a library like dnd-kit",
            "Clear homepage cache when featured stories change",
            "Featured stories should have is_featured flag and featured_order field"
        ],
        "dependencies": ["REQ-EDIT-001"]
    },
    
    # Non-Functional Requirements
    {
        "id": "REQ-NFR-001",
        "title": "Performance Optimization - Load Time and Core Web Vitals",
        "category": "Non-Functional",
        "priority": "critical",
        "labels": ["non-functional", "performance", "critical"],
        "assignees": [],
        "milestone": "Non-Functional",
        "user_story": "As a user on a slow connection, I want the platform to load quickly, so that I can access content even with limited bandwidth.",
        "acceptance_criteria": [
            "First Contentful Paint (FCP) < 1.5s on 3G",
            "Largest Contentful Paint (LCP) < 2.5s on 3G",
            "Time to Interactive (TTI) < 3.5s on 3G",
            "Page Weight < 500KB initial load (gzipped)",
            "All pages meet performance targets on simulated 3G connection",
            "Images are lazy-loaded below the fold",
            "Fonts are optimized (WOFF2 format)",
            "Critical CSS is inlined",
            "JavaScript is code-split by route",
            "Lighthouse performance score > 90",
            "Core Web Vitals pass for all key pages"
        ],
        "technical_notes": [
            "Use Next.js Image component for automatic optimization",
            "Implement font subsetting for used characters only",
            "Use next/dynamic for code splitting",
            "Consider using a CDN for static assets"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-NFR-002",
        "title": "Mobile Optimization - Responsive Design and Touch Interfaces",
        "category": "Non-Functional",
        "priority": "critical",
        "labels": ["non-functional", "mobile", "responsive", "critical"],
        "assignees": [],
        "milestone": "Non-Functional",
        "user_story": "As a mobile user, I want the platform optimized for my device, so that I can read comfortably on small screens.",
        "acceptance_criteria": [
            "All pages are responsive on mobile devices (< 768px)",
            "Touch targets are minimum 44x44px",
            "Text is readable without zooming (min 16px)",
            "No horizontal scrolling occurs",
            "Platform is installable as a PWA",
            "Tap interactions have visual feedback",
            "Forms are optimized for mobile input (correct keyboard types)",
            "Reading experience is optimized (font size, line height, margins)"
        ],
        "technical_notes": [
            "Test on real devices: iPhone, Android phones",
            "Use viewport meta tag correctly",
            "Implement touch-friendly interactions",
            "Consider thumb zones for primary actions"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-NFR-003",
        "title": "Progressive Web App (PWA) - Offline Support and Installability",
        "category": "Non-Functional",
        "priority": "high",
        "labels": ["non-functional", "pwa", "offline", "high-priority"],
        "assignees": [],
        "milestone": "Non-Functional",
        "user_story": "As a user, I want to install the platform as an app, so that I can read stories offline.",
        "acceptance_criteria": [
            "PWA install prompt appears on mobile devices",
            "Platform installs as a PWA",
            "Saved/bookmarked stories are available offline",
            "App icon appears on homescreen",
            "App opens in standalone mode (no browser chrome)",
            "Service worker caches critical assets (HTML, CSS, JS, fonts)",
            "Offline page displays when user is offline and page isn't cached",
            "App updates automatically when new version is deployed"
        ],
        "technical_notes": [
            "Create manifest.json with app metadata",
            "Implement service worker with workbox",
            "Cache strategy: Network-first for API, Cache-first for static assets",
            "Test offline functionality thoroughly",
            "Consider implementing background sync for drafts"
        ],
        "dependencies": ["REQ-NFR-002"]
    },
    {
        "id": "REQ-NFR-004",
        "title": "Accessibility (WCAG 2.1 AA) - Inclusive Design",
        "category": "Non-Functional",
        "priority": "high",
        "labels": ["non-functional", "accessibility", "a11y", "high-priority"],
        "assignees": [],
        "milestone": "Non-Functional",
        "user_story": "As a user with disabilities, I want the platform to be accessible, so that I can use it with assistive technologies.",
        "acceptance_criteria": [
            "All interactive elements are keyboard accessible",
            "Focus indicators are visible and clear",
            "Tab order is logical and intuitive",
            "All images have descriptive alt text",
            "Headings are properly structured (H1 → H6, no skipping levels)",
            "ARIA labels used where appropriate",
            "Color contrast meets WCAG AA standards (4.5:1 for normal text)",
            "Forms have proper labels and error messages",
            "Respects prefers-reduced-motion for animations",
            "Screen reader testing passes with NVDA/JAWS"
        ],
        "technical_notes": [
            "Use semantic HTML elements",
            "Test with axe DevTools and Lighthouse accessibility audit",
            "Implement skip-to-content link",
            "Ensure focus management in modals and dropdowns",
            "Test with keyboard only (no mouse)"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-NFR-005",
        "title": "Security - Authentication, Authorization, and Data Protection",
        "category": "Non-Functional",
        "priority": "critical",
        "labels": ["non-functional", "security", "critical"],
        "assignees": [],
        "milestone": "Non-Functional",
        "user_story": "As a user, I want my data to be secure, so that my personal information is protected.",
        "acceptance_criteria": [
            "HTTPS Only: All connections use TLS 1.3",
            "Authentication: JWT tokens with 1-hour expiry and refresh tokens",
            "Password Requirements: Min 8 chars, 1 uppercase, 1 lowercase, 1 number",
            "CSRF Protection: Tokens on all state-changing requests",
            "XSS Prevention: All user input sanitized",
            "SQL Injection Prevention: ORM parameterized queries only (no raw SQL)",
            "Rate Limiting: 100 requests/min per IP on auth endpoints",
            "Content Security Policy: Strict CSP headers",
            "Secure Headers: X-Frame-Options, X-Content-Type-Options, etc.",
            "Password hashing: Use bcrypt or Argon2"
        ],
        "technical_notes": [
            "Use Django security middleware",
            "Implement django-ratelimit for rate limiting",
            "Store JWTs in httpOnly cookies (not localStorage)",
            "Regularly update dependencies for security patches",
            "Implement security headers with django-csp"
        ],
        "dependencies": []
    },
    {
        "id": "REQ-NFR-006",
        "title": "SEO Optimization - Search Engine Visibility and Discoverability",
        "category": "Non-Functional",
        "priority": "high",
        "labels": ["non-functional", "seo", "high-priority"],
        "assignees": [],
        "milestone": "Non-Functional",
        "user_story": "As a platform, we want high search engine visibility, so that stories are discoverable via Google.",
        "acceptance_criteria": [
            "All story pages include proper meta tags (title, description, keywords)",
            "Open Graph tags for social media sharing",
            "Twitter Card tags",
            "Canonical URLs for all pages",
            "Structured data (JSON-LD) for articles",
            "XML sitemap generated and submitted to Google",
            "Robots.txt properly configured",
            "Page titles are unique and descriptive",
            "Meta descriptions are unique and compelling (max 160 chars)",
            "URLs are clean and descriptive (no IDs when possible)",
            "Images have descriptive filenames and alt text"
        ],
        "technical_notes": [
            "Use Next.js Head component for meta tags",
            "Generate sitemap automatically on build",
            "Implement ISR for frequently updated pages",
            "Use next-seo package for easier SEO management",
            "Submit sitemap to Google Search Console",
            "Monitor SEO performance with Google Analytics"
        ],
        "dependencies": []
    }
]


def format_issue_body(requirement: Dict) -> str:
    """Format the issue body with all requirement details."""
    body_parts = [
        f"## Requirement ID: {requirement['id']}\n",
        f"**Category:** {requirement['category']}  ",
        f"**Priority:** {requirement['priority'].upper()}\n",
        f"### User Story\n{requirement['user_story']}\n",
        "### Acceptance Criteria\n"
    ]
    
    for criterion in requirement['acceptance_criteria']:
        body_parts.append(f"- [ ] {criterion}")
    
    body_parts.append("\n### Technical Notes\n")
    for note in requirement['technical_notes']:
        body_parts.append(f"- {note}")
    
    if requirement.get('dependencies'):
        body_parts.append(f"\n### Dependencies\n")
        for dep in requirement['dependencies']:
            body_parts.append(f"- {dep}")
    
    body_parts.append(f"\n---\n*This issue was auto-generated from the StoryAfrika SRS document*")
    
    return "\n".join(body_parts)


def create_github_issues(token: str, repo_name: str, dry_run: bool = False):
    """Create GitHub issues from requirements."""
    try:
        g = Github(token)
        repo = g.get_repo(repo_name)
        
        print(f"Connected to repository: {repo.full_name}")
        print(f"Creating {len(REQUIREMENTS)} issues...\n")
        
        created_issues = []
        milestones_cache = {}
        
        for i, req in enumerate(REQUIREMENTS, 1):
            print(f"[{i}/{len(REQUIREMENTS)}] Processing {req['id']}: {req['title']}")
            
            if dry_run:
                print(f"  [DRY RUN] Would create issue with labels: {', '.join(req['labels'])}")
                continue
            
            try:
                # Get or create milestone
                milestone = None
                milestone_name = req.get('milestone')
                if milestone_name:
                    if milestone_name not in milestones_cache:
                        # Try to find existing milestone
                        for ms in repo.get_milestones(state='open'):
                            if ms.title == milestone_name:
                                milestones_cache[milestone_name] = ms
                                break
                        else:
                            # Create new milestone if not found
                            try:
                                milestones_cache[milestone_name] = repo.create_milestone(
                                    title=milestone_name,
                                    description=f"Issues related to {milestone_name}"
                                )
                                print(f"  Created new milestone: {milestone_name}")
                            except GithubException as e:
                                print(f"  Warning: Could not create milestone {milestone_name}: {e}")
                    
                    milestone = milestones_cache.get(milestone_name)
                
                # Create issue
                issue = repo.create_issue(
                    title=f"[{req['id']}] {req['title']}",
                    body=format_issue_body(req),
                    labels=req['labels'],
                    milestone=milestone
                )
                
                created_issues.append(issue)
                print(f"  ✓ Created issue #{issue.number}: {issue.html_url}")
                
            except GithubException as e:
                print(f"  ✗ Error creating issue: {e}")
                continue
        
        print(f"\n{'[DRY RUN] ' if dry_run else ''}Summary:")
        print(f"  Total requirements: {len(REQUIREMENTS)}")
        print(f"  Issues created: {len(created_issues)}")
        
        if created_issues:
            print(f"\nCreated issues:")
            for issue in created_issues:
                print(f"  - #{issue.number}: {issue.title}")
        
        return created_issues
        
    except GithubException as e:
        print(f"Error connecting to GitHub: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Create GitHub issues from StoryAfrika SRS requirements"
    )
    parser.add_argument(
        "--token",
        required=True,
        help="GitHub personal access token with repo permissions"
    )
    parser.add_argument(
        "--repo",
        default="TenacityVentures/storyafrika",
        help="GitHub repository in format owner/repo (default: TenacityVentures/storyafrika)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate issue creation without actually creating them"
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("StoryAfrika GitHub Issue Creator")
    print("=" * 80)
    print(f"Repository: {args.repo}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 80)
    print()
    
    if not args.dry_run:
        confirm = input("This will create 27 issues in the repository. Continue? (yes/no): ")
        if confirm.lower() != "yes":
            print("Cancelled.")
            sys.exit(0)
    
    create_github_issues(args.token, args.repo, args.dry_run)


if __name__ == "__main__":
    main()
