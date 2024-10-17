Name:		evolution-webcal
Summary:	Webcal integration for Evolution
Version:	2.32.0
Release:	5
License:	GPLv2
Group:		Networking/Mail
URL:		https://www.ximian.com/products/ximian_evolution/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
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
%autopatch -p1
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



%changelog
* Sat Jun 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.32.0-4
+ Revision: 805957
- rebuild for libecal
- cleaned up spec
- added patch for depricated g_thread

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - Make it compile

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 2.32.0-3
+ Revision: 677668
- rebuild to add gconftool as req

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.0-2
+ Revision: 664157
- mass rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581729
- update to new version 2.32.0

* Tue Aug 10 2010 Götz Waschk <waschk@mandriva.org> 2.31.2-3mdv2011.0
+ Revision: 568297
- rebuild for new evolution

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.2-2mdv2011.0
+ Revision: 563394
- new version

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-2mdv2011.0
+ Revision: 548450
- rebuild with latest eds

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.1
+ Revision: 529949
- update to new version 2.28.1

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 522576
- rebuilt for 2010.1

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447184
- update to new version 2.28.0

* Thu Aug 13 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 415959
- update to new version 2.27.90

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356022
- update to new version 2.26.0

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341223
- update to new version 2.25.91

* Sat Feb 14 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 340215
- update to new version 2.25.90

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287364
- new version

* Sun Aug 31 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 277782
- new version

* Fri Jul 04 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-4mdv2009.0
+ Revision: 231813
- fix license

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 2.21.92-3mdv2009.0
+ Revision: 227421
- rebuild for fixed %%update_icon_cache/%%clean_icon_cache/%%post_install_gconf_schemas
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.21.92-2mdv2009.0
+ Revision: 220731
- rebuild

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174582
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.13.90-2mdv2008.1
+ Revision: 166155
- libsoup rebuild

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 2.13.90-1mdv2008.1
+ Revision: 160629
- new version
- update  buildrequires

* Thu Jan 24 2008 Funda Wang <fwang@mandriva.org> 2.12.0-4mdv2008.1
+ Revision: 157295
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.12.0-3mdv2008.1
+ Revision: 149705
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Sep 17 2007 Olivier Blin <blino@mandriva.org> 2.12.0-2mdv2008.0
+ Revision: 89121
- rebuild because of package loss

* Sun Sep 16 2007 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdv2008.0
+ Revision: 88437
- new version

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.11.91-1mdv2008.0
+ Revision: 72474
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.11.90-1mdv2008.0
+ Revision: 63196
- new version
- build without libsoup


* Tue Mar 13 2007 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2007.1
+ Revision: 143214
- new version

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 2.9.92-1mdv2007.1
+ Revision: 126792
- new version

* Tue Feb 13 2007 Götz Waschk <waschk@mandriva.org> 2.9.91-1mdv2007.1
+ Revision: 120271
- new version

* Tue Jan 09 2007 Götz Waschk <waschk@mandriva.org> 2.9.5-1mdv2007.0
+ Revision: 106548
- new version

* Thu Nov 30 2006 Götz Waschk <waschk@mandriva.org> 2.8.0-2mdv2007.1
+ Revision: 89285
- Import evolution-webcal

* Thu Nov 30 2006 Götz Waschk <waschk@mandriva.org> 2.8.0-2mdv2007.1
- depend on evolution

* Wed Sep 06 2006 Frederic Crozat <fcrozat@mandriva.com> 2.8.0-1mdv2007.0
- Release 2.8.0

* Fri Jun 23 2006 Frederic Crozat <fcrozat@mandriva.com> 2.7.1-1mdv2007.0
- Release 2.7.1
- use new macros

* Thu Apr 27 2006 Frederic Crozat <fcrozat@mandriva.com> 2.6.0-1mdk
- Release 2.6.0

* Tue Apr 25 2006 Frederic Crozat <fcrozat@mandriva.com> 2.5.90-1mdk
- Release 2.5.90

* Wed Jan 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.4.1-2mdk
- Rebuild
- use mkrel

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.4.1-1mdk
- Release 2.4.1

* Tue Jul 05 2005 Frederic Crozat <fcrozat@mandriva.com> 2.2.1-1mdk 
- Release 2.2.1

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.1-1mdk
- New release 2.0.1

* Thu Sep 30 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.0-2mdk
- Fix buildrequires

* Wed Sep 15 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.0-1mdk
- Release 2.0.0

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.9-2mdk
- Rebuild with latest libsoup

* Fri Aug 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.9-1mdk
- Release 1.0.9

* Wed Aug 04 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.8-1mdk
- Release 1.0.8

* Wed Jul 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.7-1mdk
- New release 1.0.7

* Tue Jul 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.6-1mdk
- New release 1.0.6

* Wed Jun 09 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.5-1mdk
- Release 1.0.5

* Wed May 05 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.4-1mdk
- New release 1.0.4
- Remove patch0 (merged upstream)

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.3-1mdk
- Initial Mandrakelinux package
- Patch0: fix libexec directory

