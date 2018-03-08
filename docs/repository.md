# Introduction

This document defines the guidelines for this repository, including:

- the organisation that should be kept
- the git workflow that should be used

# Organisation

- `/`, the root of the project, should contain only:
  - README.md - contains a description of the project, a high-level usage guide, and installation
    instructions
  - LICENSE
  - build files
- `/docs` includes documents related to the project, including specification
- `/src` contains the code of the project

# Git workflow

## Setup
- `$ git clone git@projects.cs.nott.ac.uk:grp17-todo/audri.git`: Download the repository
- `cd` to repository directory
- `$ git config user.name "<your name>"`: Set your username
- `$ git config user.email "<your university email>"`: Set your email
- For your first push, use `$ git push -u origin master` to set your upstream

## Conventions
- `master` is the default development branch
- Use tags on `master` to mark version names. These are agreed upon by group, and should usually
  be after sprints

## Branch for feature
Use a feature branch when working on large changes - this allows you to save your work-in-progress
changes in the repository without it affecting `master` for everyone else

- `git checkout -b feat-<featurename>`: Create and swap to new branch
- Finish all your changes (commits)
- `git rebase -i master`: Bring your branch up to date with `master`, applying your commits on top
- `git checkout master`: Swap to master
- `git merge --no-ff feat-<featurename>`: Merge commits from feature branch into `master`
- `git branch -d feat-<featurename>`: Delete the feature branch
- `git push origin master`: Push changes to repository

## Commits
- Commit changes that have a common goal
- Use descriptive but succinct commit messages (`git commit -m`)
  - If modifying a part of a larger feature, prefix with `<featurename>: `
  - Messages should be in present tense ('fix bug that caused crash')
- Preferably signed with your GPG key (`git commit -s`)
- eg `git commit -sm "sim: fix bug in car move that caused crash"`
