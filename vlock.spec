Summary: A program which locks one or more virtual consoles
Name: vlock
Version: 1.3
Release: 31%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://cthulhu.c3d2.de/~toidinamai/vlock/vlock.html
Source: http://cthulhu.c3d2.de/~toidinamai/vlock/archive/vlock-1.3.tar.gz

Requires: pam >= 0.59, /etc/pam.d/system-auth
Buildrequires: pam-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0: vlock-1.3-system-auth.patch
# 164950 - call account management and credential reinitialization functions
Patch1: vlock-1.3-morepam.patch
# 170488 - add screen(1) warning
Patch2: vlock-1.3-screen.patch
Patch3: vlock-1.3-gcc.patch

%description
The vlock program locks one or more sessions on the console.  Vlock
can lock the current terminal (local or remote) or the entire virtual
console system, which completely disables all console access.  The
vlock program unlocks when either the password of the user who started
vlock or the root password is typed.

Install vlock if you need to disable access to one console or to all
virtual consoles.

%prep
%setup -q
%patch0 -p1 -b .system-auth
%patch1 -p1 -b .morepam
%patch2 -p1 -b .screen
%patch3 -p1 -b .gcc

%build
make RPM_OPT_FLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -p -m 755 vlock $RPM_BUILD_ROOT%{_bindir}/
install -p -m 644 vlock.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 vlock.pamd $RPM_BUILD_ROOT/etc/pam.d/vlock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%config(noreplace) %{_sysconfdir}/pam.d/vlock
%{_bindir}/vlock
%{_mandir}/man1/vlock.1*

%changelog
* Tue Feb 16 2010 Karel Zak <kzak@redhat.com> - 1.3-31
- minor fixes in spec file

* Thu Jan  7 2010 Karel Zak <kzak@redhat.com> - 1.3-30
- fix upstream URLs

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3-29.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-27
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-26
- Autorebuild for GCC 4.3

* Thu Mar  1 2007 Karel Zak <kzak@redhat.com> - 1.3-25
- add missing -p to install calls

* Thu Mar  1 2007 Karel Zak <kzak@redhat.com> - 1.3-24
- fix #226530 - Merge Review: vlock

* Wed Jul 19 2006 Karel Zak <kzak@redhat.com> - 1.3-23
- spec file cleanup & rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.3-22.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.3-22.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.3-22.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Oct 14 2005 Karel Zak <kzak@redhat.com> 1.3-22
- fix #170488 - add screen(1) warning
- compilation warnings cleanup

* Thu Oct 13 2005 Karel Zak <kzak@redhat.com> 1.3-21
- replace pam_stack with "include"

* Wed Aug  3 2005 Karel Zak <kzak@redhat.com> 1.3-20
- #164950 - call account management and credential reinitialization functions
  (patch by Nalin Dahyabhai)

* Tue May 10 2005 Karel Zak <kzak@redhat.com> 1.3-19
- fix debuginfo

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 14 2005 Adrian Havill <havill@redhat.com>
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 12 2002 Nalin Dahyabhai <nalin@redhat.com> 1.3-12
- remove absolute paths from PAM configuration for use on multilib systems

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jul 23 2001 Michael K. Johnson <johnsonm@redhat.com>
- added pam-devel buildrequires

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 01 2000 Nalin Dahyahai <nalin@redhat.com> 
- change PAM setup to use system-auth
- move man pages to %%{_mandir}

* Tue Feb 08 2000 Nalin Dahyahai <nalin@redhat.com> 
- handle compressed man pages
- use defattr instead of explicit ownership at install-time

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Jan 13 1999 Michael Johnson <johnsonm@redhat.com>
- released 1.3

* Thu Mar 12 1998 Michael K. Johnson <johnsonm@redhat.com>
- Does not create a DoS attack if pty is closed (not applicable
  to use on a VC)

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam conventions.
- Use pam according to spec, rather than abusing it as before.
- Updated to version 1.1.
- BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- moved from pam.conf to pam.d
