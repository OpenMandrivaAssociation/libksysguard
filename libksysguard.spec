%define devname %mklibname KF5Libksysguard -d
%define desname %mklibname KF5Libksysguard-designer -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define ksgrd_major 9
%define libksgrd %mklibname ksgrd %{ksgrd_major}
%define ksignalplotter_major 9
%define libksignalplotter %mklibname ksignalplotter %{ksignalplotter_major}
%define lsofui_major 9
%define liblsofui %mklibname lsofui %{lsofui_major}
%define processcore_major 9
%define libprocesscore %mklibname processcore %{processcore_major}
%define processui_major 9
%define libprocessui %mklibname processui %{processui_major}
%define formatter_major 1
%define libformatter %mklibname KSysGuardFormatter %{formatter_major}
%define sensorfaces_major 1
%define libsensorfaces %mklibname KSysGuardSensorFaces %{sensorfaces_major}
%define sensors_major 1
%define libsensors %mklibname KSysGuardSensors %{sensors_major}

Name: libksysguard
Version:	5.27.11
Release:	1
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
BuildRequires: cmake(Qt5Designer)
BuildRequires: cmake(Qt5DesignerComponents)
BuildRequires: cmake(Qt5Sensors)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5KDE4Support)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: qt5-qtpositioning
BuildRequires: pkgconfig(libcap)
BuildRequires: lm_sensors-devel

Obsoletes: %mklibname ksignalplotter 7
Obsoletes: %mklibname lsofui 7
Obsoletes: %mklibname processcore 7
Obsoletes: %mklibname processui 7
Obsoletes: %mklibname ksgrd 7

Requires: %{libksgrd} = %{EVRD}
Requires: %{libksignalplotter} = %{EVRD}
Requires: %{liblsofui} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libprocessui} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}

%description
KDE Frameworks 5 system monitoring framework.

%files -f ksgrd.lang
%{_datadir}/qlogging-categories5/libksysguard.categories
%{_datadir}/ksysguard/scripts
%{_libdir}/libexec/kauth/ksysguardprocesslist_helper
%dir %{_libdir}/libexec/ksysguard
%caps(cap_net_raw+ep) %{_libdir}/libexec/ksysguard/ksgrd_network_helper
%{_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/interfaces/org.kde.ksystemstats.xml
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_libdir}/qt5/plugins/kpackage/packagestructure/sensorface_packagestructure.so
%{_libdir}/qt5/qml/org/kde/ksysguard
%{_datadir}/knsrcfiles/systemmonitor-faces.knsrc
%{_datadir}/knsrcfiles/systemmonitor-presets.knsrc
%{_datadir}/ksysguard/sensorfaces
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%dir %{_libdir}/qt5/plugins/ksysguard
%dir %{_libdir}/qt5/plugins/ksysguard/process
%{_libdir}/qt5/plugins/ksysguard/process/ksysguard_plugin_network.so
%{_libdir}/qt5/plugins/ksysguard/process/ksysguard_plugin_nvidia.so

#----------------------------------------------------------------------------

%package -n %{libksgrd}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libksgrd}
Plasma 5 KDE System Guard shared library.

%files -n %{libksgrd}
%{_libdir}/libksgrd.so.%{ksgrd_major}
%{_libdir}/libksgrd.so.5*
%{_libdir}/libKSysGuardSystemStats.so.1
%{_libdir}/libKSysGuardSystemStats.so.5*

#----------------------------------------------------------------------------

%package -n %{libksignalplotter}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libksignalplotter}
Plasma 5 KDE System Guard shared library.

%files -n %{libksignalplotter}
%{_libdir}/libksignalplotter.so.%{ksignalplotter_major}
%{_libdir}/libksignalplotter.so.5*

#----------------------------------------------------------------------------

%package -n %{liblsofui}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{liblsofui}
Plasma 5 KDE System Guard shared library.

%files -n %{liblsofui}
%{_libdir}/liblsofui.so.%{lsofui_major}
%{_libdir}/liblsofui.so.5*

#----------------------------------------------------------------------------

%package -n %{libprocesscore}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocesscore}
Plasma 5 KDE System Guard shared library.

%files -n %{libprocesscore}
%{_libdir}/libprocesscore.so.%{processcore_major}
%{_libdir}/libprocesscore.so.5*

#----------------------------------------------------------------------------

%package -n %{libprocessui}
Summary: Plasma 5 KDE System Guard shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libprocessui}
Plasma 5 KDE System Guard shared library.

%files -n %{libprocessui}
%{_libdir}/libprocessui.so.%{processui_major}
%{_libdir}/libprocessui.so.5*

#----------------------------------------------------------------------------

%package -n %{libformatter}
Summary: Plasma 5 KDE System Guard formatting library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libformatter}
Plasma 5 KDE System Guard formatting shared library.

%files -n %{libformatter}
%{_libdir}/libKSysGuardFormatter.so.%{formatter_major}
%{_libdir}/libKSysGuardFormatter.so.5*

#----------------------------------------------------------------------------

%package -n %{libsensorfaces}
Summary: Plasma 5 KDE System Guard sensor faces shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libsensorfaces}
Plasma 5 KDE System Guard sensor faces shared library.

%files -n %{libsensorfaces}
%{_libdir}/libKSysGuardSensorFaces.so.%{sensorfaces_major}
%{_libdir}/libKSysGuardSensorFaces.so.5*

#----------------------------------------------------------------------------

%package -n %{libsensors}
Summary: Plasma 5 KDE System Guard sensors shared library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libsensors}
Plasma 5 KDE System Guard sensors shared library.

%files -n %{libsensors}
%{_libdir}/libKSysGuardSensors.so.%{sensors_major}
%{_libdir}/libKSysGuardSensors.so.5*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 system monitoring library
Group: Development/KDE and Qt
Requires: %{libksgrd} = %{EVRD}
Requires: %{libksignalplotter} = %{EVRD}
Requires: %{liblsofui} = %{EVRD}
Requires: %{libprocesscore} = %{EVRD}
Requires: %{libprocessui} = %{EVRD}
Requires: %{libformatter} = %{EVRD}
Requires: %{libsensorfaces} = %{EVRD}
Requires: %{libsensors} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 system monitoring library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/cmake/KSysGuard

%package -n %{desname}
Summary: Qt Designer plugin integrating KSysguard's widgets
Group: Development/KDE and Qt
Requires: %{devname} = %{EVRD}

%description -n %{desname}
Qt Designer plugin integrating KSysguard's widgets.

%files -n %{desname}
%{_libdir}/qt5/plugins/designer/ksignalplotter5widgets.so
%{_libdir}/qt5/plugins/designer/ksysguard5widgets.so
%{_libdir}/qt5/plugins/designer/ksysguardlsof5widgets.so

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang ksgrd --all-name --with-html
