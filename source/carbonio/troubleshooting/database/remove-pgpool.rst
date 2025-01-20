.. _remove-pgpool:

================
 Pgpool Removal
================

In version 24.12.0, the **Database Connector** Role does not exist
anymore, therefore the Pgpool software must be removed and |product|'s
``*-db`` packages must be moved away from the node that features the
Database Connector Role. This section presents all the tasks you need
to carry out to accomplish the goal.

The procedure is organised in 3 main parts and requires to log in to
the Nodes where the *Database* and *Database Connector* Roles are
installed and execute commands as the ``root`` user. The commands are
the same on Ubuntu and RHEL operating systems, unless explicitly
stated.

Before starting the procedure make sure that:

* You have SSH or console access to the *Database* and
  *Database Connector* nodes

* You need to account for some downtime, because |product| might lose
  connection with the PostgreSQL database.

* You have taken a backup of the Nodes (or the VMs), also because
  after this procedure you will proceed to upgrade |product|

* Execute each command on the Node that is mentioned

* You have carefully read the remainder of this section, to have an
  overview of the procedure and understand all the steps to be carried
  out

The *Database* and *Database Connector* Roles are usually installed on
different Nodes, but if they are installed on the same Node, you only
need to carry out these two tasks: :ref:`pg-disable` and
:ref:`pg_restart`.

.. _pg-disable:

Disable Pgpool
==============

On the Node with the *Database Connector* Role, execute the following
commands to disable pgpool and the corresponding Prometheus exporter.

.. code:: console

   # systemctl mask pgpool2.service
   # systemctl mask carbonio-prometheus-pgpool-exporter.service

Then reconfigure PostgreSQL to change the port it listens to.

.. code:: console

   # su - postgres -c "psql --command=\"ALTER SYSTEM SET port TO '5432';\""

.. _pg-install:

Install Database Components
===========================

.. note:: Skip this step if PostgreSQL and Pgpool are installed on the
   same Node.

On the Node with the **Database** Role, install all the packages
listed.

.. tab-set::

   .. tab-item:: Ubuntu
      :sync: ubuntu

      .. code:: console

         # apt install carbonio-docs-connector-db carbonio-files-db \
         carbonio-mailbox-db carbonio-message-dispatcher-db \
         carbonio-ws-collaboration-db carbonio-tasks-db

   .. tab-item:: RHEL
      :sync: rhel

      .. code:: console

         # dnf install carbonio-docs-connector-db carbonio-files-db \
         carbonio-mailbox-db carbonio-message-dispatcher-db \
         carbonio-ws-collaboration-db carbonio-tasks-db

Add the services provided by these packages to |mesh|.

.. code:: console

   # pending-setups -a

.. _pg-services:

Disable Services
================

On the Node with the *Database Connector* Role, disable all services.

.. code:: console

   # systemctl disable pgpool2.service
   # systemctl disable carbonio-prometheus-pgpool-exporter.service
   # systemctl disable carbonio-mailbox-db-sidecar.service
   # systemctl disable carbonio-docs-connector-db-sidecar.service
   # systemctl disable carbonio-files-db-sidecar.service
   # systemctl disable carbonio-message-dispatcher-db-sidecar.service
   # systemctl disable carbonio-notification-push-db-sidecar.service
   # systemctl disable carbonio-tasks-db-sidecar.service
   # systemctl disable carbonio-ws-collaboration-db-sidecar.service

.. _pg-clean:

Remove Packages
===============

On the Node with the *Database Connector* Role, remove all the
packages that are not needed anymore.

.. warning:: Pay attention to the actual packages that are removed by
   the following command. If among the packages that are going to be
   removed there are some packages that are essential for |product|,
   do not remove any packages.

.. tab-set::

   .. tab-item:: Ubuntu
      :sync: ubuntu

      .. code:: console

         # apt remove pgpool carbonio-docs-connector-db \
         carbonio-files-db carbonio-mailbox-db \
         carbonio-message-dispatcher-db \
         carbonio-notification-push-db carbonio-ws-collaboration-db \
         carbonio-prometheus-pgpool-exporter carbonio-tasks-db

   .. tab-item:: RHEL
      :sync: rhel

      .. code:: console

         # dnf remove pgpool-II carbonio-docs-connector-db \
         carbonio-files-db carbonio-mailbox-db \
         carbonio-message-dispatcher-db \
         carbonio-notification-push-db carbonio-ws-collaboration-db \
         carbonio-prometheus-pgpool-exporter carbonio-tasks-db

.. _pg_restart:

Restart Services
================

The last task is to restart all services.

.. tab-set::

   .. tab-item:: Ubuntu
      :sync: ubuntu

      As the ``zextras`` user, execute

      .. code:: console

         zextras$ zmcontrol restart

   .. tab-item:: RHEL
      :sync: rhel


      As the ``zextras`` user, execute

      .. code:: console

         zextras$ zmcontrol restart

   .. tab-item:: RHEL 9
      :sync: rhel 9

      As the ``user`` user, execute on each Node one or more  of the
      following commands.

      .. hint:: If the command fails, it means that on the Node that
         target does not exist, so disregard any error message.

      .. code:: console

         # systemctl restart carbonio-directory-server.target
         # systemctl restart carbonio-appserver.target
         # systemctl restart carbonio-mta.target
         # systemctl restart carbonio-proxy.target

.. _pg-checks:

Final Checks
============

To make sure that |mesh| was correctly updated and notified that the
DB components have been moved to a different node, you can check from
the :ref:`mesh-gui` whether the services are reportedly running on the
correct node.
