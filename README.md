The workflows are looking good, but not totally done.
- The macos env runs the test suite and fails as expected.
- The macos env is the only one that correctly sets up and runs everything.
- The windows env fails [due to mixed line endings][windows-error].
  - I wonder if this is being caused by the checkout.
  - There is a git config setting that will correct this.  Go look that up.
- The linux 3.9 environment is working as expected - like the macos environments.
  - The [3.10 and 3.11 linux environments][linux-error] are not working.  They are failing to
    complete the set up steps.


# Resources
- [Workflow examples](https://github.com/actions/starter-workflows)
- [Running tox in GH Actions](https://github.com/ymyzk/tox-gh-actions)
- [fail-fast](https://www.edwardthomson.com/blog/github_actions_6_fail_fast_matrix_workflows.html)
- [GH Action variables][gh-action-vars]

[linux-error]: https://github.com/GuyHoozdis/guyhoozdis/actions/runs/5894264270/job/15987536147
[windows-error]: https://github.com/GuyHoozdis/guyhoozdis/actions/runs/5894264270/job/15987536908
[gh-action-vars]: https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables
