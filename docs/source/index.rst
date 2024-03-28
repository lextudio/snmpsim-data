.. include:: /includes/_links.rst

SNMP Simulation Data
====================

.. toctree::
   :maxdepth: 2

   Return to PySNMP Homepage <https://pysnmp.com>

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

   $ pipenv run snmpsim-command-responder --data-dir=data/UPS --agent-udpv4-endpoint=127.0.0.1:1611
   Using "NullReporter" activity reporting method with params  
   Scanning "/Users/lextm/.snmpsim/variation" directory for variation modules... 
   Directory "/Users/lextm/.snmpsim/variation" does not exist 
   Scanning "/usr/local/share/snmpsim/variation" directory for variation modules... 
   Directory "/usr/local/share/snmpsim/variation" does not exist 
   ...
   --- SNMP Engine configuration 
   SNMPv3 EngineID: 0x80004fb8054d6163426f6f6b2d50726f2e6c6f636181182200 
   --- Simulation data recordings configuration 
   SNMPv3 Context Engine ID: 0x80004fb8054d6163426f6f6b2d50726f2e6c6f636181182200 
   Scanning "data/UPS" directory for  *.dump, *.MVC, *.sapwalk, *.snmpwalk, *.snmprec, *.snmprec.bz2 data files... 
    ...
    SNMPv1/2c community name: huawei-gse200m 
    SNMPv3 Context Name: fc2f7455eda7c40ed64d477cd0841be9 or huawei-gse200m 
    Configuring data/UPS/apc-8932.snmprec controller 
    SNMPv1/2c community name: apc-8932 
    SNMPv3 Context Name: f748dc2efe5004933c1edd2463556ef3 or apc-8932 
   --- SNMPv3 USM configuration 
   SNMPv3 USM SecurityName: simulator 
   SNMPv3 USM authentication key: auctoritas, authentication protocol: MD5 
   SNMPv3 USM encryption (privacy) key: privatus, encryption protocol: DES 
   Maximum number of variable bindings in SNMP response: 64 
   --- Transport configuration 
   Listening at UDP/IPv4 endpoint 127.0.0.1:1611, transport ID 1.3.6.1.6.1.1.0 

You can see from the console output that the simulator reads the data files and
starts to emulate UPS devices. And to test out you need one of the commands like

.. code-block:: bash

   $ snmpget -v2c -c apc-8932 localhost:1611 sysDescr.0
   SNMPv2-MIB::sysDescr.0 = STRING: APC Web/SNMP Management Card (MB:v4.1.0 PF:v6.7.2 PN:apc_hw05_aos_672.bin AF1:v6.7.2 AN1:apc_hw05_rpdu2g_672.bin MN:AP8932 HR:02 SN: 3F503A169043 MD:01/23/2019)

.. note::

   ``apc-8932`` is the v1/2c community name for the emulated UPS device, and the
   original data file is ``data/UPS/apc-8932.snmprec``. Such information can be
   found in ``snmpsim-command-responder`` console output.

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
