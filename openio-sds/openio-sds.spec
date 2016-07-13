%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define cli_name oio
%define tarname  oio-sds

Name:           openio-sds

%if %{?_with_test:0}%{!?_with_test:1}
Version:        2.1.0.c0
Release:        2%{?dist}
%define         tarversion %{version}
Source0:        https://github.com/open-io/oio-sds/archive/%{tarversion}.tar.gz
%else
# Testing purpose only. Do not modify.
%define         date %(date +"%Y%m%d%H%M")
%global         shortcommit %(c=%{tag}; echo ${c:0:7})
Version:        test%{date}.git%{shortcommit}
Release:        0%{?dist}
%define         tarversion %{tag}
Source0:        https://github.com/open-io/oio-sds/archive/%{tarversion}.tar.gz
Epoch:          1
%endif

Summary:        OpenIO Cloud Storage Solution
License:        AGPL
URL:            http://www.openio.io/
Source1:        openio-sds.tmpfiles


BuildRequires:  glib2-devel              >= 2.28.8
%if %{?fedora}0
BuildRequires:  zookeeper-devel          >= 3.3.4
%else
BuildRequires:  zookeeper-lib-devel      >= 3.3.4
%endif
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  zeromq3-devel
BuildRequires:  libcurl-devel
BuildRequires:  apr-devel                >= 1.2
BuildRequires:  sqlite-devel             >= 3.7.11
BuildRequires:  libattr-devel            >= 2.4.32
%if %{?el6}0
BuildRequires:  compat-libevent-20-devel >= 2.0
%else
BuildRequires:  libevent-devel           >= 2.0
%endif
BuildRequires:  httpd-devel              >= 2.2
BuildRequires:  lzo-devel                >= 2.0
BuildRequires:  openio-asn1c             >= 0.9.27
BuildRequires:  cmake,bison,flex
BuildRequires:  librain-devel
BuildRequires:  libdb-devel
BuildRequires:  json-c                   >= 0.12
BuildRequires:  json-c-devel             >= 0.12


%description
OpenIO software storage solution is designed to handle PETA-bytes of
data in a distributed way, data such as: images, videos, documents, emails,
and any other personal unstructured data.
OpenIO is a fork of Redcurrant, from Worldline by Atos.


%package common
Summary: common files for OpenIO Cloud Storage Solution
Requires:       expat
Requires:       glib2         >= 2.28
Requires:       openio-asn1c  >= 0.9.27
Requires:       zlib
Requires:       json-c        >= 0.12
%if %{?fedora}0
BuildRequires:  zookeeper     >= 3.3.4
%else
BuildRequires:  zookeeper-lib >= 3.3.4
%endif
%description common
OpenIO software storage solution is designed to handle PETA-bytes of
data in a distributed way, data such as: images, videos, documents, emails,
and any other personal unstructured data.
OpenIO is a fork of Redcurrant, from Worldline by Atos.
This package contains common files used by other OpenIO SDS packages.


%package server
Summary: Server files for OpenIO Cloud Storage Solution
%if %{?_with_test:0}%{!?_with_test:1}
Requires:       %{name}-common = %{version}
%else
Requires:       %{name}-common = 1:%{version}
%endif
%if %{?fedora}0
BuildRequires:  zookeeper          >= 3.3.4
Requires:       python-zookeeper
%else
BuildRequires:  zookeeper-lib      >= 3.3.4
Requires:       python-ZooKeeper
%endif
Requires:       python             >= 2.7
Requires:       apr                >= 1.2
Requires:       sqlite             >= 3.7.11
Requires:       libattr            >= 2.4.32
%if %{?el6}0
Requires:       compat-libevent-20 >= 2.0
%else
BuildRequires:  libevent           >= 2.0
%endif
Requires:       leveldb
Requires:       lzo                >= 2.0
Requires:       openio-asn1c       >= 0.9.27
Requires:       python-gunicorn    >= 19.4.5
Requires:       python-flask,python-eventlet,python-zmq,python-redis,python-requests,python-plyvel,PyYAML
Requires:       pyxattr            >= 0.4
Requires:       python-simplejson  >= 2.0.9
# Python oiopy dependencies
Requires:       python-eventlet >= 0.15.2, python-requests, python-cliff-tablib, python-cliff >= 1.13, python-tablib, python-pyeclib >= 1.2.0
%description server
OpenIO software storage solution is designed to handle PETA-bytes of
data in a distributed way, data such as: images, videos, documents, emails,
and any other personal unstructured data.
OpenIO is a fork of Redcurrant, from Worldline by Atos.
This package contains all needed server files to run OpenIO SDS
solution.


%package common-devel
Summary: Header files for OpenIO Cloud Storage Solution
%if %{?_with_test:0}%{!?_with_test:1}
Requires:       %{name}-common = %{version}
%else
Requires:       %{name}-common = 1:%{version}
%endif
%description common-devel
OpenIO software storage solution is designed to handle PETA-bytes of
data in a distributed way, data such as: images, videos, documents, emails,
and any other personal unstructured data.
OpenIO is a fork of Redcurrant, from Worldline by Atos.
This package contains header files for OpenIO SDS solution client.


