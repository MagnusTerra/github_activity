import sys
import argparse
from github_activity.core import GitHubApi


def main():
    parser = argparse.ArgumentParser(description="GitHub Activity CLI")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")

    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    ##Show
    show_parser = subparsers.add_parser("show", help="Show GitHub activity")
    show_parser.add_argument("username", type=str, help="GitHub username")
    
    
    args = parser.parse_args()

    if args.command == "show":
        api = GitHubApi()
        events = api.get_user_events(args.username)

        for event in events:
            print(f"- {event}")

if __name__ == "__main__":
    main()
