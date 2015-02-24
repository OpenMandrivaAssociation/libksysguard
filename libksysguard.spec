%define major 5
%define devname %mklibname KF5Libksysguard -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: libksysguard
Version: 5.2.1
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 system monitoring framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5)
BuildRequires: cmake(ZLIB)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(KF5KDE4Support)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5Positioning)
BuildRequires: cmake(Qt5Sensors)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Script)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5I18n)
BuildRequires: ninja
%define ksgrdname %mklibname ksgrd 5
%define ksignalplottername %mklibname ksignalplotter 5
%define lsofuiname %mklibname lsofui 5
%define processcorename %mklibname processcore 5
%define processuiname %mklibname processui 5
Requires: %{ksgrdname} = %{EVRD}
Requires: %{ksignalplottername} = %{EVRD}
Requires: %{lsofuiname} = %{EVRD}
Requires: %{processcorename} = %{EVRD}
Requires: %{processuiname} = %{EVRD}

%libpackage ksgrd 5
%libpackage ksignalplotter 5
%libpackage lsofui 5
%libpackage processcore 5
%libpackage processui 5

%description
KDE Frameworks 5 system monitoring framework


%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 system monitoring library
Group: Development/KDE and Qt
Requires: %{ksgrdname} = %{EVRD}
Requires: %{ksignalplottername} = %{EVRD}
Requires: %{lsofuiname} = %{EVRD}
Requires: %{processcorename} = %{EVRD}
Requires: %{processuiname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 system monitoring library

%prep
%setup -qn %{name}-%{plasmaver}
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install
%find_lang ksgrd
%find_lang ksysguardlsofwidgets
%find_lang processcore
%find_lang processui

%files -f ksgrd.lang,ksysguardlsofwidgets.lang,processcore.lang,processui.lang
%{_datadir}/ksysguard
%{_sysconfdir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_libdir}/libexec/kauth/ksysguardprocesslist_helper
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
