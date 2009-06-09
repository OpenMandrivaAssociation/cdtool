Summary:	Powerful command line CDROM player and tools
Name:		cdtool
Version:	2.1.8
Release:	%mkrel 6
License:	GPLv2
Group:		Sound
URL:		http://hinterhof.net/cdtool/
Source0:	http://hinterhof.net/cdtool/dist/%name-%version.tar.bz2
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
A package of command-line utilities to play and catalog audio CD-ROMs.
This package includes cdstart, cdpause, cdstop, cdeject, and
cdshuffle. Also, cdctrl may be used as a CD-ROM control daemon. Cdown
allows querying of the cddb database to build a local database of
discs usable by cdinfo, etc.

%prep
rm -rf %{buildroot}
%setup -q
sed -i -e 's, -o root,,g' Makefile.in
sed -i -e 's,/lib,/%{_lib},g' Makefile.in

%build
%configure
make RPM_OPT_FLAGS="%{optflags}"

%install
%makeinstall
# don't conflict with cdp (#21020) - AdamW 2008/01
mv %{buildroot}%{_bindir}/cdplay %{buildroot}%{_bindir}/cdplay-cdtool
mv %{buildroot}%{_mandir}/man1/cdplay.1 %{buildroot}%{_mandir}/man1/cdplay-cdtool.1

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/cdtool/*
%defattr(644,root,root,755)
%doc README INSTALL