%package mod-httpd
Summary: Apache HTTPd module for OpenIO Cloud Storage Solution
%if %{?_with_test:0}%{!?_with_test:1}
Requires:       %{name}-server  = %{version}
%else
Requires:       %{name}-server  = 1:%{version}
%endif
Requires:       httpd          >= 2.2
Requires:       libdb
%description mod-httpd
OpenIO software storage solution is designed to handle PETA-bytes of
data in a distributed way, data such as: images, videos, documents, emails,
and any other personal unstructured data.
OpenIO is a fork of Redcurrant, from Worldline by Atos.
This package contains Apache HTTPd module for OpenIO SDS solution.


%package tools
Summary: Side tools for OpenIO Cloud Storage Solution
%if %{?_with_test:0}%{!?_with_test:1}
Requires:       %{name}-server = %{version}
%else
Requires:       %{name}-server = 1:%{version}
%endif
%description tools
penIO software storage solution is designed to handle PETA-bytes of
data in a distributed way, data such as: images, videos, documents, emails,
and any other personal unstructured data.
OpenIO is a fork of Redcurrant, from Worldline by Atos.
This package contains side tools for OpenIO SDS solution.



%prep
%setup -q -n %{tarname}-%{tarversion}


%build
cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
  -DEXE_PREFIX="%{cli_name}" \
  -DZK_LIBDIR="%{_libdir}" \
  -DZK_INCDIR="%{_includedir}/zookeeper" \
  -DLZO_INCDIR="%{_includedir}/lzo" \
  -DSOCKET_OPTIMIZED=1 \
  -DOIOSDS_RELEASE=%{version} \
  "-DGCLUSTER_AGENT_SOCK_PATH=\"/run/oio/sds/sds-agent-0.sock\"" \
  .

make %{?_smp_mflags}

# Build python
PBR_VERSION=0.0.1 %{__python} setup.py build


%install
make DESTDIR=$RPM_BUILD_ROOT install

# Install python
PBR_VERSION=0.0.1 %{__python} ./setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


# Install OpenIO SDS directories
%{__mkdir_p} -v ${RPM_BUILD_ROOT}%{_localstatedir}/log/oio/sds \
  ${RPM_BUILD_ROOT}%{_sharedstatedir}/oio/sds \
  ${RPM_BUILD_ROOT}%{_sysconfdir}/oio/sds \
  ${RPM_BUILD_ROOT}%{_datarootdir}/%{name}-%{version}

# Install tmpfiles
%{__mkdir_p} -v ${RPM_BUILD_ROOT}%{_tmpfilesdir} ${RPM_BUILD_ROOT}/run/oio/sds
%{__install} -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/openio-sds.conf


%files common
%defattr(755,root,root,755)
%{_libdir}/libgridcluster-conscience.so*
%{_libdir}/libgridcluster.so*
%{_libdir}/libhcresolve.so*
%{_libdir}/libmeta0utils.so*
%{_libdir}/libmetautils.so*
%{_libdir}/libmeta0remote.so*
%{_libdir}/libmeta1remote.so*
%{_libdir}/libmeta2v2remote.so*
%{_libdir}/liboio*
# TODO find why libserver is necessary in common
%{_libdir}/libserver.so*
# TODO find why libsqliterepo is necessary in common
%{_libdir}/libsqliterepo.so*
%{_libdir}/libsqlitereporemote.so*
%{_libdir}/libsqlxsrv.so*
%{_libdir}/libmeta2v2utils.so*
%{_libdir}/libsqliteutils.so*
%{_bindir}/%{cli_name}-daemon
%defattr(0644,openio,openio,0755)
%{_sysconfdir}/oio
%{_localstatedir}/log/oio
%defattr(0640,openio,openio,0750)
%{_sharedstatedir}/oio
/run/oio
%dir %{_datarootdir}/%{name}-%{version}

