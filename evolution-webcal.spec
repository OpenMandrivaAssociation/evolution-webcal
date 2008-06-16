%define major_version 2.4
%define libsoup_version_required 2.3.0
%define eds_version_required 1.4.0

Name:		evolution-webcal
Summary:	Webcal integration for Evolution
Version: 2.21.92
Release:	%mkrel 2
License: 	GPLv2+
Group:		Networking/Mail
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

URL: 		http://www.ximian.com/products/ximian_evolution/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires: evolution-data-server-devel >= %{eds_version_required}
BuildRequires: libsoup-devel >= %{libsoup_version_required}
Buildrequires: libgnomeui2-devel
BuildRequires: perl-XML-Parser
Requires: evolution

%description
This package registers "webcal:" URI type to use Evolution.

%prep
%setup -q

%build

%configure2_5x 

%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%{find_lang} %{name}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%define schemas evolution-webcal

%post
%post_install_gconf_schemas %{schemas}

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog 
%{_sysconfdir}/gconf/schemas/*
%{_libexecdir}/evolution-webcal


