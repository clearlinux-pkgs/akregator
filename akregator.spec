#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akregator
Version  : 24.02.2
Release  : 85
URL      : https://download.kde.org/stable/release-service/24.02.2/src/akregator-24.02.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.2/src/akregator-24.02.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.2/src/akregator-24.02.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0 MIT
Requires: akregator-bin = %{version}-%{release}
Requires: akregator-data = %{version}-%{release}
Requires: akregator-lib = %{version}-%{release}
Requires: akregator-license = %{version}-%{release}
Requires: akregator-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kontactinterface-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : ktexteditor-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
BuildRequires : syndication-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Akregator
~~~~~~~~~~~
A KDE Feed Reader.
Join developer mailing list: <kde-pim@kde.org>

%package bin
Summary: bin components for the akregator package.
Group: Binaries
Requires: akregator-data = %{version}-%{release}
Requires: akregator-license = %{version}-%{release}

%description bin
bin components for the akregator package.


%package data
Summary: data components for the akregator package.
Group: Data

%description data
data components for the akregator package.


%package doc
Summary: doc components for the akregator package.
Group: Documentation

%description doc
doc components for the akregator package.


%package lib
Summary: lib components for the akregator package.
Group: Libraries
Requires: akregator-data = %{version}-%{release}
Requires: akregator-license = %{version}-%{release}

%description lib
lib components for the akregator package.


%package license
Summary: license components for the akregator package.
Group: Default

%description license
license components for the akregator package.


%package locales
Summary: locales components for the akregator package.
Group: Default

%description locales
locales components for the akregator package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n akregator-24.02.2
cd %{_builddir}/akregator-24.02.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713219647
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713219647
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akregator
cp %{_builddir}/akregator-%{version}/.krazy.license %{buildroot}/usr/share/package-licenses/akregator/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/akregator-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/akregator/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/akregator-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akregator/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akregator-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akregator/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akregator-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/akregator/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/akregator-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akregator/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/akregator-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akregator/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akregator-%{version}/src/storage/metakit/license.terms %{buildroot}/usr/share/package-licenses/akregator/4f42a9e708f812e067f2d87a77362c80f5f9c2bb || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang akregator
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/akregator
/V3/usr/bin/akregatorstorageexporter
/usr/bin/akregator
/usr/bin/akregatorstorageexporter

