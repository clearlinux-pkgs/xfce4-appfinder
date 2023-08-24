#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : xfce4-appfinder
Version  : 4.18.1
Release  : 27
URL      : https://archive.xfce.org/src/xfce/xfce4-appfinder/4.18/xfce4-appfinder-4.18.1.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/xfce4-appfinder/4.18/xfce4-appfinder-4.18.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-appfinder-bin = %{version}-%{release}
Requires: xfce4-appfinder-data = %{version}-%{release}
Requires: xfce4-appfinder-license = %{version}-%{release}
Requires: xfce4-appfinder-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : intltool
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/xfce4-appfinder/COPYING)

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
%setup -q -n xfce4-appfinder-4.18.1
cd %{_builddir}/xfce4-appfinder-4.18.1
pushd ..
cp -a xfce4-appfinder-4.18.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692909355
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1692909355
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-appfinder
cp %{_builddir}/xfce4-appfinder-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xfce4-appfinder/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang xfce4-appfinder
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xfce4-appfinder
/usr/bin/xfce4-appfinder
/usr/bin/xfrun4

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-appfinder.desktop
/usr/share/applications/xfce4-run.desktop
/usr/share/icons/hicolor/128x128/apps/org.xfce.appfinder.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.appfinder.png
/usr/share/icons/hicolor/24x24/apps/org.xfce.appfinder.png
/usr/share/icons/hicolor/32x32/apps/org.xfce.appfinder.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.appfinder.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.appfinder.svg
/usr/share/metainfo/org.xfce.xfce4-appfinder.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-appfinder/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f xfce4-appfinder.lang
%defattr(-,root,root,-)

