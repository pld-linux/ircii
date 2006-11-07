Summary:	Popular Unix Irc client
Summary(de):	Beliebter Unix-IRC-Client
Summary(fr):	Client irc UNIX populaire
Summary(pl):	Popularny uniksowy klient IRC
Summary(tr):	Yaygýn Unix Irc istemcisi
Name:		ircii
Version:	20040820
Release:	3
License:	BSD
Group:		Applications/Networking
Vendor:		IRCII Bugs <ircii-bugs@ircii.eterna.com.au>
Source0:	ftp://ircii.warped.com/pub/ircII/%{name}-%{version}.tar.gz
# Source0-md5:	520e3230bffcd26c9112d61b9c65c65d
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
URL:		http://www.eterna.com.au/ircii/
BuildRequires:	autoconf
BuildRequires:	ncompress
BuildRequires:	ncurses-devel >= 5.1
Requires:	ncompress
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ircii-help

%description
This is a popular Internet Relay Chat (IRC) client. It is a program
used to connect to IRC servers around the globe so that the user can
``chat'' with others.

%description -l de
Dies ist ein beliebter IRC-Client (Internet Relay Chat). Sie können
eine Verbindung zu einem beliebigen IRC-Server aufbauen und mit
anderen Benutzern 'chatten'.

%description -l fr
Le très poulaire client Internet Relay Chat (IRC). C'est un programme
utilisé pour se connecter aux serveurs IRC à travers le monde entier
et ``bavarder'' avec les autres.

%description -l pl
Ircii to popularny klient IRC (Internet Relay Chat). S³u¿y do ³±czenia
siê z serwerami IRC dooko³a globu tak, by u¿ytkownicy mogli ze sob±
rozmawiaæ.

%description -l tr
Bu, yaygýn kullanýlan bir IRC (Internet Relay Chat) istemcisidir.
Dünya üzerinde herhangi bir IRC sunucusuna baðlantý saðlar; baðlantý
saðlandýktan sonra kullanýcý diðer insanlarla sohbet edebilir.

%prep
%setup  -q
%patch0 -p1

%build
%configure2_13 \
	--with-paranoid \
	--enable-ipv6 \
	--with-default-server="irc.pld-linux.org poznan.irc.pl wroclaw.irc.pl warszawa.irc.pl krakow.irc.pl lublin.irc.pl" \
	--with-cast
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/irc,%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/irc-%{version} $RPM_BUILD_ROOT%{_bindir}/ircii
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
chmod -R a=rX,u=rwX $RPM_BUILD_ROOT%{_datadir}/irc

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/irc.1
echo ".so ircII.1" > $RPM_BUILD_ROOT%{_mandir}/man1/irc.1


%post
if [ ! -f /etc/irc/ircII.servers ]; then
	if [ ! -d /etc/irc ]; then
		install -d /etc/irc
		chmod 755 /etc/irc
	fi
cat  << EOF > /etc/irc/ircII.servers
irc.pld-linux.org:6667
warszawa.irc.pl:6667
lublin.irc.pl:6667
krakow.irc.pl:6667
poznan.irc.pl:6667
wroclaw.irc.pl:6667
EOF
	chown root:root /etc/irc/ircII.servers
	chmod 644 /etc/irc/ircII.servers
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*ircii
%attr(755,root,root) %dir %{_sysconfdir}/irc
%attr( - ,root,root) %{_datadir}/irc
%{_desktopdir}/*.desktop
%{_mandir}/man*/*
