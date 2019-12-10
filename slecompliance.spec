#
# spec file for package slecompliance
#
# Copyright (c) 2019 SUSE Linux GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           slecompliance
Version:        1.0.0
Release:        0
Summary:        Generate compliance report for running SLES instances
Group:          System/Monitoring
License:        GPL-3.0+
Url:            https://github.com/SUSE-Enceladus/sle-compliance
Source0:        %{name}-%{version}.tar.bz2
Requires:       python3
Requires:       python3-boto3 >= 1.4.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Generate a report for running SLES instances with respect to the compliance
status. An instance that access the SUSE operated update infrastructure
is compliant if it has the proper billing construct.

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 usr/bin/* %{buildroot}/%{_bindir}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/* %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/*

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/slecompliancereport
%{_mandir}/man*/*
