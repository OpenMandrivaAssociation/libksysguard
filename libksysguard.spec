%define devname %mklibname KF5Libksysguard -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define ksgrd_major 7
%define libksgrd %mklibname ksgrd %{ksgrd_major}
%define ksignalplotter_major 7
%define libksignalplotter %mklibname ksignalplotter %{ksignalplotter_major}
%define lsofui_major 7
%define liblsofui %mklibname lsofui %{lsofui_major}
%define processcore_major 7
%define libprocesscore %mklibname processcore %{processcore_major}
%define processui_major 7
%define libprocessui %mklibname processui %{processui_major}

Name: libksysguard
Version: 5.15.5
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 system monitoring framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
#Patch0: libksysguard-5.5.5-fix-isnan-isinf.patch
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)
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
BuildRequires: cmake(KF5GlobalAccel)

Requires: %{libksgrd} = %{EVRD}
Requires: %{libksignalplotter} = %{EVRD}
Requires: %{liblsofui} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libprocessui} = %{EVRD}

%description
KDE Frameworks 5 system monitoring framework.

%files -f ksgrd.lang -f ksysguardlsofwidgets.lang -f processcore.lang -f processui.lang
%{_sysconfdir}/xdg/libksysguard.categories
%{_datadir}/ksysguard/scripts
%{_libdir}/libexec/kauth/ksysguardprocesslist_helper
%{_sysconfdir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

#----------------------------------------------------------------------------

%package -n %{libksgrd}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libksgrd}
Plasma 5 KDE System Guard shared library.

%files -n %{libksgrd}
%{_libdir}/libksgrd.so.%{ksgrd_major}
%{_libdir}/libksgrd.so.%{version}

#----------------------------------------------------------------------------

%package -n %{libksignalplotter}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libksignalplotter}
Plasma 5 KDE System Guard shared library.

%files -n %{libksignalplotter}
%{_libdir}/libksignalplotter.so.%{ksignalplotter_major}
%{_libdir}/libksignalplotter.so.%{version}

#----------------------------------------------------------------------------

%package -n %{liblsofui}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{liblsofui}
Plasma 5 KDE System Guard shared library.

%files -n %{liblsofui}
%{_libdir}/liblsofui.so.%{lsofui_major}
%{_libdir}/liblsofui.so.%{version}

#----------------------------------------------------------------------------

%package -n %{libprocesscore}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocesscore}
Plasma 5 KDE System Guard shared library.

%files -n %{libprocesscore}
%{_libdir}/libprocesscore.so.%{processcore_major}
%{_libdir}/libprocesscore.so.%{version}

#----------------------------------------------------------------------------

%package -n %{libprocessui}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocessui}
Plasma 5 KDE System Guard shared library.

%files -n %{libprocessui}
%{_libdir}/libprocessui.so.%{processui_major}
%{_libdir}/libprocessui.so.%{version}

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 system monitoring library
Group: Development/KDE and Qt
Requires: %{libksgrd} = %{EVRD}
Requires: %{libksignalplotter} = %{EVRD}
Requires: %{liblsofui} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libprocessui} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 system monitoring library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang ksgrd || touch ksgrd.lang
%find_lang ksysguardlsofwidgets || touch ksysguardlsofwidgets.lang
%find_lang processcore || touch processcore.lang
%find_lang processui || touch processui.lang
