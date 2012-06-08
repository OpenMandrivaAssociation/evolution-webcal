%define major_version 2.4
%define libsoup_version_required 2.3.0
%define eds_version_required 1.4.0

Name:		evolution-webcal
Summary:	Webcal integration for Evolution
Version: 	2.32.0
Release:	4
License: 	GPLv2
Group:		Networking/Mail
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch1:		webcal-compile.patch

URL: 		http://www.ximian.com/products/ximian_evolution/

BuildRequires:	evolution-data-server-devel >= %{eds_version_required}
BuildRequires:	libsoup-devel >= %{libsoup_version_required}
BuildRequires:	pkgconfig(libecal-1.2)
Buildrequires:	libgnomeui2-devel
BuildRequires:	intltool
BuildRequires:	automake autoconf
Requires:	evolution

%description
This package registers "webcal:" URI type to use Evolution.

%prep
%setup -q
%apply_patches
aclocal
automake -a

%build

%configure2_5x 

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%{find_lang} %{name}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%define schemas evolution-webcal

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %{schemas}
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog 
%{_sysconfdir}/gconf/schemas/*
%{_libexecdir}/evolution-webcal
