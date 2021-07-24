DOIT_CONFIG = dict(verbosity=2)

def task_install_nox():
    return dict(actions=["nox --install-only"])

if __name__ == "__main__":
    from doit.cmd_base import ModuleTaskLoader
    from doit.doit_cmd import DoitMain
    import sys
    
    sys.exit(DoitMain(ModuleTaskLoader(globals())).run(sys.argv[1:]))
