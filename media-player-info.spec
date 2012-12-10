Name:		media-player-info
Version:	17
Release:	%mkrel 1
Summary:	Media Player Information
Group:		System/Kernel and hardware
License:	BSD
URL:		http://people.freedesktop.org/~teuf/media-player-info/
Source0:	http://people.freedesktop.org/~teuf/media-player-info/%{name}-%{version}.tar.gz
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
%makeinstall_std

%files
%doc README NEWS
%dir %{_datadir}/media-player-info
 %{_datadir}/media-player-info/*.mpi
/lib/udev/rules.d/40-usb-media-players.rules


%changelog
* Thu May 31 2012 Alexander Khrukin <akhrukin@mandriva.org> 17-1mdv2012.0
+ Revision: 801520
- version update 17

* Tue Aug 24 2010 Christophe Fergeau <cfergeau@mandriva.com> 7-1mdv2011.0
+ Revision: 572676
- release 7
- media-player-info 6

* Fri Mar 19 2010 Christophe Fergeau <cfergeau@mandriva.com> 5-1mdv2010.1
+ Revision: 525215
- fix udev rule file name
- new media-player-info release

* Thu Jan 21 2010 Christophe Fergeau <cfergeau@mandriva.com> 4-1mdv2010.1
+ Revision: 494497
- new upstream release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3-1mdv2010.0
+ Revision: 424582
- update to version 3

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2-1mdv2010.0
+ Revision: 423608
- add missing BuildRequires
- import media-player-info

