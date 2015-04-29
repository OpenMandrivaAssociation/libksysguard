%define devname %mklibname KF5Libksysguard -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: libksysguard
Version: 5.3.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 system monitoring framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5KDE4Support)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5I18n)

%define ksgrdname %mklibname ksgrd 7
%define ksignalplottername %mklibname ksignalplotter 7
%define lsofuiname %mklibname lsofui 7
%define processcorename %mklibname processcore 7
%define processuiname %mklibname processui 7
Requires: %{ksgrdname} = %{EVRD}
Requires: %{ksignalplottername} = %{EVRD}
Requires: %{lsofuiname} = %{EVRD}
Requires: %{processcorename} = %{EVRD}
Requires: %{processuiname} = %{EVRD}

%libpackage ksgrd 7
%libpackage ksignalplotter 7
%libpackage lsofui 7
%libpackage processcore 7
%libpackage processui 7

%description
KDE Frameworks 5 system monitoring framework.


%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 system monitoring library
Group: Development/KDE and Qt
Requires: %{ksgrdname} = %{EVRD}
Requires: %{ksignalplottername} = %{EVRD}
Requires: %{lsofuiname} = %{EVRD}
Requires: %{processcorename} = %{EVRD}
Requires: %{processuiname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 system monitoring library.

%prep
%setup -qn %{name}-%{plasmaver}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

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
