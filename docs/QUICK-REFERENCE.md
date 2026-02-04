# StoryAfrika Requirements - Quick Reference

## Summary

**Total Requirements:** 27  
**Version:** 1.0  
**Status:** Build-Ready

## Requirements Breakdown

### 1. Common Platform (4 requirements)
- **REQ-PLAT-001**: Platform Identity - Logo and branding
- **REQ-PLAT-002**: Theme Switching - Dark/Light/System modes
- **REQ-PLAT-003**: Global Search - Story keyword search
- **REQ-PLAT-004**: Responsive Navigation - Mobile and desktop

### 2. Story Discovery (6 requirements)
- **REQ-DISC-001**: Browse by Category - 5 fixed categories
- **REQ-DISC-002**: Browse by Country - African countries
- **REQ-DISC-003**: Curated Homepage - Featured stories, no algorithms
- **REQ-DISC-004**: Related Stories - Recommendation engine
- **REQ-DISC-005**: Reading Without Registration - Open access
- **REQ-DISC-006**: Story Search - Full-text search with ranking

### 3. Story Creation (5 requirements)
- **REQ-CREATE-001**: Story Submission Flow - Writer application
- **REQ-CREATE-002**: Rich Text Editor - TipTap/Lexical with autosave
- **REQ-CREATE-003**: Story Metadata - Title, category, tags, cover
- **REQ-CREATE-004**: Draft Management - Save and edit drafts
- **REQ-CREATE-005**: Story Submission for Review - Editorial queue

### 4. User Profiles (3 requirements)
- **REQ-PROFILE-001**: Writer Profile Page - Author portfolio
- **REQ-PROFILE-002**: Reader Account & Bookmarks - Save stories
- **REQ-PROFILE-003**: User Settings - Account and preferences

### 5. Editorial Workflow (3 requirements)
- **REQ-EDIT-001**: Editorial Review Dashboard - Story queue
- **REQ-EDIT-002**: Story Review Actions - Publish/Request Changes/Reject
- **REQ-EDIT-003**: Featured Story Curation - Homepage selection

### 6. Non-Functional (6 requirements)
- **REQ-NFR-001**: Performance - Core Web Vitals (FCP < 1.5s, LCP < 2.5s)
- **REQ-NFR-002**: Mobile Optimization - Responsive, touch-friendly
- **REQ-NFR-003**: Progressive Web App - Offline support, installable
- **REQ-NFR-004**: Accessibility - WCAG 2.1 AA compliance
- **REQ-NFR-005**: Security - HTTPS, JWT, password requirements
- **REQ-NFR-006**: SEO Optimization - Meta tags, sitemap, structured data

## Priority Levels

- **Critical** (7): REQ-DISC-003, REQ-DISC-005, REQ-CREATE-002, REQ-CREATE-005, REQ-EDIT-001, REQ-EDIT-002, REQ-NFR-001, REQ-NFR-002, REQ-NFR-005
- **High** (11): REQ-PLAT-001, REQ-PLAT-003, REQ-PLAT-004, REQ-DISC-001, REQ-DISC-002, REQ-DISC-006, REQ-CREATE-001, REQ-CREATE-003, REQ-CREATE-004, REQ-EDIT-003, REQ-NFR-003, REQ-NFR-004, REQ-NFR-006
- **Medium** (6): REQ-PLAT-002, REQ-DISC-004, REQ-PROFILE-001, REQ-PROFILE-002, REQ-PROFILE-003

## Fixed Categories

1. Stories of Life
2. Culture & Traditions
3. History & Memory
4. Journeys & Lessons
5. Creative Voices

## Technology Stack (Recommended)

- **Frontend**: Next.js 13+, React, TypeScript
- **Backend**: Django 4+, Django REST Framework
- **Database**: PostgreSQL 14+
- **Cache**: Redis
- **Storage**: AWS S3 or similar
- **Deployment**: Vercel (frontend), Railway/Heroku (backend)

## Key Principles

1. **Editorial over Algorithmic**: Manual curation, no recommendation algorithms
2. **Open Access**: All content readable without registration
3. **Preservation First**: Long-form content, cultural archive
4. **Mobile-First**: Optimized for 3G, low-bandwidth
5. **No Social Features**: No likes, comments, or social graph
6. **High Standards**: Editorial review required before publishing

## Out of Scope (MVP)

- Breaking news or real-time updates
- Social features (likes, followers, comments)
- Algorithmic feeds
- Creator monetization
- AI-generated content
- Video hosting

## Development Phases (Suggested)

### Phase 1: Foundation (Weeks 1-2)
- REQ-PLAT-001, REQ-PLAT-004
- REQ-DISC-005
- REQ-NFR-005 (Security basics)

### Phase 2: Reading Experience (Weeks 3-4)
- REQ-DISC-001, REQ-DISC-002, REQ-DISC-003
- REQ-PLAT-002, REQ-PLAT-003
- REQ-NFR-001, REQ-NFR-002

### Phase 3: Writing & Editorial (Weeks 5-6)
- REQ-CREATE-001, REQ-CREATE-002, REQ-CREATE-003, REQ-CREATE-004, REQ-CREATE-005
- REQ-EDIT-001, REQ-EDIT-002, REQ-EDIT-003

### Phase 4: User Features (Week 7)
- REQ-PROFILE-001, REQ-PROFILE-002, REQ-PROFILE-003
- REQ-DISC-004, REQ-DISC-006

### Phase 5: Polish & Optimization (Week 8)
- REQ-NFR-003, REQ-NFR-004, REQ-NFR-006
- Bug fixes and refinements
- Testing and QA

## Team Assignments (Reference)

- **Frontend Team**: George, George, Faith, Elizabeth, Augustine, Ahmed, Mohammed
- **Backend**: Zekeri
- **UI/UX**: Ahmed Faizal
- **PM**: Laura, Taiwo
- **DevOps**: Alex, Frank
- **Management**: David, Samuel

## Next Steps

1. Review complete SRS document: `docs/srs-requirements.md`
2. Create GitHub issues: Run `docs/create-github-issues.py`
3. Set up project board with milestones
4. Begin Phase 1 development

---

For detailed information on each requirement, see [srs-requirements.md](./srs-requirements.md)  
For instructions on creating GitHub issues, see [USAGE.md](./USAGE.md)
