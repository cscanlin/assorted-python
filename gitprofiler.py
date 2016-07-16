from gitpandas.utilities.plotting import plot_cumulative_blame
from gitpandas import GitHubProfile
g = GitHubProfile(username='cscanlin', ignore_forks=True, verbose=True)
blame = g.cumulative_blame(branch='master', extensions=['py'], by='project', ignore_dir=['docs'], limit=None, skip=None)
plot_cumulative_blame(blame)
