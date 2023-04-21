#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kgoldrunner
Summary:	kgoldrunner
Name:		ka5-%{kaname}
Version:	23.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a4449f6581d6a77f00dc8c6a71cfe672
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

%description -l pl.UTF-8
KGoldrunner jest grą akcji, gdzie bohater biegnie przez labirynt,
wchodzi po schodach, kopie doły i ucieka wrogom wcelu zebrania grudek
złota i przejścia do następnego poziomu. Twoi wrogowie również
szukają złota.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_desktopdir}/org.kde.kgoldrunner.desktop
%{_iconsdir}/hicolor/128x128/apps/kgoldrunner.png
%{_iconsdir}/hicolor/16x16/apps/kgoldrunner.png
%{_iconsdir}/hicolor/22x22/apps/kgoldrunner.png
%{_iconsdir}/hicolor/32x32/apps/kgoldrunner.png
%{_iconsdir}/hicolor/48x48/apps/kgoldrunner.png
%{_iconsdir}/hicolor/64x64/apps/kgoldrunner.png
%{_datadir}/kgoldrunner
%{_datadir}/metainfo/org.kde.kgoldrunner.appdata.xml
%{_datadir}/qlogging-categories5/kgoldrunner.categories
%{_datadir}/knsrcfiles/kgoldrunner.knsrc
