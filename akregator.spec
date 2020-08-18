#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akregator
Version  : 20.08.0
Release  : 25
URL      : https://download.kde.org/stable/release-service/20.08.0/src/akregator-20.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.0/src/akregator-20.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.0/src/akregator-20.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1 MIT
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
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcmutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kcrash-dev
BuildRequires : kdoctools-dev
BuildRequires : kmime-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kontactinterface-dev
BuildRequires : kparts-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktexteditor-dev
BuildRequires : kxmlgui-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev
BuildRequires : syndication-dev

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


%package dev
Summary: dev components for the akregator package.
Group: Development
Requires: akregator-lib = %{version}-%{release}
Requires: akregator-bin = %{version}-%{release}
Requires: akregator-data = %{version}-%{release}
Provides: akregator-devel = %{version}-%{release}
Requires: akregator = %{version}-%{release}

%description dev
dev components for the akregator package.


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
%setup -q -n akregator-20.08.0
cd %{_builddir}/akregator-20.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597768776
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1597768776
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akregator
cp %{_builddir}/akregator-20.08.0/COPYING %{buildroot}/usr/share/package-licenses/akregator/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/akregator-20.08.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/akregator/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/akregator-20.08.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/akregator/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/akregator-20.08.0/plugins/mk4storage/metakit/license.terms %{buildroot}/usr/share/package-licenses/akregator/4f42a9e708f812e067f2d87a77362c80f5f9c2bb
pushd clr-build
%make_install
popd
%find_lang akregator

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/kconf_update/akregator-15.08-kickoff.sh
/usr/share/kconf_update/akregator.upd
/usr/share/knotifications5/akregator.notifyrc
/usr/share/kontact/ksettingsdialog/akregator.setdlg
/usr/share/kservices5/akregator_config_advanced.desktop
/usr/share/kservices5/akregator_config_appearance.desktop
/usr/share/kservices5/akregator_config_archive.desktop
/usr/share/kservices5/akregator_config_browser.desktop
/usr/share/kservices5/akregator_config_general.desktop
/usr/share/kservices5/akregator_config_plugins.desktop
/usr/share/kservices5/akregator_mk4storage_plugin.desktop
/usr/share/kservices5/feed.protocol
/usr/share/kservices5/kontact/akregatorplugin.desktop
/usr/share/kservicetypes5/akregator_plugin.desktop
/usr/share/metainfo/org.kde.akregator.appdata.xml
/usr/share/qlogging-categories5/akregator.categories
/usr/share/qlogging-categories5/akregator.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/lib64/libakregatorinterfaces.so

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
/usr/lib64/libakregatorinterfaces.so.5
/usr/lib64/libakregatorinterfaces.so.5.15.0
/usr/lib64/libakregatorprivate.so.5
/usr/lib64/libakregatorprivate.so.5.15.0
/usr/lib64/qt5/plugins/akregator_config_advanced.so
/usr/lib64/qt5/plugins/akregator_config_appearance.so
/usr/lib64/qt5/plugins/akregator_config_archive.so
/usr/lib64/qt5/plugins/akregator_config_browser.so
/usr/lib64/qt5/plugins/akregator_config_general.so
/usr/lib64/qt5/plugins/akregator_config_plugins.so
/usr/lib64/qt5/plugins/akregator_mk4storage_plugin.so
/usr/lib64/qt5/plugins/akregatorpart.so
/usr/lib64/qt5/plugins/kontact5/kontact_akregatorplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akregator/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/akregator/4f42a9e708f812e067f2d87a77362c80f5f9c2bb
/usr/share/package-licenses/akregator/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/akregator/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f akregator.lang
%defattr(-,root,root,-)

