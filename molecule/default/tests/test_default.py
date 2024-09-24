import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("dovecot-core", "any"),
    ("dovecot-imapd", "any"),
    ("dovecot-lmtpd", "any"),
    ("dovecot-sieve", "any"),
    ("python3", "3"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if version != 'any':
        assert pkg.version.startswith(version)


@pytest.mark.parametrize("dirs", [
    "/var/lib/dovecot",
    "/etc/dovecot",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/dovecot/dovecot.conf",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_some_command_output(host):
    run = host.run("cat /etc/os-release")
    out = run.stdout+run.stderr
    assert "NAME" in out
