%define version 0.4.0
%define rel 1
%define release %mkrel %rel

Name:		qdigidoc
Version:	%{version}
Release:	%{release}
Summary:	Estonian digital signature application

Group:		Office
License:	LGPLv2+
URL:		http://code.google.com/p/esteid
Source0:	http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake
BuildRequires:	libdigidoc-devel
BuildRequires:	libdigidocpp-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-devel
Requires:	opensc


%description
QDigiDoc is an application for digitally signing and encrypting documents in
BDoc, DDoc, and CDoc container formats. These file formats are widespread in
Estonia where they are used for storing legally binding digital signatures.


%package	nautilus
Summary:	Nautilus extension for %{name}
Group:		User Interface/Desktops
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-python


%description	nautilus
The %{name}-nautilus package contains the %{name} extension for the
nautilus file manager.


%prep
%setup -q


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


