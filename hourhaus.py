DOIT_CONFIG = dict(verbosity=2)


def task_install_nox():
    return dict(actions=["nox --install-only"])


def task_kernelspec():
    def install():
        from jupyter_client.kernelspec import KernelSpecManager
        import pidgy, pathlib

        KernelSpecManager().install_kernel_spec(
            str(pathlib.Path(pidgy.__file__).parent / "kernelspec"), "pidgy", user=True
        )

    return dict(actions=[install])


if __name__ == "__main__":
    from doit.cmd_base import ModuleTaskLoader
    from doit.doit_cmd import DoitMain
    import sys

    sys.exit(DoitMain(ModuleTaskLoader(globals())).run(sys.argv[1:]))