%files data
%defattr(-,root,root,-)
/usr/share/akregator/grantleetheme/5.2/combinedview.html
/usr/share/akregator/grantleetheme/5.2/defaultnormalvisitfeed.html
/usr/share/akregator/grantleetheme/5.2/defaultnormalvisitfolder.html
/usr/share/akregator/grantleetheme/5.2/normalview.html
/usr/share/applications/org.kde.akregator.desktop
/usr/share/config.kcfg/akregator.kcfg
/usr/share/dbus-1/interfaces/org.kde.akregator.part.xml
/usr/share/icons/hicolor/128x128/apps/akregator.png
/usr/share/icons/hicolor/16x16/apps/akregator.png
/usr/share/icons/hicolor/16x16/apps/akregator_empty.png
/usr/share/icons/hicolor/22x22/apps/akregator.png
/usr/share/icons/hicolor/32x32/apps/akregator.png
/usr/share/icons/hicolor/48x48/apps/akregator.png
/usr/share/icons/hicolor/64x64/apps/akregator.png
/usr/share/icons/hicolor/scalable/apps/akregator.svg
/usr/share/knotifications6/akregator.notifyrc
/usr/share/metainfo/org.kde.akregator.appdata.xml
/usr/share/qlogging-categories6/akregator.categories
/usr/share/qlogging-categories6/akregator.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/akregator/add-feed.png
/usr/share/doc/HTML/ca/akregator/add-feed2.png
/usr/share/doc/HTML/ca/akregator/add-folder.png
/usr/share/doc/HTML/ca/akregator/add-folder2.png
/usr/share/doc/HTML/ca/akregator/advanced-tab.png
/usr/share/doc/HTML/ca/akregator/appearance-tab.png
/usr/share/doc/HTML/ca/akregator/archive-tab.png
/usr/share/doc/HTML/ca/akregator/browser-tab.png
/usr/share/doc/HTML/ca/akregator/general-tab.png
/usr/share/doc/HTML/ca/akregator/index.cache.bz2
/usr/share/doc/HTML/ca/akregator/index.docbook
/usr/share/doc/HTML/ca/akregator/interceptor-tab.png
/usr/share/doc/HTML/ca/akregator/main-window.png
/usr/share/doc/HTML/ca/akregator/main-window2.png
/usr/share/doc/HTML/ca/akregator/main-window4.png
/usr/share/doc/HTML/de/akregator/index.cache.bz2
/usr/share/doc/HTML/de/akregator/index.docbook
/usr/share/doc/HTML/en/akregator/add-feed.png
/usr/share/doc/HTML/en/akregator/add-feed2.png
/usr/share/doc/HTML/en/akregator/add-folder.png
/usr/share/doc/HTML/en/akregator/add-folder2.png
/usr/share/doc/HTML/en/akregator/advanced-tab.png
/usr/share/doc/HTML/en/akregator/appearance-tab.png
/usr/share/doc/HTML/en/akregator/archive-tab.png
/usr/share/doc/HTML/en/akregator/browser-tab.png
/usr/share/doc/HTML/en/akregator/feed.png
/usr/share/doc/HTML/en/akregator/general-tab.png
/usr/share/doc/HTML/en/akregator/index.cache.bz2
/usr/share/doc/HTML/en/akregator/index.docbook
/usr/share/doc/HTML/en/akregator/interceptor-tab.png
/usr/share/doc/HTML/en/akregator/konq.png
/usr/share/doc/HTML/en/akregator/konq2.png
/usr/share/doc/HTML/en/akregator/main-window.png
/usr/share/doc/HTML/en/akregator/main-window2.png
/usr/share/doc/HTML/en/akregator/main-window3.png
/usr/share/doc/HTML/en/akregator/main-window4.png
/usr/share/doc/HTML/en/akregator/quick-filter.png
/usr/share/doc/HTML/en/akregator/rss.png
/usr/share/doc/HTML/en/akregator/share-services-tab.png
/usr/share/doc/HTML/es/akregator/index.cache.bz2
/usr/share/doc/HTML/es/akregator/index.docbook
/usr/share/doc/HTML/et/akregator/index.cache.bz2
/usr/share/doc/HTML/et/akregator/index.docbook
/usr/share/doc/HTML/fr/akregator/index.cache.bz2
/usr/share/doc/HTML/fr/akregator/index.docbook
/usr/share/doc/HTML/it/akregator/index.cache.bz2
/usr/share/doc/HTML/it/akregator/index.docbook
/usr/share/doc/HTML/nl/akregator/index.cache.bz2
/usr/share/doc/HTML/nl/akregator/index.docbook
/usr/share/doc/HTML/pt/akregator/index.cache.bz2
/usr/share/doc/HTML/pt/akregator/index.docbook
/usr/share/doc/HTML/pt_BR/akregator/index.cache.bz2
/usr/share/doc/HTML/pt_BR/akregator/index.docbook
/usr/share/doc/HTML/ru/akregator/index.cache.bz2
/usr/share/doc/HTML/ru/akregator/index.docbook
/usr/share/doc/HTML/sv/akregator/index.cache.bz2
/usr/share/doc/HTML/sv/akregator/index.docbook
/usr/share/doc/HTML/uk/akregator/add-feed.png
/usr/share/doc/HTML/uk/akregator/add-feed2.png
/usr/share/doc/HTML/uk/akregator/add-folder.png
/usr/share/doc/HTML/uk/akregator/add-folder2.png
/usr/share/doc/HTML/uk/akregator/advanced-tab.png
/usr/share/doc/HTML/uk/akregator/appearance-tab.png
/usr/share/doc/HTML/uk/akregator/archive-tab.png
/usr/share/doc/HTML/uk/akregator/browser-tab.png
/usr/share/doc/HTML/uk/akregator/general-tab.png
/usr/share/doc/HTML/uk/akregator/index.cache.bz2
/usr/share/doc/HTML/uk/akregator/index.docbook
/usr/share/doc/HTML/uk/akregator/konq.png
/usr/share/doc/HTML/uk/akregator/main-window.png
/usr/share/doc/HTML/uk/akregator/main-window2.png
/usr/share/doc/HTML/uk/akregator/main-window3.png
/usr/share/doc/HTML/uk/akregator/main-window4.png
/usr/share/doc/HTML/uk/akregator/quick-filter.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libakregatorinterfaces.so.6.0.2
/V3/usr/lib64/libakregatorprivate.so.6.0.2
/V3/usr/lib64/qt6/plugins/akregatorpart.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_advanced.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_appearance.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_archive.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_browser.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_general.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_plugins.so
/V3/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_security.so
/V3/usr/lib64/qt6/plugins/pim6/kontact/kontact_akregatorplugin.so
/usr/lib64/libakregatorinterfaces.so.6
/usr/lib64/libakregatorinterfaces.so.6.0.2
/usr/lib64/libakregatorprivate.so.6
/usr/lib64/libakregatorprivate.so.6.0.2
/usr/lib64/qt6/plugins/akregatorpart.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_advanced.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_appearance.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_archive.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_browser.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_general.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_plugins.so
/usr/lib64/qt6/plugins/pim6/kcms/akregator/akregator_config_security.so
/usr/lib64/qt6/plugins/pim6/kontact/kontact_akregatorplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akregator/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akregator/4f42a9e708f812e067f2d87a77362c80f5f9c2bb
/usr/share/package-licenses/akregator/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/akregator/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/akregator/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akregator/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akregator/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akregator/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akregator.lang
%defattr(-,root,root,-)

