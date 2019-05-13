%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kgoldrunner
Summary:	kgoldrunner
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	337c7f23bc68b8c32effcfc2c8488af8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGoldrunner is an action game where the hero runs through a maze,
climbs stairs, dig holes and dodges enemies in order to collect all
the gold nuggets and escape to the next level. Your enemies are also
after the gold.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kgoldrunner.categories
/etc/xdg/kgoldrunner.knsrc
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_desktopdir}/org.kde.kgoldrunner.desktop
%{_iconsdir}/hicolor/128x128/apps/kgoldrunner.png
%{_iconsdir}/hicolor/16x16/apps/kgoldrunner.png
%{_iconsdir}/hicolor/22x22/apps/kgoldrunner.png
%{_iconsdir}/hicolor/32x32/apps/kgoldrunner.png
%{_iconsdir}/hicolor/48x48/apps/kgoldrunner.png
%{_iconsdir}/hicolor/64x64/apps/kgoldrunner.png
%{_datadir}/kgoldrunner
%{_datadir}/kxmlgui5/kgoldrunner
%{_datadir}/metainfo/org.kde.kgoldrunner.appdata.xml
