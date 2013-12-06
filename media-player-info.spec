Summary:	Media Player Information
Name:		media-player-info
Version:	17
Release:	3
Group:		System/Kernel and hardware
License:	BSD
Url:		http://people.freedesktop.org/~teuf/media-player-info/
Source0:	http://people.freedesktop.org/~teuf/media-player-info/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(udev)

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
%makeinstall_std

%files
%doc README NEWS
%dir %{_datadir}/media-player-info
 %{_datadir}/media-player-info/*.mpi
/lib/udev/rules.d/40-usb-media-players.rules

