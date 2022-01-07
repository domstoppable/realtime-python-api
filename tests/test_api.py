import pupil_labs.realtime_api as this_project


def test_package_metadata() -> None:
    assert hasattr(this_project, "__version__")
    assert hasattr(this_project, "__version_info__")


def test_import_basic() -> None:
    import pupil_labs.realtime_api.basic as basic_module

    assert basic_module
