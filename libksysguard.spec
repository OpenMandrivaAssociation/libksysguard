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

Requires: %{libksgrdname5} = %{EVRD}
Requires: %{libksignalplottername5} = %{EVRD}
Requires: %{liblsofuiname5} = %{EVRD}
Requires: %{libprocesscorename5} = %{EVRD}
Requires: %{libprocessuiname5} = %{EVRD}

%description
KDE Frameworks 5 system monitoring framework.

%files -f ksgrd.lang,ksysguardlsofwidgets.lang,processcore.lang,processui.lang
%{_datadir}/ksysguard/scripts
%{_libexecdir}/kauth/ksysguardprocesslist_helper
%{_sysconfdir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

#----------------------------------------------------------------------------

%define ksgrd5_major 7
%define libksgrd5 %mklibname ksgrd5_ %{ksgrd5_major}

%package -n %{libksgrd5}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name}

%description -n %{libksgrd5}
Plasma 5 KDE System Guard shared library.

%files -n %{libksgrd5}
%{_libdir}/libksgrd5.so.%{ksgrd5_major}
%{_libdir}/libksgrd5.so.%{version}

#----------------------------------------------------------------------------

%define ksignalplotter5_major 7
%define libksignalplotter5 %mklibname ksignalplotter5_ %{ksignalplotter5_major}

%package -n %{libksignalplotter5}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name}

%description -n %{libksignalplotter5}
Plasma 5 KDE System Guard shared library.

%files -n %{libksignalplotter5}
%{_libdir}/libksignalplotter5.so.%{ksignalplotter5_major}
%{_libdir}/libksignalplotter5.so.%{version}

#----------------------------------------------------------------------------

%define lsofui5_major 7
%define liblsofui5 %mklibname lsofui5_ %{lsofui5_major}

%package -n %{liblsofui5}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name}

%description -n %{liblsofui5}
Plasma 5 KDE System Guard shared library.

%files -n %{liblsofui5}
%{_libdir}/liblsofui5.so.%{lsofui5_major}
%{_libdir}/liblsofui5.so.%{version}

#----------------------------------------------------------------------------

%define processcore5_major 7
%define libprocesscore5 %mklibname processcore5_ %{processcore5_major}

%package -n %{libprocesscore5}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name}

%description -n %{libprocesscore5}
Plasma 5 KDE System Guard shared library.

%files -n %{libprocesscore5}
%{_libdir}/libprocesscore5.so.%{processcore5_major}
%{_libdir}/libprocesscore5.so.%{version}

#----------------------------------------------------------------------------

%define processui5_major 7
%define libprocessui5 %mklibname processui5_ %{processui5_major}

%package -n %{libprocessui5}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name}

%description -n %{libprocessui5}
Plasma 5 KDE System Guard shared library.

%files -n %{libprocessui5}
%{_libdir}/libprocessui5.so.%{processui5_major}
%{_libdir}/libprocessui5.so.%{version}

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 system monitoring library
Group: Development/KDE and Qt
Requires: %{libksgrdname5} = %{EVRD}
Requires: %{libksignalplottername5} = %{EVRD}
Requires: %{liblsofuiname5} = %{EVRD}
Requires: %{libprocesscorename5} = %{EVRD}
Requires: %{libprocessuiname5} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 system monitoring library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*

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



