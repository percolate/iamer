# IAMer [![Build Status](https://circleci.com/gh/percolate/iamer/tree/master.svg?style=shield&circle-token=8a0b48c518e6d05bcd8116c3e925a2ad2db7d25a)](https://circleci.com/gh/percolate/iamer)

IAMer dump and load your AWS IAM configuration into text files.

Once dumped, you can version the resulting `json` and `ini` files to keep track
of changes, and even ask your team mates to do [Pull Requests](https://help.github.com/articles/using-pull-requests)
when they want access to something.

_To Be Implemented_ Once the text files have been modified, you can load the
changes into IAM with one command.

## Quick Start

```bash
# Dump your current IAM database
$ iamer dump
Dumping users...
Dumping groups...
Dumping policies...

# Save it
$ git commit
$ git push
```

## Install

```bash
pip install iamer
```

## Configuration

IAMer uses [boto](https://github.com/boto/boto) so you will need the
following to run:
```bash
export AWS_ACCESS_KEY_ID="1234567890"
export AWS_SECRET_ACCESS_KEY="bb7075bc63f93d21fb9b8f45c3fa5ad0"
```

See the [boto documention](http://docs.pythonboto.org/en/latest/boto_config_tut.html)
for other ways to configure it.

## Usage

There are 2 modes of operation, `dump` and `load`.

### Dump your IAM configuration locally

```bash
$ iamer dump
Dumping users...
Dumping groups...
Dumping policies...
```

You will get 3 things.

A `users.ini` file with the list of users defined in IAM, and the groups and
policies attached to each.

```ini
# This user has no group or policy
[bob]

# joe is part of the useless-group group
[joe]
groups = useless-group

# superadmin has multiple groups and policies attached to him
[superadmin]
groups = ec2-rw,
         ec2-r53-r
policies = dynamodb-dev-201301121713,
           dynamodb-live-201301121713,
```

A `groups.ini` file with the list of groups defined in IAM, and the policies
attached to each.

```ini
# A group with no policy
[useless-group]

# The ec2-rw group has the ec2-read-write policy attached to it
[ec2-rw]
policies = ec2-read-write

# This group has 2 policies attached
[ec2-r53-r]
policies = ec2-read-only,
           r53-read-only
```

And in the `policies/` folder, you will find all the policies referenced in the
`users.ini` and `groups.ini` files as `json` files.

For example, the `policies/ec2-read-write.json` will contain:
```json
{
  "Statement": [
    {
      "Action": "ec2:*",
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

### Update your IAM config based on your local files

_TO BE IMPLEMENTED_
