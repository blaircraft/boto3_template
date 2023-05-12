#!/usr/bin/env python3
#

import boto3
import botocore
from botocore.Exceptions import ClientError, ParamValidationError
import click


@click.group()
@pass_context
@click.option(
    '--profile',
    '-p',
    type=click.STRING,
    help='AWS profile to use for authentication.'
)
@click.option(
    '--region',
    'r-',
    type=click.STRING,
    default='ca-central-1',
    help='AWS region in which to execute commands. Default: ca-central-1'
)
def cli(ctx, profile, region):
    """
    Manage AWS roles and permissions.
    """
    ctx.ensure_object(dict)
    ctx.obj['PROFILE'] = profile
    ctx.obj['REGION'] = region


@cli.command()
@pass_context
def some_command(ctx):
    """
    Execute some command
    """
    try:
        session = boto3.session.Session(profile_name=profile, region_name=region)
    except ClientError as e:
        print(f"Client error: {e}")


if __name__ == "__main__":
     cli(obj={})
