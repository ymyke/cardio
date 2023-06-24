# How to contribute to Cardio

Thanks for contributing to Cardio! 🙏


## Contributing as a non-developer, i.e., as a player

- Please play the game.
- Provide feedback:
  - Report bugs in [Issues](https://github.com/ymyke/cardio/issues).
  - Add new ideas or discuss and vote on existing ideas in
    [Discussions](https://github.com/ymyke/cardio/discussions).


## Contributing as a developer, designer, level designer, etc.

Start by reading [DOMAIN](DOMAIN.md) and the file you're currently reading. That should
give you a first overview of the project. Then, pick from the following options:

- Resolve [Issues](https://github.com/ymyke/cardio/issues).
- Pick ideas from [Discussions](https://github.com/ymyke/cardio/discussions), turn them
into [Issues](https://github.com/ymyke/cardio/issues) and implement them. 
- Contribute in [Discussions](https://github.com/ymyke/cardio/discussions). Especially
anything around improving software architecture. 
- Look for the "good first issue" label in both issues and discussions to get started.


## Specific areas to work on

- New [locations](https://github.com/ymyke/cardio/discussions/categories/locations) and
  [skills](https://github.com/ymyke/cardio/discussions/categories/skills).
- Introduce [items](https://github.com/ymyke/cardio/discussions/categories/items)?
- [Improve computer strategy](https://github.com/ymyke/cardio/discussions/106), make it
more elaborate. 
- Improve the current UI (aka TUI, terminal user interface).
- Add new user interfaces, e.g., a web-based interface.


## Contribution workflow

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Add docstrings and comments as necessary and reasonable.
4. Adapt/extend [DOMAIN.md](DOMAIN.md) if necessary.
5. If you added a new skill, make sure to work through the checklist at the top of
   `skills.py`.
6. Ensure the test suite passes. (Run `pytest`.)
7. Use `black` to format your code.
8. Issue a pull request.


## Todo labels in the code

Use the following labels in the code to mark todos:

- `TODO`: High priority todos
- `FIXME`: Todos in general.
- `QQ`: Questions, low-prio todos, etc.

(Consider using vscode's ["todo
tree"](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
extension to get an overview of all todos in the code.)


## License

- Cardio is licensed under the GPLv3 license. See [LICENSE](LICENSE) for details.
- By contributing, you agree that your contributions will be licensed under 
  [the same license](LICENSE).
