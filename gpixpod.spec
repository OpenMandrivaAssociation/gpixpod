%define name	gpixpod
%define version	0.6.2
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Photo manager for capable iPods
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/%name/%name-%{version}.tar.bz2
URL:		http://gpixpod.sourceforge.net/
License:	GPL
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	python-devel
BuildRequires:	gtk+2-devel
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT installed-docs
python setup.py install --root=$RPM_BUILD_ROOT

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GPixPod" longtitle="Photo Manager for the iPod" section="Multimedia/Graphics" xdg="true"
EOF

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

%find_lang %name

mv %buildroot%_datadir/doc/%name installed-docs
mv %buildroot%py_platsitedir/gpixpod* %buildroot%_prefix/lib/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc installed-docs/*
%{_bindir}/%name
%{_datadir}/%name
%_datadir/applications/*.desktop
%_prefix/lib/%name
%py_platsitedir/*
%_mandir/man1/%name.1*
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

