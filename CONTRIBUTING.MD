# Contribution guidelines

First of all, thanks for thinking of contributing to this project. :smile:
We are grateful that you considered contributing to **rose**. We welcome any contribution that could enhance app's functionality. Please follow the below guidelines for contribution. Visit [gitter.im](https://gitter.im/rose_) for discussion on issues.

## Pull Request Checklist
Kindly follow the simple steps below to submit a Pull Request.<br>
- If a relevant issue already exists, discuss on the issue a and get it assigned to yourself on GitHub.
- If no relevant issue exists, open a new issue and get it assigned to yourself on GitHub.
- Before sending a Pull Request, please make sure that you're assigned the task on a GitHub issue.
- Make sure your changes are consistent with the guidelines and follow the coding style of the project. Use `pylint` to check your Python changes. 
- Test the relevant parts of the code throughly.
- Ensure any new dependencies are added to requirements.txt

# Development

Refer [git-workflow](https://github.com/asmeurer/git-workflow) for more doubts. <br>

Do this once
1. Fork this repo.
2. Clone this repo with `git clone https://github.com/kaustubhhiware/rose.git`
3. Go to the directory with `cd rose`
4. Add your own fork as a remote to the repo `git remote add <your username>  https://github.com/<your username>/rose.git`
5. Install dependencies with `pip install -r requirements.txt`

Do this each time you need to add a feature <br>
1. Do `git checkout master`to switch to main branch and `git pull origin master` to sync with this repo.
2. Make a seperate branch with a descriptive name (that could explain the purpose of the PR) such as `awesome_feature` and switch to it by running `git checkout -b your_branch(here, awesome_feature)` in the terminal.
3. Add/Modify the code and do `git add files_involved` to add your changes.
4. Commit your changes using `git commit`. Add a descriptive summary in the editor.  Make sure that the project is in a workable state after each commit. 
5. Do `git push <your name>` to push code into your fork.
6. Finally, create a PR by clicking on the *New Pull Request* button  [here](https://github.com/kaustubhhiware/rose/pulls).
