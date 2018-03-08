# Introduction
This document outlines the organisation of the project Kanban board

# Structure
1. backlog
  - Initial board for new items

2. active
  - Items that are available for development
  - All items that have been chosen for a sprint
  - Sprint finished once all have been moved to `closed`

3. wip
  - Items that have been claimed by (or assigned to) a team member
  - Should ideally have multiple assignees who collaborate on it
  - Details of item should include feature branch name if one is being used

4. testing
  - Items that are in testing (ideally by assignees)
  - If unassigned, any team member may perform testing

5. ready
  - Items that are complete but not fully merged

6. closed
  - Changes are fully complete, tested, and in master branch
