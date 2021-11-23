============
Zextras Docs
============

.. _docs_introduction:

Introduction
============

Zextras Docs is based on a heavily customized LibreOffice online package
allowing for collaborative editing of documents, spreadsheets and
presentations straight from the Zimbra WebClient.

.. warning:: Zextras Docs is not compatible with Zimbra version 8.8.11
   and lower.

.. _docs_components:

Components
==========

.. _docs_zextras_docs_server:

Zextras Docs Server
-------------------

The Zextras Docs server is the heart of the service. The service hosts
each document opened through a LibreOffice engine and responds to the
client via an image upon every keystroke and change in the document.

.. important:: This component must be installed on one or more
   dedicated nodes running Ubuntu 16.04 LTS, Ubuntu 18.04 LTS or Red
   Hat Centos 7.

.. _docs_zextras_docs_extension:

Zextras Docs Extension
----------------------

The extension is the key component which coordinates everything. Its
main tasks are:

-  Select which Docs server the next document will be opened on.

-  Redirect the client when it needs to open a document.

-  Read and write documents to and from system storage on behalf of the
   Docs server.

-  Connect to each Docs server via an administrative websocket and keep
   track of the availability and the resource usage of each.

-  Orchestrate concurrent user connections to the same document in the
   same server. (document sharing)

The Zextras Docs Extension is contained within the Zextras Core
component of Zextras Suite.

.. _docs_zextras_docs_zimlet:

Zextras Docs Zimlet
-------------------

A Zextras Docs Zimlet handles the integration with Drive items and with
email attachments. It is a thin web client which connects to a native
server instance via websocket, renders a document and only sends changes
to the client in order to keep the fidelity of the document on par with
a desktop client while at the same time reducing the bandwidth to the
bare minimum.

Documents in preview and attachments are shown in read-only mode with a
simplified interface, while edit mode has a full interface.

Its main tasks are:

-  Change the "create" button in the ZWC to the related Docs feature.

-  Change the preview feature to use Docs.

-  Allow the preview of documents.

.. _docs_minimum_system_requirements:

Minimum System Requirements
===========================

Following are the minimum system requirements to install Zextras Docs
server:

-  Centos 7, Ubuntu 16.04, or Ubuntu 18.04

-  At least 2 CPU cores

-  At least 4 GB RAM

-  At least 4 GB free disk space

.. _docs_browser_compatibility:

Browser compatibility
=====================

The following list shows which browsers are known to fully support all
Zextras features.

.. csv-table::
   :header: "Browser", "Version", "OS", "Supported"
   :file: browsercompatibility.csv

          
Items marked as ":fa:`check-circle;sd-text-warning` Limited" are only
supported on the browser’s two previous stable releases.

.. _docs_document_management_flow:

Document Management Flow
========================

This is what happens "behind the scenes" when a user creates a new
document:

1.  The Zimlet prompts the Extension to create a new empty document

2.  The Extension creates the document and returns the document’s ID to
    the client

3.  The Zimlet opens a new Zimbra tab containing an iframe pointing
    towards '/service/extension/wopi-proxy'

4.  The extension receives the request from the client, creates a new
    token for the needed document, and replies with a new url

5.  The new url points toward ``/docs/[docs-node-id]/[token]``, which
    will be proxied by nginx to the specific Docs Server node

6.  The Docs Server will respond with the web application in Javascript

7.  The web application opens a websocket connection, going through the
    nginx

8.  Docs Server receives the websocket connection along with a token,
    sends a ``read wopi`` command towards the mailbox url indicated in
    the parameters (the url is validates against allowed nodes)

9.  The Extension validates the token and replies with information and
    content

10. The Docs Server node parses the document, renders it and sends it
    back to the client.

11. The document is fully opened and editable.

::

   Open document
                                     redirect to docs
       +------------------------+             +----------------------+
       |     Zimbra Proxy       |             |       Mailbox        |
       |                        +------------->                      |
       |      Nginx             |             | Zextras Docs Extension|
       +------------------------+             +----------------------+
                         |                        |              ^
                         |                        |              |
                         |                        |             WOPI:
                         |                   Admin Web          Read/Write
                         |                   Socket             Documents
                         |                        |              |
                         |                        |              |
                         |                        |              |
                         |                    +---v----------------+
                         |                    |                    |
                         +-------------------->   Docs Server      |
                      Load Client             |                    |
                      Open client websocket   +--------------------+

.. _docs_networking_and_ports:

Networking and ports
====================

All mailbox servers will need to be able to directly communicate with
the Docs Server over port 8443 (HTTPS Backend), which must be open on
both ends.

The Docs Server communicates with the Extension through port 9980, so
incoming traffic from all mailbox and proxy servers to that port must be
allowed. The Docs Server component must also be able to directly
communicate with the master LDAP server as well as with all Proxy
servers.

