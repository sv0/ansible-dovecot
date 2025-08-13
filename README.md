Ansible Dovecot
===============

[![CI](https://github.com/sv0/ansible-dovecot/actions/workflows/ci.yml/badge.svg)](https://github.com/sv0/ansible-dovecot/actions/workflows/ci.yml)

This ansible role installs and configures [Dovecot](https://www.dovecot.org/).
The Secure IMAP server.

It has been tested for the following systems:

* Linux
  * Debian Bookworm
  * Debian Trixie
* OpenBSD 7.6
* NetBSD 10.1

Requirements
------------

* Python >=3.9 on Ansible controller host.
* [ansible-core](https://pypi.org/project/ansible-core/) version >= 2.14, <2.20


Default Variables
-----------------

Directory where TLS certificate could be found.
I use ACME client [dehydrated](https://dehydrated.io),
so all otained certificates are in `/var/lib/dehydrated/certs`

```yaml
certificate_dir: "/var/lib/dehydrated/certs"
```

see `defaults/main.yml` for more details.

Dependencies
------------

Install
--------

Download latest release with `ansible-galaxy`

```shell
    ansible-galaxy role install sv0.dovecot
```

Playbook
--------

```yaml
    - hosts: servers
      roles:
        - sv0.dovecot
      vars:
        certificate_dir: "/var/lib/dehydrated/certs"
```

Tests
-----

Run local tests with

```shell
    molecule test
```

Requires Molecule and Docker to be installed on devel host.

License
-------

MIT

Author Information
------------------

[Slavik Svyrydiuk](https://slavik.svyrydiuk.eu/about.html)

Usefull links
-------------

- [DOVECOT. The Secure IMAP server](https://www.dovecot.org/)
