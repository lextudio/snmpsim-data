.. include:: /includes/_links.rst

SNMP Simulation Data
====================

.. toctree::
   :maxdepth: 2

Free and open-source `SNMP simulator <https://www.pysnmp.com/snmpsim>`_ can
pretend to be one or many SNMP agents. But to be a reasonably convincing SNMP
agent, the simulator needs to serve SNMP managed objects that resemble the ones
served by real-world SNMP-enabled devices.

This package offers a collection of snapshots taken from various real hardware
devices and operating systems.

The data snapshots are distributed under 2-clause :doc:`BSD license </license>`.

Online Simulation
-----------------

.. note::

   Due to technical issues, the online simulation is currently running a
   different SNMP agent simulator, and the data served are different as well.

   We are working on bringing the online simulation back to the original.

All the packaged snapshots are also served by
`public SNMP simulator instance <http://demo.pysnmp.com>`_ under SNMP community
and context name identifiers noted in the documentation below.

For example, to read SNMP managed object of the Ubiquiti M5 Wi-Fi bridge:

.. code-block:: bash

   $ snmpget -v2c -c network/wifi/ubiquiti-m5 demo.pysnmp.com sysDescr.0

Local Simulation
----------------

If you prefer to have local simulation, follow `SNMP simulator documentation <https://www.pysnmp.com/snmpsim>`_
on how to set up simulation data. Besides other things, local installation will
let you add data variation calls into the otherwise static snapshots.

An example of local simulation setup is to use ``snmpsim-data-lextudio`` package
as below:

.. code-block:: bash

   $ pyenv local 3.12
   $ pip install pipenv
   $ pipenv install snmpsim-data-lextudio
   $ pipenv run setup-snmpsim-data ./data

This installs ``snmpsim-lextudio`` package as a dependency, and copy simulation
data into the ``data`` directory.

Invoke ``snmpsim-command-responder`` and point it to a directory with simulation
data:

.. code-block:: bash

   $ pipenv run snmpsim-command-responder --data-dir=data/UPS --agent-udpv4-endpoint=127.0.0.1:1024

This allows the simulator to read the specific files and emulate UPS devices.

Snapshots Contribution
----------------------

Consider donating some snapshots of SNMP data (e.g. ``snmpwalk``) as reported
by any real-world hardware to this SNMP simulator data project. Having the
real-world SNMP probes would benefit many SNMP implementers and testers.

Please create pull requests here against ``snmpsim-data`` package, and add your
``.snmpwalk`` or ``.snmprec`` files to the data directory. Alternatively, you
might give us a URL to download, or any other way.

.. warning::

   Just keep in mind that your SNMP dumps may contain sensitive information.
   Therefore it's best to collect ``.snmpwalk`` from non-production devices.

With your permission, we would then publish these ``.snmpwalk`` online.

Contact
-------

In case of questions or troubles using PySNMP, please open up a
new `GitHub issue`_ or ask on `Stack Overflow`_.

For other inquiries, please contact `LeXtudio Inc.`_.

More information about support options can be found in the following
section.

.. toctree::
   :maxdepth: 1

   Support Options <https://www.pysnmp.com/support>
