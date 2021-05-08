Summary:	Media Player Information
Name:		media-player-info
Version:	24
Release:	2
Group:		System/Kernel and hardware
License:	BSD
Url:		https://www.freedesktop.org/wiki/Software/media-player-info
Source0:	http://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3
BuildRequires:	pkgconfig(udev)
BuildRequires:	systemd-rpm-macros

%description
This is the freedesktop.org media player information database.

This package contains udev rules to identify media players as well as a
compilation of .mpi files describing the media player capabilities of these
devices. This information used to live in hal-info, but it has been moved to
its own package as part of the "halectomy".

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc NEWS
%dir %{_datadir}/media-player-info
%{_datadir}/media-player-info/*.mpi
%{_udevrulesdir}/40-usb-media-players.rules
%{_udevhwdbdir}/20-usb-media-players.hwdb
