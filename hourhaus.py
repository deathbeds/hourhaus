if __name__ == "__main__":
    from doit.cmd_base import ModuleTaskLoader
    from doit.doit_cmd import DoitMain
    import sys
    
    sys.exit(DoitMain(ModuleTaskLoader(my_module_with_tasks)).run(sys.argv[1:]))
