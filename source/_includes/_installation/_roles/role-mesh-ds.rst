
.. tab-set::

   .. tab-item:: Ubuntu
      :sync: ubuntu

      .. code:: console

         # apt install service-discover-server \
         carbonio-directory-server carbonio-message-broker \
         carbonio-storages
 
   .. tab-item:: RHEL
      :sync: rhel

      .. code:: console

         # dnf install service-discover-server \
         carbonio-directory-server carbonio-message-broker \
         carbonio-storages

Please note:

* Unlike other client-server software (like e.g., PostgreSQL), the
  ``service-discover`` software on which |product| is based does not
  require the agent to be installed along the server, therefore the
  ``service-discover-agent`` package is needed only in the other
  nodes

* The ``carbonio-message-broker`` package is unique within a |product|
  infrastructure
