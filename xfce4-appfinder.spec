#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-appfinder
Version  : 4.13.2
Release  : 11
URL      : http://archive.xfce.org/src/xfce/xfce4-appfinder/4.13/xfce4-appfinder-4.13.2.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/xfce4-appfinder/4.13/xfce4-appfinder-4.13.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-appfinder-bin = %{version}-%{release}
Requires: xfce4-appfinder-data = %{version}-%{release}
Requires: xfce4-appfinder-license = %{version}-%{release}
Requires: xfce4-appfinder-locales = %{version}-%{release}
BuildRequires : intltool
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)

%description


%package bin
Summary: bin components for the xfce4-appfinder package.
Group: Binaries
Requires: xfce4-appfinder-data = %{version}-%{release}
Requires: xfce4-appfinder-license = %{version}-%{release}

%description bin
bin components for the xfce4-appfinder package.


%package data
Summary: data components for the xfce4-appfinder package.
Group: Data

%description data
data components for the xfce4-appfinder package.


%package license
Summary: license components for the xfce4-appfinder package.
Group: Default

%description license
license components for the xfce4-appfinder package.


%package locales
Summary: locales components for the xfce4-appfinder package.
Group: Default

%description locales
locales components for the xfce4-appfinder package.


%prep
%setup -q -n xfce4-appfinder-4.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545532488
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1545532488
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-appfinder
cp COPYING %{buildroot}/usr/share/package-licenses/xfce4-appfinder/COPYING
%make_install
%find_lang xfce4-appfinder

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-appfinder
/usr/bin/xfrun4

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-appfinder.desktop
/usr/share/applications/xfce4-run.desktop
/usr/share/metainfo/org.xfce.xfce4-appfinder.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-appfinder/COPYING

%files locales -f xfce4-appfinder.lang
%defattr(-,root,root,-)

