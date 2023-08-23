# 2023-08-22

The [linux and macos workflows](https://github.com/GuyHoozdis/guyhoozdis/actions/runs/5945646219)
are working as expected.  -The windows workflows are still failing on mixed line endings.-

I added a .gitattributes file that was probably a little overkill.  I think forcing the python
extensions to `lf` is what did it, but it might have been the catch-all rule added at the very end.
I'll have to come back and experiment some more to figure out what is minimally needed.

All the workflows are now working as expected.  Everything sets up and runs correctly.  The tests
fail, but they are expected to do that.  Implementing the tests and writing some actual source code
for the package is the next step.


# 2023-08-16

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
- [Advanced usage of the setup-python action][caching-packages]

[linux-error]: https://github.com/GuyHoozdis/guyhoozdis/actions/runs/5894264270/job/15987536147
[windows-error]: https://github.com/GuyHoozdis/guyhoozdis/actions/runs/5894264270/job/15987536908
[gh-action-vars]: https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables
[caching-packages]: https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#caching-packages
