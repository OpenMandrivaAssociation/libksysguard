%define major 5
%define libname %mklibname KF5Libksysguard %{major}
%define devname %mklibname KF5Libksysguard -d
%define debug_package %{nil}

Name: libksysguard
Version: 5.0.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/plasma/%{version}/%{name}-%{version}.tar.xz
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
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 system monitoring framework

%package -n %{libname}
Summary: KDE Frameworks system monitoring framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 system monitoring framework

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 system monitoring library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 system monitoring library

%prep
%setup -q
%cmake -G Ninja

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

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.4.98.0

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
