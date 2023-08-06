import argparse
from customattack.commands.attack_command import AttackCommand
from customattack.commands.train_model_command import TrainModelCommand


def main():
    parser = argparse.ArgumentParser(
        "customattack CLI",
        usage="[python -m] customattack <commands> [<args>]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(help="customattack commands helpers")
    AttackCommand.register_subcommand(subparsers)
    TrainModelCommand.register_subcommand(subparsers)
    # Let's go
    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        exit(1)
    # Run
    func = args.func
    del args.func
    func.run(args)


if __name__ == "__main__":
    main()
