import nox

@nox.session(venv_backend="conda", reuse_venv=True)
def sphinx(session):
  session.install("jupyter-book")

@nox.session(venv_backend="conda", reuse_venv=True)
def mkdocs(session):
  session.install("mkdocs")
  
@nox.session(venv_backend="conda", reuse_venv=True)
def nikola(session):
  session.install("nikola", "ruamel.yaml", "notebook")

