from tackle import hook


@hook(is_public=True)
def do_experiment_1(name: str = "foo"):
    print(name)
