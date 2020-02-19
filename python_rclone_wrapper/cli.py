"""Console script for python_rclone_wrapper."""
from python_rclone_wrapper.locking import ProcessLock
from python_rclone_wrapper.rclone import RClone
import logging
import argparse
import sys

logger = logging.getLogger(__name__)
log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', default=1)
parser.add_argument('-p', '--pid', action='store', dest='pid', default='/var/run/python_rclone_wrapper.pid', help='PID File')
parser.add_argument('-c', '--config', action='store', dest='config', default='rclone.conf', help='rclone config file')
parser.add_argument('--flags', nargs='+', help='rclone command flags', default=[])
parser.add_argument('command', action='store', choices=RClone.commands())
parser.add_argument('arguments', nargs='*', help='Command Arguments', default=[])

def parse_arguments():
    args = parser.parse_args()
    level = log_levels[min(len(log_levels)-1, args.verbose)]  # capped to number of levels
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")
    return args

def main():
    """Console script for python_rclone_wrapper."""
    args = parse_arguments()
    logger.debug("Creating process lock with PID File: %s", args.pid)
    with ProcessLock(args.pid):
        rclone = RClone(args.config)
        command = getattr(rclone, args.command)
        result = command(arguments=args.arguments, flags=args.flags)

        if result['error']:
            logger.error(result['error'])

        if result['out']:
            logger.info(result['out'])
        return result['code']
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
