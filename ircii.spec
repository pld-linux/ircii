Summary:	Popular Unix Irc client
Summary(de.UTF-8):	Beliebter Unix-IRC-Client
Summary(fr.UTF-8):	Client irc UNIX populaire
Summary(pl.UTF-8):	Popularny uniksowy klient IRC
Summary(tr.UTF-8):	Yaygın Unix Irc istemcisi
Name:		ircii
Version:	20111115
Release:	1
License:	BSD
Group:		Applications/Networking
Vendor:		IRCII Bugs <ircii-bugs@ircii.eterna.com.au>
Source0:	ftp://ircii.warped.com/pub/ircII/%{name}-%{version}.tar.gz
# Source0-md5:	8e38ba5828c02fa44289ae3dcbccd04c
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

%description -l de.UTF-8
Dies ist ein beliebter IRC-Client (Internet Relay Chat). Sie können
eine Verbindung zu einem beliebigen IRC-Server aufbauen und mit
anderen Benutzern 'chatten'.

%description -l fr.UTF-8
Le très poulaire client Internet Relay Chat (IRC). C'est un programme
utilisé pour se connecter aux serveurs IRC à travers le monde entier
et ``bavarder'' avec les autres.

%description -l pl.UTF-8
Ircii to popularny klient IRC (Internet Relay Chat). Służy do łączenia
się z serwerami IRC dookoła globu tak, by użytkownicy mogli ze sobą
rozmawiać.

%description -l tr.UTF-8
Bu, yaygın kullanılan bir IRC (Internet Relay Chat) istemcisidir.
Dünya üzerinde herhangi bir IRC sunucusuna bağlantı sağlar; bağlantı
sağlandıktan sonra kullanıcı diğer insanlarla sohbet edebilir.

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

%{__make} -j1 install \
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