%files server
%defattr(755,root,root,755)
%{_libdir}/grid/msg_conscience.so*
%{_libdir}/grid/msg_fallback.so*
%{_libdir}/grid/msg_ping.so*
%{_libdir}/grid/msg_stats.so*
%{_libdir}/libmeta0v2.so*
%{_libdir}/libmeta1v2.so*
%{_libdir}/libmeta2v2.so*
%{_libdir}/libmeta2v2utils.so*
%{_libdir}/librawx.so*
%{_libdir}/libserver.so*
%{_libdir}/libsqliterepo.so*
%{_libdir}/libsqliteutils.so*
%{_bindir}/%{cli_name}-account-server
%{_bindir}/%{cli_name}-blob-auditor
%{_bindir}/%{cli_name}-blob-indexer
%{_bindir}/%{cli_name}-blob-mover
%{_bindir}/%{cli_name}-blob-rebuilder
%{_bindir}/%{cli_name}-conscience-agent
%{_bindir}/%{cli_name}-cluster
%{_bindir}/%{cli_name}-crawler-storage-tierer
%{_bindir}/%{cli_name}-echo-server
%{_bindir}/%{cli_name}-event-agent
%{_bindir}/%{cli_name}-meta0-init
%{_bindir}/%{cli_name}-meta0-client
%{_bindir}/%{cli_name}-meta0-server
%{_bindir}/%{cli_name}-meta1-server
%{_bindir}/%{cli_name}-meta2-server
%{_bindir}/%{cli_name}-meta1-client
%{_bindir}/%{cli_name}-rawx-compress
%{_bindir}/%{cli_name}-rawx-uncompress
%{_bindir}/%{cli_name}-rdir-server
%{_bindir}/%{cli_name}-sqlx
%{_bindir}/%{cli_name}-sqlx-server
%{_bindir}/%{cli_name}-tool
%{_bindir}/%{cli_name}-proxy
%{_bindir}/zk-bootstrap.py*
%{_bindir}/openio
%defattr(644,root,root,755)
%{python_sitelib}/oio*
/usr/lib/tmpfiles.d/openio-sds.conf

%files common-devel
%defattr(644,root,root,755)
%{_prefix}/include/*
%{_libdir}/pkgconfig/oio-sds.pc

%files mod-httpd
%defattr(755,root,root,755)
%{_libdir}/httpd/modules/mod_dav_rawx.so*

%files tools
%defattr(755,root,root,755)
%{_bindir}/%{cli_name}-bootstrap.py
%{_bindir}/%{cli_name}-reset.sh
%{_bindir}/zk-reset.py
%{_bindir}/%{cli_name}-unlock-all.sh
%{_bindir}/%{cli_name}-wait-scored.sh


%pre common
# Add user and group "openio" if not exists
getent group openio >/dev/null || groupadd -g 220 openio
if ! getent passwd openio >/dev/null; then
  useradd -M -d /var/lib/oio -s /bin/bash -u 120 -g openio -c "OpenIO services" openio
fi

%post common
/sbin/ldconfig
%post server
/sbin/ldconfig
%post mod-httpd
/sbin/ldconfig

%postun common
/sbin/ldconfig
%postun server
/sbin/ldconfig
%postun mod-httpd
/sbin/ldconfig

%changelog
* Fri Jun 17 2016 - 2.1.0.XX-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Python API (python-oiopy) is now part of the core
* Tue May 17 2016 - 2.1.0.c0-2%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Recompile with CMAKE_BUILD_TYPE="RelWithDebInfo"
* Mon May 09 2016 - 2.1.0.c0-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Testing new release 2.1.0.c0
* Tue Apr 19 2016 - 2.0.0-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
* Fri Apr 15 2016 - 2.0.0.c3-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release candidate
* Wed Mar 16 2016 - 2.0.0.c2-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release candidate
- Fix %defattr warnings
- Add files
* Thu Mar 03 2016 - 2.0.0.c1-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release candidate (change major version)
* Thu Feb 25 2016 - 1.1.rc0-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release cadidate
* Mon Dec 14 2015 - 1.0.1-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
- Renamed package client-devel to common-devel
* Tue Dec 01 2015 - 1.0.0-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release 1.0.0
* Wed Sep 16 2015 - 0.8.3-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Mon Sep 14 2015 - 0.8.2-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Thu Sep 10 2015 - 0.8.1-2%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Wed Sep 02 2015 - 0.8.1-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Fri Aug 28 2015 - 0.8.0-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
- Remove Net-SNMP package
* Fri Jul 03 2015 - 0.7.6-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Tue Jun 30 2015 - 0.7.5-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Tue Jun 30 2015 - 0.7.4-2%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Remove integrityloop package
* Mon Jun 29 2015 - 0.7.4-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Mon Jun 22 2015 - 0.7.3-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Wed Jun 17 2015 - 0.7.2-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Wed Jun 17 2015 - 0.7.1-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Tue Jun 09 2015 - 0.7-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
- Removed useless BuildRequires
- Add python dependencies in server
* Thu May 28 2015 - 0.6.6-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Tue May 26 2015 - 0.6.5-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Sun May 17 2015 - 0.6.4-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Fri May 15 2015 - 0.6.3-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Wed May 13 2015 - 0.6.2-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Tue May 12 2015 - 0.6.1-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Mon May 11 2015 - 0.6-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
* Fri Apr 24 2015 - 0.5-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
* Thu Apr 09 2015 - 0.3-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- New release
* Wed Mar 25 2015 - 0.2.2-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Bugfix release
* Thu Mar 19 2015 - 0.2.1-1%{?dist} - Romain Acciari <romain.acciari@openio.io>
- Initial release
