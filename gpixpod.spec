%define name	gpixpod
%define version	0.6.2
%define release %mkrel 8

Name: 	 	%{name}
Summary: 	Photo manager for capable iPods
Version: 	%{version}
Release: 	%{release}

Source0:		http://prdownloads.sourceforge.net/%name/%name-%{version}.tar.bz2
Patch0:		gpixpod-0.6.2-close-about.patch
URL:		http://gpixpod.sourceforge.net/
License:	GPLv2+
Group:		Graphics
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	desktop-file-utils
Requires:	pygtk2.0-libglade pygtk2.0
Requires:	python-gobject
Requires:	dbus-python
Requires:	gnome-python gnome-python-gnomevfs

%description
GPixPod is an application for uploading and organizing photos and photo albums
on recent Apple iPod models.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 GPixPod_icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 GPixPod_icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 GPixPod_icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

mv %buildroot%_datadir/doc/%name installed-docs
mv %buildroot%py_platsitedir/gpixpod* %buildroot%_prefix/lib/%name/

perl -pi -e "s/python2.4/python/" %buildroot%_bindir/%name

%files
%doc installed-docs/*
%{_bindir}/%name
%{_datadir}/%name
%_datadir/applications/*.desktop
%_prefix/lib/%name
%py_platsitedir/*
%_mandir/man1/%name.1*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png




%changelog
* Fri Nov 04 2011 Götz Waschk <waschk@mandriva.org> 0.6.2-8mdv2012.0
+ Revision: 717576
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.6.2-7mdv2011.0
+ Revision: 437807
- rebuild

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.6.2-6mdv2009.1
+ Revision: 320593
- rebuild for new python

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Sep 03 2008 Götz Waschk <waschk@mandriva.org> 0.6.2-5mdv2009.0
+ Revision: 279957
- fix closing of the about dialog
- update license

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.6.2-4mdv2009.0
+ Revision: 218421
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 18 2007 Götz Waschk <waschk@mandriva.org> 0.6.2-4mdv2008.0
+ Revision: 53312
- use the right python


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.6.2-3mdv2007.0
+ Revision: 88347
- rebuild

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 0.6.2-2mdv2007.1
+ Revision: 63799
- rebuild
- Import gpixpod

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2007.1
- New version 0.6.2

* Tue Sep 12 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-3mdv2007.0
- fix file locations again

* Tue Sep 12 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdv2007.0
- fix build and installation
- add missing binaries

* Mon Sep 11 2006 Jerome Soyer <saispo@mandriva.org> 0.6.0-1mdv2007.0
- New release 0.6.0

* Sun Aug 27 2006 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2007.0
- New release 0.5.2

* Tue Aug 22 2006 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2007.0
- New release 0.5.1

* Thu Jul 06 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2007.0
- source URL
- new version

* Wed Jun 21 2006 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdv2007.0
- xdg menu
- New release 0.4.4

* Wed Jun 14 2006 Götz Waschk <waschk@mandriva.org> 0.4.3-1mdv2007.0
- New release 0.4.3

* Wed Apr 26 2006 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdk
- New release 0.4.2

* Thu Mar 30 2006 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdk
- New release 0.4.1

* Wed Mar 22 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdk
- New release 0.4.0

* Thu Mar 09 2006 Austin Acton <austin@mandriva.org> 0.3.4-1mdk
- New release 0.3.4

* Tue Feb 28 2006 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdk
- New release 0.3.3

* Fri Feb 24 2006 Austin Acton <austin@mandriva.org> 0.3.2-1mdk
- New release 0.3.2
- drop patch

* Thu Feb 16 2006 Austin Acton <austin@mandriva.org> 0.3-1mdk
- initial package

