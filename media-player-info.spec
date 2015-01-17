Summary:	Media Player Information
Name:		media-player-info
Version:	22
Release:	1
Group:		System/Kernel and hardware
License:	BSD
Url:		http://people.freedesktop.org/~teuf/media-player-info/
Source0:	http://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3
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
%configure
%make

%install
%makeinstall_std

%files
%doc README NEWS
%dir %{_datadir}/media-player-info
 %{_datadir}/media-player-info/*.mpi
/lib/udev/rules.d/40-usb-media-players.rules
/lib/udev/hwdb.d/20-usb-media-players.hwdb
