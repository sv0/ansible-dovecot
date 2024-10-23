Ansible Dovecot
===============

[![CI](https://github.com/sv0/ansible-dovecot/actions/workflows/ci.yml/badge.svg)](https://github.com/sv0/ansible-dovecot/actions/workflows/ci.yml)

Install and configure [Dovecot](https://www.dovecot.org/).
The Secure IMAP server.

Requirements
------------

- Debian 12 (Bookworm)
- OpenBSD 7.6

Default Variables
-----------------

Directory where TLS certificate could be found.
I use ACME client [dehydrated](https://dehydrated.io),
so all otained certificates are in `/var/lib/dehydrated/certs`

```yaml
dovecot_certificate_dir: "/var/lib/dehydrated/certs"
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
        dovecot_certificate_dir: "/var/lib/dehydrated/certs"
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
