#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.module_utils.common.collections import ImmutableDict
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.plugins.callback import CallbackBase
from ansible.vars.manager import VariableManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible import context

import os


# Create a callback plugin so we can capture the output
class ResultsCollectorJSONCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in.

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin.
    """

    def __init__(self, *args, **kwargs):
        super(ResultsCollectorJSONCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        host = result._host
        self.host_unreachable[host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        """Print a json representation of the result.

        Also, store the result in an instance attribute for retrieval later
        """
        host = result._host
        self.host_ok[host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        host = result._host
        self.host_failed[host.get_name()] = result


def run_playbook(host_list, playbook_content):
    # 注意ansible.cfg中 host_key_checking参数设置为False，否则会导致新机器的ansible任务卡在ssh host key确认上
    # required for
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/inventory/manager.py#L204
    if not isinstance(host_list, list):
        raise Exception('host_list必须为ip列表')
    sources = ','.join(host_list)
    if len(host_list) == 1:
        sources += ','
    context.CLIARGS = ImmutableDict(connection='smart', module_path=None, forks=10,
                                    become=None, become_method=None, become_user=None,
                                    check=False, diff=False, verbosity=5, syntax=None, start_at_task=None)
    # initialize needed objects
    loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
    passwords = dict()

    # create inventory, use path to host config file as source or hosts in a comma separated string
    inventory = InventoryManager(loader=loader, sources=sources)

    # variable manager takes care of merging all the different sources to give you a unified view of variables available in each context
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    results_callback = ResultsCollectorJSONCallback()

    # Actually run it
    from utils.tools import get_ranstr
    tmp_yaml_path = '/tmp/{}.yaml'.format(get_ranstr(12))
    try:
        with open(tmp_yaml_path, 'w') as f:
            f.write(playbook_content)
        playbook = PlaybookExecutor(playbooks=[tmp_yaml_path], inventory=inventory,
                                    variable_manager=variable_manager, loader=loader, passwords=passwords)
        playbook._tqm._stdout_callback = results_callback
        playbook.run()

        print("UP ***********")
        for host, result in results_callback.host_ok.items():
            print('{0} >>> {1}'.format(host, result._result))

        print("FAILED *******")
        for host, result in results_callback.host_failed.items():
            print('{0} >>> {1}'.format(host, result._result['msg']))

        print("DOWN *********")
        for host, result in results_callback.host_unreachable.items():
            print('{0} >>> {1}'.format(host, result._result['msg']))

    except Exception as e:
        raise e
    finally:
        os.remove(tmp_yaml_path)
    # Remove ansible tmpdir

# content = '''---
# - hosts: all
#   remote_user: root
#   gather_facts: false
#   tasks:
#   - name: ping
#     ping:
#   - name: touch file
#     file: path=/tmp/20210507 state=touch '''
# run_playbook(['192.168.100.33'], content)