.. _docs_installation_and_configuration:

Installation and Configuration
==============================

.. important:: This component must be installed on one or more
   dedicated nodes running Ubuntu 16.04 LTS, Ubuntu 18.04 LTS or Red
   Hat Centos 7.

.. _docs_docs_nodes:

Docs Nodes
----------

Download the ``zextras-docs.tgz`` standalone installer for your
distribution (`Centos 7
<https://download.zextras.com/zextras-docs-installer/latest/zextras-docs-centos7.tgz>`_
\| `Ubuntu 16
<https://download.zextras.com/zextras-docs-installer/latest/zextras-docs-ubuntu16.tgz>`_
\| `Ubuntu 18
<https://download.zextras.com/zextras-docs-installer/latest/zextras-docs-ubuntu18.tgz>`_),
extract it and as the *root* user execute the ``install.sh`` script
contained in the package.

To obtain the information required for the initial Docs Server setup,
run the following command on any mailbox server:

::

   zimbra@mbx1:~$ zmlocalconfig -s ldap_master_url zimbra_ldap_user zimbra_ldap_userdn zimbra_ldap_password

This will return the info you need in the following format:

::

   ldap_master_url = ldap://ldap01.cfd6a9e5.test.example.com:389
   zimbra_ldap_user = zimbra
   zimbra_ldap_userdn = uid=zimbra,cn=admins,cn=zimbra
   zimbra_ldap_password = Deyked4ofMarj

The script will install the Zextras Docs package and then ask the
information about the master ldap, url, username and password, which
will be used to add a new server in the LDAP with just the 'docs'
service installed/enabled. Every Docs Server will be visible by every
node, and will read the LDAP in order to write the configuration in
``/opt/zimbra/conf/docs/loolwsd.xml``.

Once the setup is completed no other configuration is needed.

.. _docs_docs_server_download_links: 

Docs Server download links
--------------------------

.. _docs_adding_custom_fonts_to_the_docs_server:

Adding Custom Fonts to the Docs Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add Custom Fonts to your Docs Server, simply copy the ``.ttf`` font
files in the ``/opt/zimbra/docs/core/share/fonts/truetype/`` directory,
then generate the new font cache and restart the docs server running
``zdocs restart`` as ``root``.

To generate the new font cache, run the following command based on the
Docs Server’s Operating System:

.. tab-set::

      .. tab-item:: Ubuntu 16 and 18

         ``dpkg-reconfigure zextras-docs-server``

      .. tab-item:: CentOS 7

         ``fc-cache /opt/zimbra/docs/zextras-docs-core/share/fonts``

.. warning:: The server will briefly be unavailable during the
   restart, and clients will need to close and open again any open
   document to see the new fonts in the list.

.. _docs_mailbox_nodes:

Mailbox Nodes
-------------

While the Zextras Docs extension is already contained within Zextras
Suite, the com_zextras_docs Zimlet needs to be deployed on the server
and enabled on all users and COS that need to have access to the Zextras
Docs features.

The ``com_zextras_docs`` Zimlet can be deployed from the "Core" section
of the Zextras Adminictration Zimlet.

No configuration on the mailboxd side is needed after the Zimlet has
been deployed and enabled.

.. _docs_proxy_nodes:

Proxy Nodes
-----------

The proxy configuration must be re-generated after adding one or more
Zextras Docs Servers to the infrastructure: to do so, run
``/opt/zimbra/libexec/zmproxyconfgen`` as the *zimbra* user and then
restart the proxy service running ``zmproxyctl restart`` as the same
user.

The new docs nodes will be read from ldap and no manual configuration is
needed.

.. _docs_licensing:

Licensing
=========

**Zextras Docs is included in every Zextras Suite Pro license..**

The standalone installer is released under the MPLv2 license while the
extension and Zimlet are released under a proprietary license.

.. _docs_removal:

Removal
=======

Before uninstalling the software the node must be removed form LDAP
either from the docs node via command::

  zdocs remove-local-server

or via the zmprov command from any zimbra node::

  zmprov deleteServer {servername}

.. _docs_commands:

Commands
========

.. _docs_zextras_docs_server_cli_zdocs:

Zextras Docs Server CLI - zdocs
-------------------------------

On Docs server zdocs (/usr/local/bin/zdocs as root) command can generate
the config for lool (it’s already on cron), add/remove the docs server
from ldap, test configuration and manage the service.

**``zdocs`` command.**

