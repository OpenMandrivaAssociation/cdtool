Summary:	Powerful command line CDROM player and tools
Name:		cdtool
Version:	2.1.8
Release:	8
License:	GPLv2
Group:		Sound
URL:		http://hinterhof.net/cdtool/
Source0:	http://hinterhof.net/cdtool/dist/%name-%version.tar.bz2
# fixes error: conflicting types for 'getline' 09 Jun 2009
Patch0:		%{name}-2.1.8-fix-getline.patch
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
%patch0 -p1
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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.8-7mdv2011.0
+ Revision: 616991
- the mass rebuild of 2010.0 packages

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 2.1.8-6mdv2010.0
+ Revision: 384520
- fix getline error
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.1.8-5mdv2009.0
+ Revision: 243469
- rebuild

* Thu Feb 21 2008 Adam Williamson <awilliamson@mandriva.org> 2.1.8-3mdv2008.1
+ Revision: 173777
- fix hardcoded /lib with %%_lib (broke half the commands on x86_64, #37975)
- replace configure.patch with substitions

* Mon Jan 28 2008 Adam Williamson <awilliamson@mandriva.org> 2.1.8-2mdv2008.1
+ Revision: 159037
- rename cdplay to cdplay-cdtool to fix #21020, drop conflict with cdp
- new license policy
- rewrap description
- clean spec

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.1.8-1mdv2008.1
+ Revision: 136290
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Nov 30 2006 Lenny Cartier <lenny@mandriva.com> 2.1.8-1mdv2007.0
+ Revision: 89252
- Update to 2.1.8 (sorry rtp, joey potter owns me)
- Import cdtool

