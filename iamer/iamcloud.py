import json
import urllib
from ConfigParser import SafeConfigParser
import os
import os.path
from boto.iam.connection import IAMConnection

from iamuser import IamUser
from iamgroup import IamGroup
from iampolicy import IamPolicy
from constants import (USERS_FILE,
                       GROUPS_FILE,
                       POLICIES_DIR)


class IamCloud(object):
    """Representation of the IAM database in AWS"""
    def __init__(self):
        self._users = set()
        self._groups = set()
        self._policies = set()
        self._conn = IAMConnection()

    def _load_users(self):
        raw_users = self._conn.get_all_users()
        is_truncated = (raw_users[u'list_users_response']
                                 [u'list_users_result']
                                 [u'is_truncated'])
        u_list = (raw_users[u'list_users_response']
                           [u'list_users_result']
                           [u'users'])
        while is_truncated == u'true':
            marker = (raw_users[u'list_users_response']
                               [u'list_users_result']
                               [u'marker'])
            raw_users = self._conn.get_all_users(marker=marker)
            is_truncated = (raw_users[u'list_users_response']
                                     [u'list_users_result']
                                     [u'is_truncated'])
            u_list += (raw_users[u'list_users_response']
                                [u'list_users_result']
                                [u'users'])

        for u_dict in u_list:
            name = u_dict[u'user_name']

            # User's groups
            groups = set()
            raw_groups = self._conn.get_groups_for_user(name)
            g_list = (raw_groups[u'list_groups_for_user_response']
                                [u'list_groups_for_user_result']
                                [u'groups'])
            for g_dict in g_list:
                groups.add(g_dict[u'group_name'])

            # User's policies
            policies = set()
            raw_policies = self._conn.get_all_user_policies(name)
            p_list = (raw_policies[u'list_user_policies_response']
                                  [u'list_user_policies_result']
                                  [u'policy_names'])
            for policy_name in p_list:
                raw_policy = self._conn.get_user_policy(name, policy_name)
                encoded_policy = (raw_policy[u'get_user_policy_response']
                                            [u'get_user_policy_result']
                                            [u'policy_document'])
                str_policy = urllib.unquote_plus(encoded_policy)
                dict_policy = json.loads(str_policy)
                policy = IamPolicy(policy_name, dict_policy)
                policies.add(policy)

            user = IamUser(name, groups, policies)
            self._users.add(user)

    @property
    def users(self):
        if not self._users:
            self._load_users()

        return self._users

    def _load_groups(self):
        raw_groups = self._conn.get_all_groups()
        is_truncated = (raw_groups[u'list_groups_response']
                                  [u'list_groups_result']
                                  [u'is_truncated'])
        g_list = (raw_groups[u'list_groups_response']
                            [u'list_groups_result']
                            [u'groups'])

        while is_truncated == u'true':
            marker = (raw_groups[u'list_groups_response']
                                [u'list_groups_result']
                                [u'marker'])
            raw_groups = self._conn.get_all_groups(marker=marker)
            is_truncated = (raw_groups[u'list_groups_response']
                                      [u'list_groups_result']
                                      [u'is_truncated'])
            g_list += (raw_groups[u'list_groups_response']
                                 [u'list_groups_result']
                                 [u'groups'])

        for g_dict in g_list:
            name = g_dict[u'group_name']

            # Group's policies
            policies = set()
            raw_policies = self._conn.get_all_group_policies(name)
            p_list = (raw_policies[u'list_group_policies_response']
                                  [u'list_group_policies_result']
                                  [u'policy_names'])
            for policy_name in p_list:
                raw_policy = self._conn.get_group_policy(name, policy_name)
                encoded_policy = (raw_policy[u'get_group_policy_response']
                                            [u'get_group_policy_result']
                                            [u'policy_document'])
                str_policy = urllib.unquote_plus(encoded_policy)
                dict_policy = json.loads(str_policy)
                policy = IamPolicy(policy_name, dict_policy)
                policies.add(policy)

            group = IamGroup(name, policies)
            self._groups.add(group)

    @property
    def groups(self):
        if not self._groups:
            self._load_groups()

        return self._groups

    @property
    def policies(self):
        if not self._policies:
            self._load_policies()

        return self._policies

    def dump_users(self):
        """Dump users into files"""
        config = SafeConfigParser()

        for user in sorted(self.users):
            config.add_section(user.name)
            if user.groups:
                config.set(user.name,
                           u'groups',
                           ',\n'.join(sorted(user.groups)))
            if user.policies:
                policy_names = set()
                for policy in user.policies:
                    policy_names.add(policy.name)
                config.set(user.name,
                           u'policies',
                           ',\n'.join(sorted(policy_names)))

        with open(USERS_FILE, 'w') as configfile:
            config.write(configfile)

    def dump_groups(self):
        """Dump groups into files"""
        config = SafeConfigParser()

        for group in sorted(self.groups):
            config.add_section(group.name)
            if group.policies:
                policy_names = set()
                for policy in group.policies:
                    policy_names.add(policy.name)
                config.set(group.name,
                           u'policies',
                           ',\n'.join(sorted(policy_names)))

        with open(GROUPS_FILE, 'w') as configfile:
            config.write(configfile)

    def dump_policies(self):
        """Dump user and group policies into files"""
        policies_to_dump = set()

        # Check that there is no dupe policy
        policy_used = {}
        for user in self.users:
            for policy in user.policies:
                if policy.name not in policy_used:
                    policy_used[policy.name] = set(["user:" + user.name])
                else:
                    policy_used[policy.name].add("user:" + user.name)
        for group in self.groups:
            for policy in group.policies:
                if policy.name not in policy_used:
                    policy_used[policy.name] = set(["group:" + group.name])
                else:
                    policy_used[policy.name].add("group:" + group.name)

        for policy_name in policy_used:
            if len(policy_used[policy_name]) > 1:
                print("Multiple policies named {} have been found:"
                      .format(policy_name))
                for policy_user in policy_used[policy_name]:
                    print " - {}".format(policy_user)
                print
                print ("You must rename any duplicate policy for the dump to "
                       "be consistent.")
                print "Rename those and dump again."

        for user in self.users:
            for policy in user.policies:
                policies_to_dump.add(policy)

        for group in self.groups:
            for policy in group.policies:
                policies_to_dump.add(policy)

        # If the policies folder is not there, create it
        if policies_to_dump and not os.path.isdir(POLICIES_DIR):
            os.mkdir(POLICIES_DIR, 0755)

        for policy in policies_to_dump:
            filename = policy.name + u'.json'
            filepath = os.path.join(POLICIES_DIR, filename)
            with open(filepath, 'w') as policy_file:
                json.dump(policy.document,
                          policy_file,
                          sort_keys=True,
                          indent=2,
                          separators=(',', ': '))

    def dump(self):
        """Dump everything into files"""
        print "Dumping users into {filename}...".format(filename=USERS_FILE)
        self.dump_users()

        print "Dumping groups into {filename}...".format(filename=GROUPS_FILE)
        self.dump_groups()

        print ("Dumping policies into {foldername}/*.json..."
               .format(foldername=POLICIES_DIR))
        self.dump_policies()
