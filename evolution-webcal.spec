Name:		evolution-webcal
Summary:	Webcal integration for Evolution
Version: 	2.32.0
Release:	4
License: 	GPLv2
Group:		Networking/Mail
URL: 		http://www.ximian.com/products/ximian_evolution/
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		evolution-webcal-2.32.0_g_thread.patch
Patch1:		webcal-compile.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libecal-1.2)
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
%makeinstall_std

%find_lang %{name}

%define schemas evolution-webcal

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog 
%{_sysconfdir}/gconf/schemas/*
%{_libexecdir}/evolution-webcal

