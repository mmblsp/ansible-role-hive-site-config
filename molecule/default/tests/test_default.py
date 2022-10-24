import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    """test isinstance file"""
    hive_site_conf = host.file('/etc/hive/hive-site.conf')

    assert hive_site_conf.exists
    assert hive_site_conf.user == 'root'
    assert hive_site_conf.group == 'root'
