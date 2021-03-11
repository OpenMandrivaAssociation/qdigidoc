Name:		qdigidoc
Version:	4.2.8
Release:	1
Summary:	Estonian digital signature application

Group:		Office
License:	LGPLv2+
URL:		https://github.com/open-eid/DigiDoc4-Client
Source0:	https://github.com/open-eid/DigiDoc4-Client/releases/download/v%{version}/qdigidoc4-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  qmake5
BuildRequires:	libdigidocpp-devel
BuildRequires:	openldap-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(libpcsclite) >= 1.7

Requires:       hicolor-icon-theme
Requires:	opensc


%description
QDigiDoc is an application for digitally signing and encrypting documents in
BDoc, DDoc, and CDoc container formats. These file formats are widespread in
Estonia where they are used for storing legally binding digital signatures.


%package	nautilus
Summary:	Nautilus extension for %{name}
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-python


%description	nautilus
The %{name}-nautilus package contains the %{name} extension for the
nautilus file manager.


%prep
%setup -q -n qdigidoc4


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ../..
popd

%make -C %{_target_platform}/build


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C %{_target_platform}/build

%find_lang nautilus-qdigidoc


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/kde4/services/*.desktop

%files nautilus -f nautilus-qdigidoc.lang
%defattr(-,root,root,-)
%{_libdir}/nautilus/extensions-2.0/python/*




%changelog
* Sun Nov 07 2010 Sander Lepik <sander85@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 594859
- fix group
- import qdigidoc


* Tue Oct 26 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.4.0-1mdv2010.1
- new version 0.4.0

* Thu Sep 23 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-14mdv2010.1
- Rebuilt with new openssl

* Wed Sep 08 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-13mdv2010.1
- First build on new bs
- Spec file cleaned up

* Wed Apr 14 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-12mdv2010.1
- New build from Google Code repository

* Thu Feb 11 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-11mdv2010.1
- fix segmentation fault caused by old libp11

* Fri Jan 29 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-10mdv2010.1
- Changeset 2451: client maybe fixes libp11 error codes (Ticket: #880)
- Changeset 2456: use common_en strings
- Changeset 2497: client fix url parsing and dont leak (Ticket: #1252)
- Changeset 2498: client cleanup and fix p12 loading (Ticket #1253)
- Changeset 2499: client seems to work without this flag and fixes openssl 1.0 error (Ticket #982)
- Changeset 2517: Fixed a few compiler warnings
- Changeset 2518: Fixed a signed/unsigned mismatch warning

* Mon Jan 18 2010 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-9mdv2010.1
- Changeset 2371: crypto handle pin errors (Ticket #1167)
- Changeset 2374: client validate proxy settings before signing (Ticket #1136)
- Changeset 2376: client ask pin again when its wrong (Ticket #883)
- Changeset 2377: common rename to SslConnectPrivate?  class
- Changeset 2387: common cleanup and dont cache invalid pin (Ticket #883)
- Changeset 2399: client try to keep same card selected (Ticket #1184)
- Changeset 2400: client validate again on wrong pin (Ticket #883)
- Changeset 2401: client use only valid pkcs12 certificate (Ticket #1220)
- Changeset 2407: crypto fix build
- Changeset 2411: clear cards list earlier (Ticket #1228)
- Changeset 2421: client try to fix card switchin bug, requires libp11 0.2.7 (Ticket #1133, #988)
- Changeset 2422: common cleanup api
- Changeset 2429: use X509_NAME_print_ex to workaround QSslCertificate character decoding issues
- Changeset 2435: crypto update strings (Ticket: #792)
- Changeset 2439: crypto translations update
- Changeset 2440: cleanup API
- Changeset 2448: client use new libdigidocpp pkcs12 user settings
- Changeset 2450: client store proxy on digidoc config

* Wed Dec 30 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-8mdv2010.1
- Changeset 2344: client fix Message Dialog window titles (Ticket #1110)
- Changeset 2352: client fix roles
- Changeset 2360: client escape html metacharacters (Ticket #1152)
- Changeset 2363: crypto avoid libdigidoc pkcs#11 api and implement pinpad support (Ticket #873)
- Changeset 2366: crypto fix return codes (Ticket #873)

* Thu Dec 17 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-7mdv2010.1
- Changeset 2279, 2283, 2284, 2292, 2342, 2343: translation update
- Changeset 2280: client fix double extension (Ticket #645)
- Changeset 2281: client add more error messages (Ticket #1056)
- Changeset 2288: set on first start OS language (Ticket #1032)
- Changeset 2293: client fix expire dialog (Ticket #1060)
- Changeset 2312: client disable IK check
- Changeset 2336: client cleanup timer code
- Changeset 2337: client forgot form last commit
- Changeset 2338: client change mobile-id sms header (Ticket #937)
- Changeset 2339: client parse content on QNetoworkReply::UnknownContentError?
- Changeset 2340: client translate
- Changeset 2341: client cleanup

* Mon Dec 07 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-6mdv2010.1
- Changeset 2229, 2231: client show warning when user adds file to signed document (Ticket #1024)
- Changeset 2232, 2237, 2238: translation update
- Changeset 2240: client disable IK validator for testing

* Tue Dec 01 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-5mdv2010.1
- Changeset 2209: common use constData, dont delete dialog on event loop (Ticket #992)
- Changeset 2218: common qt 4.6 fixes
- Changeset 2219: common fix build qt < 4.6

* Thu Nov 26 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-4mdv2010.1
- Changeset 2172: accept key events when widget has focus (Ticket #999)
- Changeset 2191: client dont delete dialog on event loop (Ticket #992)
- Changeset 2192: accept only selected rows (Ticket #999)

* Tue Nov 24 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-3mdv2010.1
- Changeset 2171: translation update

* Mon Nov 23 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-2mdv2010.1
- Fix for language selection

* Fri Nov 20 2009 Sander Lepik <sander.lepik@eesti.ee> - 0.3.0-1mdv2010.1
- Initial release for Mandriva

* Mon Nov 09 2009 Kalev Lember <kalev@smartlink.ee> - 0.3.0-0.7.svn2095
- rebuilt with new libdigidocpp

* Sun Nov 08 2009 Kalev Lember <kalev@smartlink.ee> - 0.3.0-0.6.svn2095
- rebuilt with new libdigidocpp

* Sun Nov 08 2009 Kalev Lember <kalev@smartlink.ee> - 0.3.0-0.5.svn2095
- rebuilt with new libdigidocpp

* Fri Nov 06 2009 Kalev Lember <kalev@smartlink.ee> - 0.3.0-0.4.svn2095
- rebuilt with new libdigidocpp

* Thu Nov 05 2009 Kalev Lember <kalev@smartlink.ee> - 0.3.0-0.3.svn2095
- rebuilt with new libdigidocpp

* Sun Jun 14 2009 Kalev Lember <kalev@smartlink.ee> - 0.3.0-0.2.svn2095
- Initial RPM release.