.. code:: bash

   usage: zdocs [-h] [--auto-restart] [--ldap-dn LDAP_DN] [--ldap-pass LDAP_PASS]
                [--ldap-url LDAP_URL] [--hostname HOSTNAME] [--debug][--cron]

   {genkey,write-local-server,remove-local-server,generate-config,ldap-write-config,ldap-test,start,stop,restart,status,setup}

   Manage Zextras Docs service.

   Available commands:
     genkey                Generate a private key needed for authentication between docs and mailbox servers.
     write-local-server    Add or update in LDAP the necessary server entry for this server in order to be reachable from other servers.
     remove-local-server   Remove local server entry in LDAP.
     generate-config       Populate the config template with ldap values and write a new configuration file.
     ldap-write-config     Write new configuration about the ldap access needed to generate the docs configuration file.
     ldap-test             Check the ldap connection.
     start                 Start the service.
     stop                  Stop the service.
     restart               Restart the service.
     status                Print service status.
     setup                 Start the initial setup.

   positional arguments:
   {genkey,write-local-server,remove-local-server,generate-config,ldap-write-config,ldap-test,start,stop,restart,status,setup}

   optional arguments:
     -h, --help            show this help message and exit
     --auto-restart        Automatically restart the service if configuration is changed (to be used with generate-config)
     --ldap-dn LDAP_DN     Ldap dn (distinguish name) to bind to (to be used with ldap-test and ldap-settings)
     --ldap-pass LDAP_PASS Ldap password used of the DN (to be used with ldap-test and ldap-settings)
     --ldap-url LDAP_URL   Ldap url completed with schema (ex.: ldaps://ldap.example.com, to be used with ldap-test and ldap-settings)
     --hostname HOSTNAME   Hostname of this server (to be used with add-local-server)
     --debug               Show complete errors when things go bad.
     --cron                Start in cron mode, avoid any output unless there is an error (to be used with generate-config).

   examples:
   #regenerate the config and restart the server if config changed
     zdocs --auto-restart generate-config
   #restart the service
     zdocs restart
   #check ldap connection availability using current settings
     zdocs ldap-test
   #check ldap connection using custom settings
     zdocs --ldap-url ldaps://ldap.example.com/ --ldap-dn 'uid=zimbra,cn=admins,cn=zimbra' --ldap-pass password ldap-test
   #change the ldap connection settings
     zdocs --ldap-url ldap://ldap2.example.com/ --ldap-dn 'uid=zimbra,cn=admins,cn=zimbra' --ldap-pass password
   ldap-write-config
   #add the local server
     zdocs write-local-server
   #add the local server with a custom hostname in LDAP, this command should be already invoked during setup.
     zdocs --hostname myhostname write-local-server
   #remove the local server from LDAP, useful when destroying the server, you can also use 'zmprov deleteServer' from a mailbox server.
     zdocs remove-local-server

.. _docs_zextras_docs_extension_cli_zxsuite_docs:

Zextras Docs Extension CLI - zxsuite docs
-----------------------------------------

On a Mailbox server, the ``zxsuite docs`` command is available. This
command allows to check and control the Docs service’s status, to
force a configuration reload and to see the Docs Servers'
status. Please refer to section :ref:`docs_zextras_docs_cli`.

.. _docs_troubleshooting:

Troubleshooting
===============

.. grid::
   :gutter: 3
            
   .. grid-item-card::
      :class-header: sd-font-weight-bold
              
      Nothing happens when opening a document / extension requests
      returns 503
      ^^^^^
      
      This is most likely due to a connection issue between the
      mailbox server and the Docs server. Check the ``mailbox.log``
      and see the reason for the connection failure. If there are no
      connection errors, check the Docs server with ``zdocs status``
      on the docs node.

      The mailbox will log every connection and disconnection for each
      Docs server.

   .. grid-item-card::
      :class-header: sd-font-weight-bold
   
      404 error code instead of docs
      ^^^^^

      The proxy configuration needs to be re-generated and the proxy
      restarted

   .. grid-item-card::
      :class-header: sd-font-weight-bold

      Docs opens but a message “this is embarrassing…​” appears instead
      of the document
      ^^^^^

      This happens if the Docs server cannot connect back to the
      mailbox server to read and write the document. Check name
      resolution and SSL certificate of mailboxd which must be valid
      for the Docs server that does not inherit Zimbra certificate
      management.

.. _docs_zextras_docs_cli:

Zextras Docs CLI
================

This section contains the index of all the available ``zextras docs``
commands. Full reference can be found in `the dedicated
section <./cli.xml#_zxdocs_cli_commands>`_.

`doDeployDocsZimlet <./cli.xml#docs_doDeployDocsZimlet>`_ \|
`doReloadConfig <./cli.xml#docs_doReloadConfig>`_ \|
`doRestartService <./cli.xml#docs_doRestartService>`_ \|
`doStartService <./cli.xml#docs_doStartService>`_ \|
`doStopService <./cli.xml#docs_doStopService>`_ \|
`getServices <./cli.xml#docs_getServices>`_ \|
`status <./cli.xml#docs_status>`_
