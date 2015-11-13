#!/usr/bin/env python

from __future__ import print_function
from pprint import pprint
from time import sleep
import argparse
import digitalocean


ACTIONS = [
    'start',
    'stop',
    'status',
    'ip'
]

def get_args():
    parser = argparse.ArgumentParser(description='sgw usage')
    parser.add_argument('--token', '-t', required=True)
    parser.add_argument('--wait', '-w', action='store_true', default=False)
    parser.add_argument('--verbose', '-v', action='store_true', default=False)
    parser.add_argument('action', choices=ACTIONS)
    parser.add_argument('droplet')
    return parser.parse_args()


def __get_droplet(token, name):
    manager = digitalocean.Manager(token=token)
    droplets = manager.get_all_droplets()
    if name is None:
        return droplets[0] if len(droplets) > 0 else None
    for d in droplets:
        if d.name == name:
            return d


def start(token, droplet_name, wait, verbose=False):
    if verbose:
        print('Requested power on of {}'.format(droplet_name))
    d = __get_droplet(token, droplet_name)
    assert d, 'Could not find droplet named {}'.format(droplet_name)
    if d.status == 'active':
        return
    d.power_on()
    if not wait:
        return d
    while __get_droplet(token, droplet_name).status != 'active':
        print('.', end='')
        sleep(1)
    print('Done!')



def stop(token, droplet_name, wait, verbose=False):
    if verbose:
        print('Requested shutdown of {}'.format(droplet_name))
    d = __get_droplet(token, droplet_name)
    assert d, 'Could not find droplet named {}'.format(droplet_name)
    if d.status == 'off':
        return
    d.shutdown()
    if not wait:
        return d
    while __get_droplet(token, droplet_name).status != 'off':
        print('.', end='')
        sleep(1)
    print('Done!')


def status(token, droplet_name, verbose=False):
    if verbose:
        print('Requested status of {}'.format(droplet_name))
    d = __get_droplet(token, droplet_name)
    assert d, 'Could not find droplet named {}'.format(droplet_name)
    pprint(vars(__get_droplet(token, droplet_name)))
    # pprint(args)


def get_ip(token, droplet_name, verbose=False):
    if verbose:
        print('Requested IP of {}'.format(droplet_name))
    d = __get_droplet(token, droplet_name)
    assert d, 'Could not find droplet named {}'.format(droplet_name)
    print(d.ip_address)


def main():
    args = get_args()
    if args.action == 'start':
        start(args.token, args.droplet, args.wait, args.verbose)
    elif args.action == 'stop':
        stop(args.token, args.droplet, args.wait, args.verbose)
    elif args.action == 'status':
        status(args.token, args.droplet, args.verbose)
    elif args.action == 'ip':
        get_ip(args.token, args.droplet, args.verbose)


if __name__ == '__main__':
    main()
