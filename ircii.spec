Summary:	Popular Unix Irc client
Name:		ircii
Version:	4.4G
Release:	1d
Copyright:	BSD
Group:		Applications/Communications
Source:		ftp://ircii.warped.com/pub/ircII/ircii-current.tar.gz
Source1:	ircii.wmconfig
Patch1:		ircii-current-debian.patch
Patch2:		ircii-4.4B.non-blocking.patch
Patch3:		ircii-4.4B.config.patch
Obsoletes:	ircii-help
Buildroot:	/var/tmp/%{name}-%{version}-buildroot
Summary(de):	Beliebter Unix-IRC-Client
Summary(fr):	Client irc UNIX populaire.
Summary(tr):	Yaygýn Unix Irc istemcisi
Summary(pl):	Popularny Unixowy Klient Irc

%description
This is a popular Internet Relay Chat (IRC) client.  It
is a program used to connect to IRC servers around the
globe so that the user can ``chat'' with others.

%description -l pl
To jest popularny klient IRC (Internet Relay Chat). To jest
program u¿ywany do ³±czenia siê z serwerami IRC dooko³a
globu tak by u¿ytkownicy mogli ze sob± rozmawiaæ.

%description -l de
Dies ist ein beliebter IRC-Client (Internet Relay Chat). Sie können eine
Verbindung zu einem beliebigen IRC-Server aufbauen und mit
anderen Benutzern 'chatten'.

%description -l fr
Le très poulaire client Internet Relay Chat (IRC). C'est
un programme utilisé pour se connecter aux serveurs IRC à
travers le monde entier et ``bavarder'' avec les autres.

%description -l tr
Bu, yaygýn kullanýlan bir IRC (Internet Relay Chat) istemcisidir. Dünya
üzerinde herhangi bir IRC sunucusuna baðlantý saðlar; baðlantý saðlandýktan
sonra kullanýcý diðer insanlarla sohbet edebilir.

%prep
%setup -q -n %{name}-current
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -rf `find . -name CVS`
CFLAGS="$RPM_OPT_FLAGS -DDEBIAN" LDFLAGS=-s \
./configure %{_target} \
    --prefix=/usr \
    --with-cast \
    --with-default-server=warszawa.irc.pl:6667
    
cd include; make; cd ..
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make prefix=$RPM_BUILD_ROOT/usr install
ln -sf irc-%{version} $RPM_BUILD_ROOT/usr/bin/irc

install %SOURCE1 $RPM_BUILD_ROOT/etc/X11/wmconfig/ircii

strip $RPM_BUILD_ROOT/usr/bin/* || :

gzip -9nf doc/* $RPM_BUILD_ROOT%{_mandir}/man1/*

%post
if [ ! -f /etc/irc/ircII.servers ]; then
if [ ! -d /etc/irc ]; then
install -d /etc/irc
fi
cat  << EOF > /etc/irc/ircII.servers
warszawa.irc.pl:6667
lublin.irc.pl:6667
krakow.irc.pl:6667
poznan.irc.pl:6667
hub.irc.pl:6667
EOF
chown root.root /etc/irc
chown root.root /etc/irc/ircII.servers
chmod 755 /etc/irc
chmod 644 /etc/irc/ircII.servers
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*

%attr(755,root,root) /usr/bin/*

%attr(644,root,root, 755) /usr/share/irc

%attr(644,root,root) /etc/X11/wmconfig/ircii
%{_mandir}/man1/*

%changelog
* Thu Mar 04 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- updated to 4.4G
- man pages are now gzipped
- added patch from debian

* Fri Feb 19 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- updated to 4.4F

* Thu Jan 07 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- updated to 4.4E

* Wed Jan 06 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- many, many changes
- spec rewrited
- added color and irc2-10 patch
- PLDized

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- obsoletes ircii-help (donnie, don't do ever that again!)

* Wed Jun 03 1998 <djb@redhat.com>
- moved help stuff into main package

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 4.4
- changed to use a build root

* Wed Nov  5 1997 Otto Hammersmith <otto@redhat.com>
- moved wmconfig file from ircii-help file list

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- use termios, not termio

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added Erik's patch to fix file closing brokenness.

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated source urls

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
