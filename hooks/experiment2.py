from tackle import hook


@hook(is_public=True)
def do_experiment_2(name: str = "foo"):
    """Do something"""
    print(name, "things")

