%define name cdtool
%define version 2.1.8
%define release %mkrel 1

Summary: Powerful command line CDROM player and tools
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sound
Url: http://hinterhof.net/cdtool/
Source: http://hinterhof.net/cdtool/dist/%name-%version.tar.bz2
Patch0: cdtool-configure.patch
Conflicts: cdp

%description
A package of command-line utilities to play and
catalog audio CD-ROMs.  This package includes 
cdstart, cdpause, cdstop, cdeject, and cdshuffle.
Also, cdctrl may be used as a CD-ROM control daemon.
Cdown allows querying of the cddb database to build a 
local database of discs usable by cdinfo, etc.


%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch0 -p1

%build

%configure

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/cdtool/*
%defattr(644,root,root,755)
%doc README COPYING INSTALL


