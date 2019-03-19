Name:           squeezed
Version:        0.19.0
Release:        7%{?dist}
Summary:        Memory ballooning daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/squeezed
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/squeezed/archive?at=v0.19.0&format=tar.gz&prefix=squeezed-0.19.0#/squeezed-0.19.0.tar.gz) = 3ff31b91e839e0d6b1af248f2ead3b025a9df2b4
Source1:        squeezed.service
Source2:        squeezed-sysconfig
Source3:        squeezed-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  opam
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-dom0-libs
BuildRequires:  xen-libs-devel
BuildRequires:  xen-libs
BuildRequires:  systemd
BuildRequires:  systemd-devel
Requires:       message-switch

%{?systemd_requires}

%description
Memory ballooning daemon for the xapi toolstack.

%prep
%autosetup -p1

%build
make

%install
make install DESTDIR=%{buildroot}%{_sbindir}
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/squeezed.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/squeezed
%{__install} -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/squeezed.conf

%files
%doc README.md 
%doc LICENSE 
%doc MAINTAINERS
%{_sbindir}/squeezed
%{_unitdir}/squeezed.service
%config(noreplace) %{_sysconfdir}/sysconfig/squeezed
%config(noreplace) %{_sysconfdir}/squeezed.conf

%post
%systemd_post squeezed.service

%preun
%systemd_preun squeezed.service

%postun
%systemd_postun squeezed.service

%changelog
* Thu May 10 2018 Christian Lindig <christian.lindig@citrix.com> - 0.19.0-1
- jbuild: remove obsolete (and unused) rpclib.syntax dependency

* Wed Feb 28 2018 Christian Lindig <christian.lindig@citrix.com> - 0.18.0-1
- Use memory.ml from xcp-idl
- Add awareness of PV-in-PVH guests

* Fri Feb 02 2018 Christian Lindig <christian.lindig@citrix.com> - 0.17.0-1
- CP-26167 Port squeezed to jbuilder (#57)

* Thu Nov 02 2017 Rob Hoes <rob.hoes@citrix.com> - 0.16.0-1
- CA-263119: Use adjusted maxmem in execute_action

* Mon Jul 24 2017 Rob Hoes <rob.hoes@citrix.com> - 0.15.0-1
- Use new RPC mechanism

* Wed Jul 12 2017 Rob Hoes <rob.hoes@citrix.com> - 0.14.0-1
- CA-258652/SCTX-2565: Record initial host free memory

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 0.13.1-3
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Fri Feb 17 2017 Frederico Mazzone <frederico.mazzone@citrix.com> - 0.13.1-2
- CA-243676: Do not restart toolstack services on RPM upgrade

* Tue Jan 10 2017 Rob Hoes <rob.hoes@citrix.com> - 0.13.1-1
- git: Add metadata to the result of `git archive`

* Wed Sep 14 2016 Euan Harris <euan.harris@citrix.com> - 0.13.0-1
- Do not try to work around domains which appear to be stuck

* Mon Aug 22 2016 Rafal Mielniczuk <rafal.mielniczuk@citrix.com> - 0.12.2-2
- Package for systemd

* Fri Aug 19 2016 Euan Harris <euan.harris@citrix.com> - 0.12.2-1
- When determining dom0's total memory allocation, always ask Xen first

* Fri Jul 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.12.1-1
- New release

* Mon May 16 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.11.0-1
- Re-run chkconfig on upgrade

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.6-2
- Remove dependency on xen-missing-headers

* Fri Jun  6 2014 Jonathan Ludlam <jonathan.ludlam@citrix.com> - 0.10.6-1
- Update to 0.10.6

* Fri Apr 11 2014 Euan Harris <euan.harris@citrix.com> - 0.10.5-1
- Switch build from obuild to oasis

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.4-1
- Update to 0.10.4

* Fri Sep 20 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.3-1
- Update to allow minimal operation without xen

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.2-1
- Update to new xenstore interface in v1.2.3

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.1-1
- Add get_domain_zero_palicy call required for domain 0 ballooning

* Mon Sep  2 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.0-1
- Update to 0.10.0, with support for domain 0 ballooning

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

