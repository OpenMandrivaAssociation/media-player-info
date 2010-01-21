Name:		media-player-info
Version:	4
Release:	%mkrel 1
Summary:	Media Player Information
Group:		System/Kernel and hardware
License:	BSD
URL:		http://people.freedesktop.org/~teuf/media-player-info/
Source:		http://people.freedesktop.org/~teuf/media-player-info/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python
BuildRequires:	udev-devel
BuildArch:	noarch

%description
This is the freedesktop.org media player information database.

This package contains udev rules to identify media players as well as a 
compilation of .mpi files describing the media player capabilities of these
devices. This information used to live in hal-info, but it has been moved to 
its own package as part of the "halectomy".

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README NEWS
%dir %{_datadir}/media-player-info
 %{_datadir}/media-player-info/*.mpi
/lib/udev/rules.d/90-usb-media-players.rules
